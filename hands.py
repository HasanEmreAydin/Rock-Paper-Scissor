import cv2
import mediapipe as mp
import numpy as np

class RPSHandGesture:
    def __init__(self):
        self.mp_hands = mp.solutions.hands
        self.mp_drawing = mp.solutions.drawing_utils
        self.cap = cv2.VideoCapture(0)

    def get_hand_gesture(self, hand_landmarks, image_height):
        # Parmakların durumlarını kontrol et
        index_finger = [
            int(hand_landmarks.landmark[8].y * image_height),
            int(hand_landmarks.landmark[6].y * image_height)
        ]
        middle_finger = [
            int(hand_landmarks.landmark[12].y * image_height),
            int(hand_landmarks.landmark[10].y * image_height)
        ]
        ring_finger = [
            int(hand_landmarks.landmark[16].y * image_height),
            int(hand_landmarks.landmark[14].y * image_height)
        ]
        pinky_finger = [
            int(hand_landmarks.landmark[20].y * image_height),
            int(hand_landmarks.landmark[18].y * image_height)
        ]
        
        # Taş, Kağıt, Makas belirleme
        if all([index_finger[0] > index_finger[1], middle_finger[0] > middle_finger[1], 
                ring_finger[0] > ring_finger[1], pinky_finger[0] > pinky_finger[1]]):
            return "Rock"
        elif ring_finger[0] > ring_finger[1] and pinky_finger[0] > pinky_finger[1]:
            return "Scissors"
        else:
            return "paper"

    def run(self):
        with self.mp_hands.Hands(min_detection_confidence=0.5, min_tracking_confidence=0.5) as hands:
            while self.cap.isOpened():
                success, image = self.cap.read()
                if not success:
                    print("Kamera çerçevesi alınamadı.")
                    break

                image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
                results = hands.process(image)
                image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

                if results.multi_hand_landmarks:
                    for hand_landmarks in results.multi_hand_landmarks:
                        gesture = self.get_hand_gesture(hand_landmarks, image.shape[0])
                        cv2.putText(image, gesture, (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 255), 2)

                        # El çizimleri
                        self.mp_drawing.draw_landmarks(image, hand_landmarks, self.mp_hands.HAND_CONNECTIONS)

                cv2.imshow('Rock Paper Scissors', image)
                if cv2.waitKey(1) & 0xFF == 27:
                    break

        self.cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    rps_detector = RPSHandGesture()
    rps_detector.run()
