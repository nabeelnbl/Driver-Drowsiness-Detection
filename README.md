\documentclass[12pt]{article}

\usepackage{hyperref}
\usepackage{geometry}
\geometry{a4paper, margin=1in}
\usepackage{titlesec}

\titleformat{\section}{\Large\bfseries}{\thesection.}{0.5em}{}
\titleformat{\subsection}{\bfseries}{\thesubsection}{0.5em}{}

\title{\textbf{Driver Drowsiness Detection Using OpenCV, Dlib \& Machine Learning}}
\author{Mohammed Nabeel}
\date{}

\begin{document}

\maketitle

\section{Project Overview}

Driver drowsiness is a significant factor in road accidents.  
This project detects driver fatigue in \textbf{real-time} using:

\begin{itemize}
    \item OpenCV for video stream processing
    \item Dlib 68 facial landmarks
    \item Eye Aspect Ratio (EAR) for blink detection
    \item Mouth Aspect Ratio (MAR) for yawn detection
    \item Optional Machine Learning classifier for \textit{Alert} vs \textit{Drowsy}
\end{itemize}

The system triggers an alarm when drowsiness is detected.

\section{Features}

\begin{itemize}
    \item Real-time face detection
    \item Eye blink detection
    \item Prolonged eye closure detection
    \item Yawn detection
    \item Facial landmark extraction
    \item Alarm sound on drowsiness
    \item Extendable ML model for better classification
\end{itemize}

\section{Folder Structure}

\begin{verbatim}
Driver_Drowsiness_Detection/
│
├── src/
│   ├── face_landmark_test.py
│   ├── realtime_drowsiness.py
│   ├── features.py
│   └── train_model.py
│
├── data/
│   ├── train/
│   └── test/
│
├── models/
│   └── drowsiness_model.pkl
│
├── resources/
│   └── shape_predictor_68_face_landmarks.dat
│
├── alarm.wav
└── README.tex
\end{verbatim}

\section{Technologies Used}

\begin{itemize}
    \item Python 3.8+
    \item OpenCV
    \item Dlib
    \item Imutils
    \item NumPy \& SciPy
    \item scikit-learn
    \item Playsound
\end{itemize}

\section{Installation \& Setup}

\subsection{Clone the Repository}
\begin{verbatim}
git clone https://github.com/your-username/Driver_Drowsiness_Detection.git
cd Driver_Drowsiness_Detection
\end{verbatim}

\subsection{Install Dependencies}
\begin{verbatim}
pip install -r requirements.txt
\end{verbatim}

Or manually install OpenCV, dlib, numpy, scipy, imutils, scikit-learn, playsound.

\subsection{Download Facial Landmark Model}

Download the landmark predictor from:

\url{http://dlib.net/files/shape_predictor_68_face_landmarks.dat.bz2}

Extract and place the file into:

\begin{verbatim}
resources/shape_predictor_68_face_landmarks.dat
\end{verbatim}

\section{Test Facial Landmark Detection}

Run the following:

\begin{verbatim}
python src/face_landmark_test.py
\end{verbatim}

You should see green landmark points on your face.

\section{Run Real-Time Drowsiness Detection}

Start the main script:

\begin{verbatim}
python src/realtime_drowsiness.py
\end{verbatim}

\subsection*{System Detects:}

\begin{itemize}
    \item EAR threshold → eye closure
    \item MAR threshold → yawn detection
    \item Consecutive frames → drowsiness alert
\end{itemize}

An alarm will play when drowsiness is detected.

\section{Optional: Train Machine Learning Model}

Extract EAR, MAR, and blink features and run:

\begin{verbatim}
python src/train_model.py
\end{verbatim}

This generates:

\begin{verbatim}
models/drowsiness_model.pkl
\end{verbatim}

\section{Future Enhancements}

\begin{itemize}
    \item CNN-based eye state classification
    \item LSTM-based temporal analysis
    \item Dashboard UI
    \item Raspberry Pi deployment
    \item YOLO-based face detection
\end{itemize}

\section{Contribution}

Contributions, ideas, and pull requests are welcome.

\section{License}

This project is licensed under the MIT License.

\section{Author}

\textbf{Mohammed Nabeel}  
AI \& ML Enthusiast

\end{document}
