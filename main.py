import cv2
import dlib
import numpy as np
from scipy.spatial import distance

from playsound import playsound
import threading

# -----------------------------
# ALARM SYSTEM
# -----------------------------

alarm_on = False

def start_alarm():
    global alarm_on
    if not alarm_on:
        alarm_on = True
        threading.Thread(target=play_alarm_sound).start()

def play_alarm_sound():
    global alarm_on
    playsound("alaram_3.wav")   # put your wav file in the same folder
    alarm_on = False


# -----------------------------
# EAR CALCULATION (Eye Aspect Ratio)
# -----------------------------

def calculate_ear(eye):
    A = distance.euclidean(eye[1], eye[5])
    B = distance.euclidean(eye[2], eye[4])
    C = distance.euclidean(eye[0], eye[3])
    ear = (A + B) / (2.0 * C)
    return ear


# -----------------------------
# MAR CALCULATION (Mouth Aspect Ratio)
# -----------------------------

def calculate_mar(mouth):
    A = distance.euclidean(mouth[2], mouth[10])
    B = distance.euclidean(mouth[4], mouth[8])
    C = distance.euclidean(mouth[0], mouth[6])
    mar = (A + B) / (2.0 * C)
    return mar


# -----------------------------
# CONSTANTS AND THRESHOLDS
# -----------------------------

EAR_THRESHOLD = 0.25            # Below this → eyes are closing
EAR_CONSEC_FRAMES = 20          # More frames = more strict
MAR_THRESHOLD = 0.70            # Above this → yawning

COUNTER = 0
YAWN_COUNT = 0


# -----------------------------
# LOAD DLIB MODELS
# -----------------------------

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")


# -----------------------------
# START WEBCAM
# -----------------------------

cap = cv2.VideoCapture(0)


while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = detector(gray)

    for face in faces:

        # Get landmarks
        shape = predictor(gray, face)
        landmarks = np.array([[p.x, p.y] for p in shape.parts()])

        # Eye coordinates
        left_eye = landmarks[36:42]
        right_eye = landmarks[42:48]

        # Mouth coordinates
        mouth = landmarks[48:68]

        # Calculate EAR & MAR
        left_ear = calculate_ear(left_eye)
        right_ear = calculate_ear(right_eye)
        ear = (left_ear + right_ear) / 2.0

        mar = calculate_mar(mouth)

        # Draw polygons
        cv2.polylines(frame, [left_eye], True, (0, 255, 0), 1)
        cv2.polylines(frame, [right_eye], True, (0, 255, 0), 1)
        cv2.polylines(frame, [mouth], True, (255, 0, 0), 1)

        # -----------------------------
        # DROWSINESS (EYE CLOSURE)
        # -----------------------------
        if ear < EAR_THRESHOLD:
            COUNTER += 1

            if COUNTER >= EAR_CONSEC_FRAMES:
                cv2.putText(frame, "DROWSINESS ALERT!", (50, 100),
                            cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 0, 255), 3)
                start_alarm()
        else:
            COUNTER = 0
            alarm_on = False

        # -----------------------------
        # YAWN DETECTION
        # -----------------------------
        if mar > MAR_THRESHOLD:
            YAWN_COUNT += 1
            cv2.putText(frame, "YAWNING!", (50, 150),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.2, (255, 0, 0), 3)

        # -----------------------------
        # DISPLAY METRICS
        # -----------------------------

        cv2.putText(frame, f"EAR: {ear:.2f}", (500, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 255), 2)
        cv2.putText(frame, f"MAR: {mar:.2f}", (500, 70),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 255), 2)

    # Show output
    cv2.imshow("Driver Drowsiness Detection System", frame)

    if cv2.waitKey(1) == 27:  # ESC to exit
        break

cap.release()
cv2.destroyAllWindows()
