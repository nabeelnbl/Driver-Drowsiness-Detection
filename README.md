Here is a **clean, professional README** you can directly copy-paste into your GitHub.
(Simple English, no LaTeX, no curly braces, no sections.)

---

# Driver Drowsiness Detection System

This project detects driver drowsiness in real time using eye-blink detection and yawn detection.
The system uses OpenCV, dlib, and facial landmark analysis to monitor eye aspect ratio (EAR) and mouth aspect ratio (MAR).
If the driver is sleepy or yawning, an alarm sound is triggered automatically.

---

## Features

* Real-time webcam monitoring
* Eye Aspect Ratio (EAR) for blink and eye-closure detection
* Mouth Aspect Ratio (MAR) for yawn detection
* Automatic alarm alert using an audio file
* Facial landmark visualization on eyes and mouth

---

## Technologies Used

* Python
* OpenCV
* dlib
* numpy
* scipy
* threading
* playsound

---

## Setup Instructions

### 1. Clone this repository

```
git clone https://github.com/your-username/your-repository.git
cd your-repository
```

### 2. Create and activate environment

```
python -m venv venv
```

Windows:

```
venv\Scripts\activate
```

macOS / Linux:

```
source venv/bin/activate
```

### 3. Install dependencies

```
pip install opencv-python dlib numpy scipy playsound
```

### 4. Download the face landmarks model

Download the file:

shape_predictor_68_face_landmarks.dat

Link (official dlib model):
[https://dlib.net/files/shape_predictor_68_face_landmarks.dat.bz2](https://dlib.net/files/shape_predictor_68_face_landmarks.dat.bz2)

Extract it and place the .dat file inside your project folder.

### 5. Add alarm sound file

Place your audio file in the same folder and name it:

```
alaram_3.wav
```

---

## Run the Project

Execute the Python script:

```
python main.py
```

Your webcam will start automatically.

Press ESC to exit.

---

## How It Works

### Eye Aspect Ratio (EAR)

* EAR decreases when eyes begin to close
* If EAR stays below threshold for several frames → drowsiness alert

### Mouth Aspect Ratio (MAR)

* MAR increases during a yawn
* If MAR crosses the threshold → yawn detected

### Alarm

* A background thread plays the alarm sound whenever drowsiness is detected

---

## Output Preview

* Real-time window showing face landmarks
* Alerts for

  * DROWSINESS
  * YAWNING
* EAR and MAR values displayed on the screen

---

If you want, I can also make a **GitHub-ready project structure**, **badges**, or **demo GIF instructions**.
