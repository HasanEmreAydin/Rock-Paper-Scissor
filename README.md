# Intelligent Robot Arm for Rock-Paper-Scissors Game

## Overview
This project integrates computer vision, robotics, and machine learning to create a humanoid robotic arm capable of playing the classic game Rock-Paper-Scissors (RPS) in real time. The system detects human gestures using a YOLO-based model, determines the optimal robot response, and performs corresponding gestures using an Arduino-controlled robotic arm.

## Features
- **Real-Time Gesture Recognition**: Utilizes YOLOv8 for detecting hand gestures with high accuracy and low latency.
- **Robotic Arm Control**: Implements Arduino-based servo motor control for smooth and precise gesture execution.
- **Interactive Gameplay**: The robot dynamically responds to human gestures using a winning strategy logic.
- **System Optimization**: Threading and resolution adjustments ensure efficient performance.

## System Architecture
The project consists of two main components:
1. **Gesture Detection Module**: Written in Python, this module uses YOLOv8 to classify user gestures and communicates with the Arduino.
2. **Robotic Control Module**: Written in Arduino C++, this module controls the servo motors of the robotic arm to replicate gestures.

---

## Requirements

### Hardware
- **Robotic Arm**: Modular InMoov humanoid robotic arm (3D-printed parts).
- **Servo Motors**: MG996R (x5) for controlling the fingers and wrist.
- **Microcontroller**: Arduino Uno.
- **Camera**: Logitech or any compatible 2D camera.
- **Servo Driver**: Adafruit 16-Channel PWM/Servo Driver.
- **Computer**: For running Python-based detection software.

### Software
- Python 3.9 or later
- YOLOv8 (via `ultralytics` library)
- OpenCV
- Arduino IDE

---

## Installation

### Python Setup
```bash
git clone https://github.com/HasanEmreAydin/Rock-Paper-Scissors
cd Rock-Paper-Scissors
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
