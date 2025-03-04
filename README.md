# Face Recognition System

## Overview
This project implements a real-time face recognition system using OpenCV and the `face_recognition` library. It detects and recognizes known faces from a directory and marks unknown faces accordingly.

## Features
- Detects faces in a live video stream.
- Recognizes known faces by comparing them with stored face encodings.
- Displays bounding boxes and names for recognized faces.
- Identifies unknown faces.
- Allows users to quit the application by pressing 'q'.

## Prerequisites
Ensure you have the following dependencies installed:

- Python 3.x
- OpenCV (`cv2`)
- `face_recognition` library
- NumPy

### Install Dependencies
Run the following command to install required dependencies:
```sh
pip install opencv-python numpy face-recognition
```

## Project Structure
```
face_recognition_project/
│── known_faces/          # Directory containing known face images (JPG/PNG files)
│── face_recognition.py   # Main script for face recognition
│── README.md             # Documentation
```

## Usage
1. **Add known faces:** Place images of known individuals in the `known_faces/` directory. Ensure the filenames correspond to the person's name (e.g., `john_doe.jpg`).
2. **Run the script:** Execute the following command:
   ```sh
   python face_recognition.py
   ```
3. **Interacting with the system:**
   - The camera will start capturing video.
   - Recognized faces will be labeled with their names.
   - Unknown faces will be labeled as "Unknown."
   - Press 'q' to exit the program.

## Troubleshooting
- Ensure your webcam is properly connected.
- If the program fails to detect faces, try using clearer images.
- If dependencies are not installed, use the provided `pip install` command.

## Future Enhancements
- Improve accuracy using deep learning models like FaceNet.
- Implement automatic face registration for unknown users.
- Store face encodings in a database instead of reloading images on every run.
- Deploy as a web-based system using Flask/Django and React.js.



