# CONTOUR DETECTION
# - contours are basically boundaries of objects
# - contours are basically edges, but not the same mathematically
# - useful for object detection 

import cv2 as cv
import numpy as np

img = cv.imread('Photos/cats.jpg')
cv.imshow('Cats', img)

# convert to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# blur the image (will reduce number of contours)
blur = cv.GaussianBlur(gray, (5,5), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)

# get edges with canny
canny = cv.Canny(blur, 125, 175)
cv.imshow('Canny edges', canny)

# Get contours
# - findCounters() looks at the "structuring element" (edges) and returns 2 values:
#     contours -> a list of all coordinates of contours
#     hierarchies -> hierarchical representation of contours (circle inside square inside square, etc)
# - second parameter is "mode" that the function returns contours
#     RETR_LIST -> all contours
#     RETR_TREE -> all hierarchical contours
#     RETR_EXTERNAL -> only external (outside) contours
# - third param is contour approximation method
#     CHAIN_APPROX_NONE -> does nothing, just returns all of the contours
#     CHAIN_APPROX_SIMPLE -> compresses all contours into ones (the endpoints usually) that make the most sense
contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)

# can find number of contours:
print(f'{len(contours)} contour(s) found!')

# Can visualize contours found in image by drawing over the image:
# First make a blank image:
blank = np.zeros(img.shape, dtype='uint8')
cv.imshow('Blank', blank)
# Then draw the contours on the blank image
# - the -1 means draw all contours in the contours list
cv.drawContours(blank, contours, -1, (0,0,255), 1)
cv.imshow('Contours drawn', blank)



# Instead of blurring and canny edge detecting, we can try thresholding:

# Thresholding
# - "binarizes" the image -> i.e. if the intensity of a
#   pixel in the image is below 125, it will be set to 0 (black). If pixel is 
#   above 125, it is set to 1 (white).
# - also need to specifiy max value, and then thresholding type (BINARY in this
#   case for binarizing)
ret, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)
cv.imshow("Thresh", thresh)

# Now try contours and visualizing them
contoursWithThresh, hierarchiesWithThresh = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
print(f'{len(contoursWithThresh)} contour(s) found!')
blankWithThresh = np.zeros(img.shape, dtype='uint8')
cv.imshow('Blank with Thresh', blankWithThresh)
cv.drawContours(blankWithThresh, contoursWithThresh, -1, (0,0,255), 1)
cv.imshow('Contours drawn with thresh', blankWithThresh)

cv.waitKey(0)

# Recommended to try canny first, then thresholding