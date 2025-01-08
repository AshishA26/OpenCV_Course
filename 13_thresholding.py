# THRESHOLDING
# - binarizing an image
# - convert an image, to a binary (black and white) image
# - ex: compare each pixel to a threshold value. 
#   If pixel less than threshold, set to 0. If more, set to 1

import cv2 as cv

img = cv.imread('Photos/cats.jpg')
cv.imshow('Cats', img)
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# Simple Thresholding
# - threshold takes in threshold value, max value, a threshold type
#   (BINARY in this case for binarizing)
# - "binarizes" the image -> i.e. if the intensity of a
#   pixel in the image is below 150, it will be set to 0 (black). If pixel is 
#   above 125, it is set to 1 (white).
# - higher threshold value makes image more white
threshold, thresh = cv.threshold(gray, 150, 255, cv.THRESH_BINARY)
cv.imshow('Simple thresholded', thresh)
# can also do the inverse (black <-> white):
threshold, thresh_inv = cv.threshold(gray, 150, 255, cv.THRESH_BINARY_INV)
cv.imshow('Simple thresholded inverse', thresh_inv)

# Adaptive Thresholding
# - can let the computer find the optimal threshold value itself
# - finds optimal values, then "slides" the kernel
# - takes:
#         adaptiveMethod: method to use for adaptive threshold
#               ADAPTIVE_THRESH_MEAN_C     -> computes a mean of the neighborhood pixels to get optimal value
#               ADAPTIVE_THRESH_GAUSSIAN_C -> weighted mean
#         thresholdType,
#         blockSize: neighborhood/kernal size
#         C: an int subtracted from mean, used for fine tuning
adaptive_thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY_INV, 11, 9)
cv.imshow('Adaptive thresh', adaptive_thresh)

cv.waitKey(0)