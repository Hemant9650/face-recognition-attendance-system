import cv2
import os

# Create a folder to store registered images
if not os.path.exists('registered_students'):
    os.makedirs('registered_students')

def register_student():
    name = input("Enter Student's Name: ").strip()
    if not name:
        print("Name cannot be empty.")
        return

    # Initialize webcam
    cam = cv2.VideoCapture(0)
    print("Capturing image. Look at the camera...")

    # Capture a single frame
    ret, frame = cam.read()
    if not ret:
        print("Failed to capture image.")
        cam.release()
        return

    # Save the captured image with the student's name
    img_path = os.path.join('registered_students', f"{name}.jpg")
    cv2.imwrite(img_path, frame)
    print(f"Image saved as {img_path}")

    cam.release()
    cv2.destroyAllWindows()

register_student()
