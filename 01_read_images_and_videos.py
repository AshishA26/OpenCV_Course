# READING IMAGES AND VIDEOS

import cv2 as cv

# Reading images:
img = cv.imread('Photos/cat_large.jpg') # read in images as a matrix of pixels
cv.imshow('Cat', img) # display image in a new window. 'Cat' is name of the window.
# Note a large image may go off screen

cv.waitKey(0) # waits an infinite amount of time for a keyboard key to be pressed
cv.destroyAllWindows()

# Reading videos:

# get instance of VideoCapture class
capture = cv.VideoCapture('Videos/dog.mp4')
# Use VideoCapture(0) or another integer to get 
# webcam/other connected cameras. Use a path for a video.

while True:
    # Read video frame by frame.
    # Returns the frame itself, and the isTrue bool saying 
    # whether the frame was successfully read in.
    isTrue, frame = capture.read()
    cv.imshow('Video', frame) # display the frame. Looping through this will make it look like a video

    # Stop the video (break out of the loop) if d key is pressed
    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()

# "-215: Assertion Failed" error means file was not found in specified path. 
# In our case we ran out of frames