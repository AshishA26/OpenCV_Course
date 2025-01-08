# COMPUTING HISTOGRAMS
# - allow you to visualize distribution of pixel intensity

import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

img = cv.imread('Photos/cats.jpg')
cv.imshow('Cats', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# Grayscale histogram

# - calcHist takes in lists of images, color channels, masks, histSizes (i.e. bin size), and ranges
gray_hist = cv.calcHist([gray], [0], None, [256], [0,256])

cv.waitKey(0)

plt.figure()
plt.title('Grayscale Histogram')
plt.xlabel('Bins')
plt.ylabel('# of pixels')
plt.plot(gray_hist)
plt.xlim([0,256])
plt.show()
# shows a peak of pixel values between 200 to 240, showing most of image is white

# we can also make histogram of a certain mask
blank = np.zeros(img.shape[:2], dtype='uint8')
mask = cv.circle(blank, (img.shape[1]//2, img.shape[0]//2), 100, 255, -1)
masked = cv.bitwise_and(gray,gray,mask=mask)
cv.imshow('masked', masked)
gray_hist = cv.calcHist([gray], [0], mask, [256], [0,256])

cv.waitKey(0)

plt.figure()
plt.title('Grayscale Histogram of mask')
plt.xlabel('Bins')
plt.ylabel('# of pixels')
plt.plot(gray_hist)
plt.xlim([0,256])
plt.show()



# Color histogram

plt.figure()
plt.title('Color Histogram')
plt.xlabel('Bins')
plt.ylabel('# of pixels')
# make a histogram for each color
colors = ('b', 'g', 'r')
for i, col in enumerate(colors):
    hist = cv.calcHist([img], [i], None, [256], [0,256])
    plt.plot(hist, color=col)
    plt.xlim([0,256])
plt.show()

# for a mask:

blank = np.zeros(img.shape[:2], dtype='uint8')
mask = cv.circle(blank, (img.shape[1]//2, img.shape[0]//2), 100, 255, -1)
masked = cv.bitwise_and(img,img,mask=mask)
cv.imshow('masked color', masked)

cv.waitKey(0)

plt.figure()
plt.title('Color Histogram with mask')
plt.xlabel('Bins')
plt.ylabel('# of pixels')
colors = ('b', 'g', 'r')
for i, col in enumerate(colors):
    hist = cv.calcHist([img], [i], mask, [256], [0,256])
    plt.plot(hist, color=col)
    plt.xlim([0,256])
plt.show()