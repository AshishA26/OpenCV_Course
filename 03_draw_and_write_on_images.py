# DRAW AND WRITE ON IMAGE
# - can draw on a blank image, or read in an image and draw on that

import cv2 as cv
import numpy as np

# Create a blank image. 
# - The tuple is height, width, and number of color channels
# - uint8 is image type.
blank = np.zeros((500, 500,3), dtype = 'uint8')
cv.imshow('Blank', blank)

# 1. Paint the image a certain color (paint all pixels in image green)
blank[:] = 0,255,0
cv.imshow('Green', blank)

# 2. Paint the part of the image
blank[200:300, 300:400] = 0,0,255
cv.imshow('Red', blank)

# 3. Draw a rectangle
cv.rectangle(blank, (0,0), (250,500), (255,0,0), thickness = cv.FILLED)
cv.imshow('Rectangle',blank)
# can also do blank.shape[1]//2 instead of (250,500) for example

# 3. Draw a circle
cv.circle(blank,(blank.shape[1]//2, blank.shape[0]//2), 40, (0,0,255), thickness = 3)
cv.imshow('Circle', blank)

# 4. Draw a line
cv.line(blank, (0,0), (300,243), (255,255,255), thickness = 3)
cv.imshow('Line', blank)

# 5. Write text
cv.putText(blank, 'Hello', (255,255), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0,0,0), 2)
cv.imshow('Text', blank)

cv.waitKey(0)