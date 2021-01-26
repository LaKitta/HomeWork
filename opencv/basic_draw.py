import cv2 as cv
import numpy as np

blank = np.zeros((500,500,3), dtype='uint8')

cv.imshow('blank', blank)

# # paint the image with a color 

# blank[:] = 0,0,255
# cv.imshow('colered', blank)

# blank[100:300] = 0,0,0
# cv.imshow('colered2', blank)

# draw a rectangle, circle, line

# cv.rectangle(blank, (0,0), (blank.shape[1]//2,blank.shape[0]//2), (0,255,255), thickness=-1)
# cv.imshow('rectangle', blank)

cv.circle(blank, (blank.shape[1]//2,blank.shape[0]//2), 50, (255,255,255), 5)
cv.imshow('cirle', blank)

cv.line(blank, (0,0), (blank.shape[1]//2,blank.shape[0]//2), (255,255,255), 5)
cv.imshow('line', blank)

# write text

cv.putText(blank, 'Hello', (250,250), cv.FONT_HERSHEY_TRIPLEX, 1.0, (255,255,255), 2)
cv.imshow('test', blank)

cv.waitKey(0)