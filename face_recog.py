import cv2
import face_recognition
import numpy as np
import os

# Load known faces
known_face_encodings = []
known_face_names = []

known_faces_dir = "known_faces"  # Change this to your actual path
for filename in os.listdir(known_faces_dir):
    if filename.endswith(".jpg") or filename.endswith(".png"):
        image = face_recognition.load_image_file(os.path.join(known_faces_dir, filename))
        encodings = face_recognition.face_encodings(image)
        if encodings:  # Ensure that encodings are found
            known_face_encodings.append(encodings[0])  # Use the first encoding found
            known_face_names.append(os.path.splitext(filename)[0])  # Use the filename as the name

# Initialize video capture
video_capture = cv2.VideoCapture(0)

while True:
    ret, frame = video_capture.read()
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Find face locations in the current frame
    face_locations = face_recognition.face_locations(rgb_frame)
    print(f"Detected {len(face_locations)} faces.")

    if face_locations:  # Ensure faces are detected
        # Find face encodings for the detected faces
        face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)
        print(f"Number of face encodings found: {len(face_encodings)}")

        # Iterate through each detected face and compare with known faces
        for face_encoding, face_location in zip(face_encodings, face_locations):
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
            name = "Unknown"

            if True in matches:
                # Find the known face with the smallest distance to the detected face
                face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
                best_match_index = np.argmin(face_distances)
                name = known_face_names[best_match_index]

            # Draw box and label around the face
            (top, right, bottom, left) = face_location
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
            cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
            cv2.putText(frame, name, (left + 6, bottom - 6), cv2.FONT_HERSHEY_DUPLEX, 0.5, (255, 255, 255), 1)

    # Display the video feed
    cv2.imshow('Video', frame)

    # Break loop on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture
video_capture.release()
cv2.destroyAllWindows()
