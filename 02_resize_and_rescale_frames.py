# RESIZE AND RESCALE FRAMES
# - resize and rescale to reduce computational strain
# - get rid of some pixel information basically
# rescale -> scaling width and height by some value

import cv2 as cv

def rescaleFrame(frame, scale=0.75):
    '''
    Works for images, videos and live videos
    '''
    width = frame.shape[1] * scale # shape[1] is width of image
    height = frame.shape[0] * scale # shape[0] is height
    dimensions = (int(width), int(height)) # make a tuple with width and height
    # https://stackoverflow.com/questions/67851320/cant-parse-center-sequence-item-with-index-0-has-a-wrong-type
    # need to cast to int

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

def changeResolution(width, height):
    '''
    Does same as rescaleFrame function, but only works on live videos (webcam)
    '''
    capture.set(3,width) # 3 is width
    capture.set(4,height) # 4 is height

# Read image
img = cv.imread('Photos/cat.jpg')
img_resized = rescaleFrame(img)
cv.imshow('Cat', img)
cv.imshow('Cat resized', img_resized)

cv.waitKey(0)
cv.destroyAllWindows()

# Read video
capture = cv.VideoCapture('Videos/dog.mp4')
while True:
    isTrue, frame = capture.read()
    frame_resized = rescaleFrame(frame, 0.25)
    cv.imshow('Video', frame)
    cv.imshow('Video Resized', frame_resized)
    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()
