# 🎓 Face Recognition Attendance System

An AI-powered attendance system that uses real-time face recognition to automatically mark student attendance using a webcam.

---

## 🚀 Features

- Student face registration via webcam
- Real-time face detection and recognition
- Automatic attendance logging with date & time
- CSV-based attendance record storage
- Duplicate attendance prevention
- Face bounding box display

---

## 🛠 Technologies Used

- Python
- OpenCV
- face_recognition
- NumPy
- CSV file handling

---

## 📂 Project Structure

```
first.py    → Register student face
second.py   → Recognize faces & mark attendance
third.py    → Alternative recognition version
registered_students/ → Stores captured images
attendance_log.csv   → Stores attendance records
```

---

## ⚙ Installation

1. Clone the repository:

```
git clone https://github.com/Hemant9650/face-recognition-attendance-system.git
```

2. Go into the project folder:

```
cd face-recognition-attendance-system
```

3. Install dependencies:

```
pip install -r requirements.txt
```

---

## ▶ How to Run

### Step 1: Register Students
```
python first.py
```

### Step 2: Start Attendance System
```
python second.py
```

Press **'q'** to exit the camera.

---

## 📌 Future Improvements

- GUI interface
- Database integration
- Cloud deployment
- Multi-user authentication
- Real-time dashboard

---

## 👨‍💻 Author

Hemant9650
