import cv2
import face_recognition
import os
from datetime import datetime

def load_registered_faces():
    """Load all registered faces and their names."""
    faces = []
    names = []
    for filename in os.listdir('registered_students'):
        if filename.endswith('.jpg'):
            img_path = os.path.join('registered_students', filename)
            img = face_recognition.load_image_file(img_path)
            
            # Get face encodings
            encodings = face_recognition.face_encodings(img)
            if len(encodings) > 0:  # Check if a face was detected
                faces.append(encodings[0])
                names.append(filename.split('.')[0])
            else:
                print(f"Warning: No face detected in {filename}. Skipping this file.")
    return faces, names


def mark_attendance(name):
    """Mark attendance in the attendance log file."""
    with open('attendance_log.csv', 'a') as f:
        now = datetime.now()
        dt_string = now.strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"{name},{dt_string}\n")
    print(f"{name} marked as present on {dt_string}.")

def recognize_faces():
    """Recognize faces using the webcam."""
    known_faces, known_names = load_registered_faces()

    # Initialize webcam
    cam = cv2.VideoCapture(0)
    print("Press 'q' to quit.")

    while True:
        ret, frame = cam.read()
        if not ret:
            print("Failed to capture frame.")
            break

        # Resize frame for faster processing
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
        rgb_frame = rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)


        # Find all face locations and encodings in the frame
        face_locations = face_recognition.face_locations(rgb_frame)
        face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

        for face_encoding, face_location in zip(face_encodings, face_locations):
            matches = face_recognition.compare_faces(known_faces, face_encoding)
            name = "Unknown"

            # Use the known face with the smallest distance
            face_distances = face_recognition.face_distance(known_faces, face_encoding)
            best_match_index = face_distances.argmin() if len(face_distances) > 0 else None

            if best_match_index is not None and matches[best_match_index]:
                name = known_names[best_match_index]
                mark_attendance(name)

            # Draw rectangle around the face
            top, right, bottom, left = [v * 4 for v in face_location]
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
            cv2.putText(frame, name, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (255, 0, 0), 2)

        # Display the frame
        cv2.imshow("Attendance System", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cam.release()
    cv2.destroyAllWindows()

recognize_faces()
