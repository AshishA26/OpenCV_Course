# MERGE AND SPLIT COLOR CHANNELS

import cv2 as cv
import numpy as np

img = cv.imread('Photos/park.jpg')
cv.imshow('Boston', img)

# Splitting
b,g,r = cv.split(img)

# display the images and print their dimensions
cv.imshow('Blue',b)
cv.imshow('Green',g)
cv.imshow('Red',r)
print(img.shape) # a tuple of (x, y, # of color channels)
print(b.shape) # a tuple of (x,y)...no third item as shape of component is 1 (i.e. 1 color channel -> grayscale)
print(g.shape)
print(r.shape)
# - displayed as grayscale images that show distrubution of pixel intensity.
# - lighter regions show higher concentration of color


# Merging
merged = cv.merge([b,g,r])
cv.imshow('Merged', merged)


# We can make the specific channels shown in their specific color:

# make a blank image - holds the dimensions of the image basically
blank = np.zeros(img.shape[:2], dtype='uint8')

# make it a 3 color channel image for each color, where
# the unused colors are set to black (blank)
blue = cv.merge([b,blank,blank])
green = cv.merge([blank,g,blank])
red = cv.merge([blank,blank,r])
cv.imshow('Blue with color',blue)
cv.imshow('Green with color',green)
cv.imshow('Red with color',red)

cv.waitKey(0)