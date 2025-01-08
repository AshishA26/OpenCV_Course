# FACE DETECTION with HAAR CASCADE
# - detects prescense of a face in an image
# - different from face recognition
# - sensitive to noise

import cv2 as cv

img = cv.imread('Photos/group 1.jpg')
cv.imshow('Person', img)
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# read in xml file (from openCV github)
haar_cascade = cv.CascadeClassifier('haar_face.xml')

# detect faces
# lower minNeighbors makes it more prone to noise
faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=1)

print(f'Number of faces found = {len(faces_rect)}')

# Draw boxes around detections
for (x,y,w,h) in faces_rect:
    cv.rectangle(img, (x,y), (x+w,y+h), (0,255,0), thickness=2)
cv.imshow('Detected face', img)

cv.waitKey(0)