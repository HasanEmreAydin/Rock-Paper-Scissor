import cv2
import serial
from ultralytics import YOLO
from threading import Thread

class RPSHandGestureYOLO:
    def __init__(self, serial_port, model_path, baud_rate=9600):
        self.model = YOLO(model_path)
        self.cap = cv2.VideoCapture(0)
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, 160)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 120)
        self.arduino = serial.Serial(serial_port, baud_rate, timeout=0.05)
        self.robot_move = None

    def determine_robot_move(self, user_gesture):
        moves = {"Rock": "paper", "Paper": "sci", "Scissors": "rock"}
        return moves.get(user_gesture)

    def send_to_robot(self, command):
        if command:
            self.arduino.write(f"{command}\n".encode('utf-8'))

    def process_frame(self, frame):
        results = self.model.predict(frame, conf=0.5, verbose=False)
        if results[0].boxes:
            for box in results[0].boxes:
                label = results[0].names[int(box.cls)]
                if label in ["Rock", "Paper", "Scissors"]:
                    self.robot_move = self.determine_robot_move(label)
                    Thread(target=self.send_to_robot, args=(self.robot_move,)).start()
                    return label
        return None

    def run(self):
        while self.cap.isOpened():
            success, frame = self.cap.read()
            if not success:
                print("Kamera çerçevesi alınamadı.")
                break

            user_gesture = self.process_frame(frame)
            if user_gesture and self.robot_move:
                cv2.putText(frame, f"User: {user_gesture}", (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 255), 2)
                cv2.putText(frame, f"Robot: {self.robot_move}", (10, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 0), 2)

            cv2.imshow('Rock Paper Scissors', frame)
            if cv2.waitKey(1) & 0xFF == 27:  # ESC tuşu ile çıkış
                break

        self.cap.release()
        cv2.destroyAllWindows()
        self.arduino.close()

if __name__ == "__main__":
    serial_port = 'COM4'
    model_path = 'best3.pt'
    rps_detector = RPSHandGestureYOLO(serial_port, model_path)
    rps_detector.run()
