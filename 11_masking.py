# MASKING
# - use bitwise operations to do masking
# - masking is focusing on certain portions of image
# - ex. get only faces in an image with people

import cv2 as cv
import numpy as np

img = cv.imread('Photos/cats 2.jpg')
cv.imshow('Cats', img)

# note: dimensions of mask has to be same size as image
blank = np.zeros(img.shape[:2], dtype='uint8')
cv.imshow('Blank', blank)

circle = cv.circle(blank.copy(), (img.shape[1]//2 + 25, img.shape[0]//2), 100, 255, -1)
rectangle = cv.rectangle(blank.copy(), (30,30), (370,370), 255, -1)

# can combine shapes etc to make a mask
mask = cv.bitwise_and(circle,rectangle)
cv.imshow('mask', mask)

masked = cv.bitwise_and(img,img,mask=mask)
cv.imshow('Masked', masked)

cv.waitKey(0)