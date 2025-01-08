# FACE TRAINING
# - use openCV's built-in face recognizer
# - will train based on images in "Faces" folder

import os
import cv2 as cv
import numpy as np

# Get list of people
# people = []
# for i in os.listdir(r'./Faces/train/'):
#     people.append(i)
people = ['Ben Afflek', 'Elton John', 'Jerry Seinfield', 'Madonna', 'Mindy Kaling']

DIR = r'./Faces/train/'

haar_cascade = cv.CascadeClassifier('haar_face.xml')

features = [] # image arrays of faces
labels = [] # whose face is it

# Loop over every persons folder, and every image
# in that folder, and add it to the training set
def create_training_set():
    for person in people:
        # Make a path for the specific person
        path = os.path.join(DIR, person)
        label = people.index(person)
 
        # For every image in the person's folder, get image path,
        # read in the image, and convert to grayscale.
        # Then detect the face, crop to get the roi (region of interest),
        # and append the face to the features list, and the corresponding label 
        # to the labels list.
        for img in os.listdir(path):
            img_path = os.path.join(path, img)
            img_array = cv.imread(img_path)
            gray = cv.cvtColor(img_array, cv.COLOR_BGR2GRAY)
            
            faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4)
            for (x,y,w,h) in faces_rect:
                faces_roi = gray[y:y+h, x:x+w]
                features.append(faces_roi)
                labels.append(label)

create_training_set()
print('Training done -----------------')

# convert to numpy arrays
features = np.array(features, dtype='object')
labels = np.array(labels)
# save the features and labels lists
np.save('features.npy', features)
np.save('labels.npy',labels)

# instantiate the face recognizer
face_recognizer = cv.face.LBPHFaceRecognizer_create()

# Train the recognizer on the features list and the labels list
face_recognizer.train(features, labels)

# save the trained model for use elsewhere
face_recognizer.save('face_trained_model.yml')