# EDGE DETECTION AND GRADIENTS
# - gradients and edges are basically the same in programming
# - we have done canny before. Here we will do something different

import cv2 as cv
import numpy as np

img = cv.imread('Photos/park.jpg')
cv.imshow('Boston', img)
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# Lapacian method
# - makes image look like a pencil shading and lightly smudged
# - computes gradient of grayscale image
# How it works:
# - transitioning black <-> white, is considered a postive and negative slope
# - images cannot have negative pixel values
# - so you find absolute values of image, then convert to image specific datatype (uint8)
lap = cv.Laplacian(gray, cv.CV_64F)
lap = np.uint8(np.absolute(lap))
cv.imshow('Laplacian', lap)

# Sobel method
# - compute gradients over x and y axis, then combine
sobelx = cv.Sobel(gray, cv.CV_64F, 1, 0)
sobely = cv.Sobel(gray, cv.CV_64F, 0, 1)
combined_sobel = cv.bitwise_or(sobelx,sobely)
cv.imshow('Sobel X', sobelx)
cv.imshow('Sobel Y', sobely)
cv.imshow('Combined Sobel', combined_sobel)

# Canny (just to compare with)
canny = cv.Canny(gray, 125, 175)
cv.imshow('Canny edges', canny)

cv.waitKey(0)