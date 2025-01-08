# COLOR SPACES
# - how to switch between color spaces
# - a color space is a system for representing an array of colors
# - such as RBG, HSV, etc

import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('Photos/park.jpg')
cv.imshow('Boston', img)

# Convert BGR to Grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# BGR to HSV
# - HSV is Hue, Saturation, Value
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('HSV', hsv)

# BGR to LAB (L*a*b)
# - LAB is Lightness, Red/Green Value, Blue/Yellow Value 
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow('LAB', lab)

# BGR to RGB
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow('RGB', rgb)

# - Can also do the reverse of most things
# - If you then want grayscale to hsv, you to convert to BGR first, then hsv.

# HSV to BGR
hsv_bgr = cv.cvtColor(hsv, cv.COLOR_HSV2BGR)
cv.imshow('HSV-->BGR', hsv_bgr)

# HSV to BGR
lab_bgr = cv.cvtColor(lab, cv.COLOR_LAB2BGR)
cv.imshow('LAB-->BGR', lab_bgr)

cv.waitKey(0)

# OpenCV uses BGR, as opposed to our usual RGB
# displaying this photo not with cv, then the image colors will look 'inverted'
plt.imshow(img)
plt.show()
# Instead, inverting image using cv, then displaying it makes it look proper:
plt.imshow(rgb)
plt.show()


