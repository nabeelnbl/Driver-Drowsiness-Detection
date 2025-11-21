# Driver Drowsiness Detection System

### Eye Blink + Yawn Detection using OpenCV, Dlib, and Machine Learning

---

## Overview

Driver drowsiness is a major cause of road accidents. This project detects early signs of fatigue by monitoring:

* Eye closure (blink duration)
* Mouth opening (yawn detection)
* Head pose / focus

The system uses OpenCV, Dlib's facial landmark detection, and a machine learning model to classify whether a driver is **Alert** or **Drowsy** in real time.

---

## Features

* Real-time webcam monitoring
* Eye Aspect Ratio (EAR) calculation
* Mouth Aspect Ratio (MAR) calculation
* ML model to classify drowsiness
* Alarm system when drowsiness is detected
* Accurate facial landmark detection

---

## Tech Stack

* Python
* OpenCV
* Dlib
* Scikit-learn
* NumPy

---

## Dataset

You can use public datasets such as:

* Closed Eyes Dataset
* YawDD (Yawning Detection Dataset)

Dataset labels:

* Open Eyes
* Closed Eyes
* Yawn
* No Yawn

---

## Workflow

### 1. Capture Video

Frames are captured live from the webcam using OpenCV.

### 2. Detect Face and Landmarks

Dlib 68-face landmark model detects the eyes and mouth region.

### 3. Compute EAR (Eye Aspect Ratio)

Formula used:

```
EAR = (distance(p2, p6) + distance(p3, p5)) / (2 * distance(p1, p4))
```

### 4. Compute MAR (Mouth Aspect Ratio)

```
MAR = (distance(p50, p58) + distance(p52, p56) + distance(p51, p57)) / (2 * distance(p48, p54))
```

### 5. Extract Features

* EAR values
* MAR values
* Blink count
* Yawn frequency

### 6. Train ML Model

You can use models like:

* SVM
* Logistic Regression
* Random Forest

Target labels:

* 0 = Alert
* 1 = Drowsy

### 7. Real-Time Prediction

The trained model predicts the state every frame.
If the driver is detected as *Drowsy*, an alarm plays.

---

## Installation

### Clone Repository

```
git clone https://github.com/your-username/drowsiness-detection.git
cd drowsiness-detection
```

### Install Dependencies

```
pip install opencv-python dlib imutils numpy scikit-learn playsound
```

---

## How to Run

Run the real-time detection:

```
python main.py
```

Run the model training:

```
python train_model.py
```

---

## Folder Structure

```
drowsiness-detection/
│── main.py
│── train_model.py
│── utils.py
│── model.pkl
│── alarm.wav
│── README.md
│── dataset/
│    ├── open_eyes/
│    ├── closed_eyes/
│    ├── yawn/
│    └── no_yawn/
```

---

## Results

* Detects eye closure accurately
* Detects yawning
* Works in real time
* Machine learning enhances accuracy

---

## Future Improvements

* Use Deep Learning CNN instead of Dlib
* Convert model to TensorFlow Lite and deploy on mobile
* Raspberry Pi integration


