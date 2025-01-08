# SMOOTHING AND BLURRING
# - smooth image when it has a lot of noise (from problems in lighting, etc)

# what happens when you apply blur:
# - you first define a kernel
# - this kernel is a window (3x3 window for example)
# - when you apply blur, it is applied to the middle
#   pixel as a result of the pixels around it
# - this window then slides right, and then down, 
#   and computes for all the pixels in the image
# - higher kernel size = more blur

import cv2 as cv

img = cv.imread('Photos/cats.jpg')
cv.imshow('Cats', img)

# Averaging Blur
# - compute pixel intensity of middle pixel 
#   as a average of surrounding pixels
average = cv.blur(img, (7,7))
cv.imshow('Average blur',average)

# Gaussian Blur
# - similiar to averaging, but
#   surrounding pixel is given a weight
# - use these weights to average
# - more natural than averaging
# - note: sigmaX = std deviation in x direction
gauss = cv.GaussianBlur(img, (7,7), 0)
cv.imshow('Gauss blur', gauss)

# Median Blur
# - same as averaging, but find median instead
median = cv.medianBlur(img, 7) # cv assumes 7 means 7x7 kernel
cv.imshow('Median Blur', median)

# Bilateral Blur
# - most effective
# - applies blurring but retains edges in the image 
#   (other blurs dont care about what happens to edges)
# - takes in diameter (instead of kernel), 
#   sigmaColor (larger value = more colors in neighborhood considered),
#   sigmaSpace (larger value means pixels further away from central pixel are taken into consideration)
bilateral = cv.bilateralFilter(img, 10, 35, 25)
cv.imshow('Bilateral blur', bilateral)

cv.waitKey(0)