# FACE RECOGNITION

import cv2 as cv
import numpy as np

# Load the files, lists, and models
people = ['Ben Afflek', 'Elton John', 'Jerry Seinfield', 'Madonna', 'Mindy Kaling']
haar_cascade = cv.CascadeClassifier('haar_face.xml')
# features = np.load('features.npy', allow_pickle=True)
# labels = np.load('labels.npy', allow_pickle=True)
face_recognizer = cv.face.LBPHFaceRecognizer_create()
face_recognizer.read('face_trained_model.yml')

# Read in an image to predict on, and convert to grayscale
img = cv.imread(r'./Faces/train/Ben Afflek/5.jpg')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Person', gray)

# Detect the face in the image
faces_rect = haar_cascade.detectMultiScale(gray, 1.1, 4)
# Loop over every face in the image
for (x,y,w,h) in faces_rect:
    faces_roi = gray[y:y+h, x:x+h]
    # predict who the person is using the face_recognizer we trained
    label, confidence = face_recognizer.predict(faces_roi)
    print(f'Label = {people[label]} with a confidence of {confidence}')
    # Note that confidence of 0, means it 100% matched. Can think of it as error instead.

    # put some text on the image
    cv.putText(img, str(people[label]), (0,20), cv.FONT_HERSHEY_COMPLEX, 1.0, (0,255,0), thickness=2)
    # draw rectangle around the face
    cv.rectangle(img, (x,y), (x+w, y+h), (0,255,0), thickness=2)

cv.imshow('Detected Face', img)

cv.waitKey(0)