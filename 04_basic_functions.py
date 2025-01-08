# BASIC ESSENTIAL FUNCTIONS

import cv2 as cv

img = cv.imread('Photos/park.jpg')
cv.imshow('Boston', img)

# Converting to Grayscale
# - only see intensity distribution of pixels rather than color itself
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# Blur an image
# - removes noise in image (noise maybe due to bad lighting, etc)
# - Gaussian Blur takes in source image, kernal size (has to be an odd number),
#   and sigmaX. It can take in more though.
# - Increase kernal size to increase blur
blur = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)

# Edge Cascade
# - Find edges present in an image
# - Canny edge is common.
# - Can either just edge detect on image...
#   or edge detect on blurred image to get less edges
# - more blur = less edges
canny = cv.Canny(img, 125, 175)
cv.imshow('Canny', canny)
cannyAfterBlur = cv.Canny(blur, 125, 175)
cv.imshow('Canny after blur', cannyAfterBlur)

# Dilating the image
# - often use the canny image as "structuring element"
# - makes edges thicker
dilated = cv.dilate(cannyAfterBlur, (7,7), iterations=3)
cv.imshow('Dilated', dilated)

# Eroding
# - attempting (will not be perfect) to undo what dilating did
eroded = cv.erode(dilated, (7,7), iterations=3)
cv.imshow('Eroded', eroded)

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


# https://www.projectpro.io/recipes/what-is-dilation-of-image-dilate-image-opencv

# Dilation is a morphological transformation
# operator used to increase the size or thickness
# of the foreground object in an image. In most
# cases, Dilation is used to connect two broken
# objects of an image. To dilate an image, we
# define a kernel matrix which is made of ones
# and slide the kernel through the image. A kernel
# is nothing but a small matrix used for sharpening,
# blurring, embossing, edge detection, and much more.
# It is also sometimes called a convolution matrix,
# a mask, or a filter. Each pixel element is assigned
# a one if any of the pixels under the kernel neighborhood
# is 1. This increases the size of the white region in
# the image, which in turn increases the size of the
# foreground object in an image. Dilation is usually
# performed after the image is eroded using another
# morphological transformation operator called Erosion.
# This process helps in removing the white noise from the image.

#     src: The image which is to be dilated
#     kernel: The kernel matrix
#     iterations : (Optional) The number of iterations that
#                  specify how many times the operation will
#                  be performed. The default value is 1