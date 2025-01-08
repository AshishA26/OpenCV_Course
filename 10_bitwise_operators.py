# BITWISE OPERATORS
# - and, or, xor, not
# - used in image processing and masks
# - a pixel is turned off it value of 0, on if 1

import cv2 as cv
import numpy as np

# Make blank, then rectangle and circle
blank = np.zeros((400,400), dtype='uint8')
rectangle = cv.rectangle(blank.copy(), (30,30), (370,370), 255, -1)
circle = cv.circle(blank.copy(), (200,200), 200, 255, -1)
cv.imshow('Rectangle', rectangle)
cv.imshow('Circle', circle)

# bitwise AND
# - places the 2 images ontop of each other and returns the "intersection"
#   (i.e. returns the common region)
bitwise_and = cv.bitwise_and(rectangle,circle)
cv.imshow('Bitwise AND', bitwise_and)

# bitwise OR
# - intersecting and non-intersecting regions
bitwise_or = cv.bitwise_or(rectangle,circle)
cv.imshow('Bitwise OR', bitwise_or)

# bitwise XOR
# - only non-intersecting regions
bitwise_xor = cv.bitwise_xor(rectangle,circle)
cv.imshow('Bitwise XOR', bitwise_xor)

# bitwise NOT
# - inverts the binary color
bitwise_not = cv.bitwise_not(rectangle)
cv.imshow('Bitwise NOT', bitwise_not)

cv.waitKey(0)