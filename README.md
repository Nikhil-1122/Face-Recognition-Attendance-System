# Face Recognition Attendance System

A real-time Face Recognition Attendance System that automates attendance marking using computer vision and deep learning techniques.  
The system identifies individuals through a webcam and records attendance with timestamps, reducing manual effort and proxy attendance.

---

## Features

- Real-time face detection and recognition
- Automatic attendance marking with time
- Prevents duplicate attendance entries in a session
- Supports multiple users
- Simple and scalable design

---

## Technologies Used

- Python
- OpenCV
- CNN
- FaceNet (via dlib and face_recognition)
- NumPy
- CSV

---

## Project Structure
Face-Recognition-Attendance-System/
│
├── dataset/ # Contains face image folders (not uploaded to GitHub)
│ ├── Person_1/
│ ├── Person_2/
│
├── capture_faces.py # Capture face images using webcam
├── train_model.py # Train the face recognition model
├── attendance_system.py # Real-time attendance system
└── attendance.csv # Attendance output file


---

## How the System Works

1. Capture multiple face images of each person using a webcam.
2. Train the system to extract facial embeddings using deep learning.
3. Recognize faces in real time using a live video feed.
4. Automatically mark attendance with the current timestamp.
5. Avoid duplicate entries during the same execution.

---

## How to Run the Project
Step 1: Capture Face Images
Run python capture_faces.py
-Enter the person's name
-Press C to capture images
-Capture 20–30 images per person

Step 2: Train the Model
-python train_model.py

Step 3: Run Attendance System
-python attendance_system.py

## Attendance Format
Attendance is stored in a CSV file in the following format:

Name,Time
Nikhil,10:58:12
Rajesh,11:02:45

## Use Cases
-Classroom attendance management
-Office and workplace attendance
-Secure identity verification
-Smart campus applications

## Privacy and Ethics
-Face images are stored locally and not uploaded to GitHub
-No cloud services or external servers are used
-This project is intended for educational and academic purposes only
