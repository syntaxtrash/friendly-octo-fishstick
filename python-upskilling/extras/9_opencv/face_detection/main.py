"""
How to run. Run with virtual environment, it's recommended practice to avoid issues with global pip packages.

1. Navigate to extras/9_opencv/face_detection

2. Get current directory location, run this command:
pwd
3.  Copy the directory location and create a virtual environment, run this command:
python -m venv (file location)/extras/9_opencv/face_detection/faceDetectionEnv
# this will create a folder named faceDetectionEnv

4. Activate the virtual environment (on Windows): 
(file location)/extras/9_opencv/face_detection/faceDetectionEnv/Scripts/activate

(on Unix or MacOS)
(file location)/extras/9_opencv/face_detection/faceDetectionEnv/bin/activate

5. Make sure virtual environment is activated, run this command to check if pip points to faceDetectionEnv:
pip -V 

6. Install opencv for python, run this command:
pip install opencv-python

7. Verify installation, run this command and locate opencv-python:
pip list

8. Run main.py with this command:
python main.py

"""

import cv2
import sys
import logging as log
import datetime as dt
from time import sleep

cascPath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascPath)
log.basicConfig(filename='webcam.log',level=log.INFO)

video_capture = cv2.VideoCapture(0)
anterior = 0

while True:
    if not video_capture.isOpened():
        print('Unable to load camera.')
        sleep(5)
        pass

    # Capture frame-by-frame
    ret, frame = video_capture.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30)
    )

    # Draw a rectangle around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    if anterior != len(faces):
        anterior = len(faces)
        log.info("faces: "+str(len(faces))+" at "+str(dt.datetime.now()))


    # Display the resulting frame
    cv2.imshow('Video', frame)


    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    # Display the resulting frame
    cv2.imshow('Video', frame)

# When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows()