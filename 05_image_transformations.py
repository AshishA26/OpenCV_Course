# IMAGE TRANSFORMATIONS

import cv2 as cv
import numpy as np

img = cv.imread('Photos/park.jpg')
cv.imshow('Boston', img)

# Translation
# - shift image along x and y axis
#   -x -> Left
#   -y -> up
#    x -> right
#    y -> down
def translate(img, x, y): 
    # x and y are amount you want to shift

    # need to create a "translation matrix"
    transMatrix = np.float32([[1,0,x],[0,1,y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMatrix, dimensions)

translated = translate(img, -100, 100)
cv.imshow('Translated', translated)


# Rotation
# - rotate by some angle (degrees) about a certain rotation point
# +ve angle is CCW, -ve is CW
def rotate(img, angle, rotPoint = None):

    # get height and width of image
    (height, width) = img.shape[:2]

    # if no rotation point specified, rotate about center of image
    if rotPoint is None:
        rotPoint = (width//2, height//2)

    rotMatrix = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = (width, height)
    return cv.warpAffine(img, rotMatrix, dimensions)

rotated = rotate(img, -45)
cv.imshow('Rotated', rotated)

# can rotate again, but will introduce the black areas from previous rotation
rotated_again = rotate(rotated, -45)
cv.imshow('Rotated again', rotated_again)

# Flip
#    0 -> flip vertically
#    1 -> horizontally
#   -1 ->both horz. and vert.
flip = cv.flip(img, 0)
cv.imshow('Flip', flip)

# Stuff talked about in 04_basic_functions.py:

# Resize
# - can resize, even to different aspect ratios
# - use cv.INTER_AREA for shrinking image
# - use cv.INTER_LINEAR or CUBIC for enlarging image
resized = cv.resize(img, (500,500), interpolation=cv.INTER_AREA)
cv.imshow('Resized', resized)

# Cropping
# - images are arrays, can use array slicing
# - select portion of image based on pixel values
cropped = img[50:200, 200:400]
cv.imshow('Cropped', cropped)

cv.waitKey(0)