import cv2 as cv
import numpy as np

img = cv.imread('media/cat.jpg')

blank = np.zeros(img.shape[:2], dtype='uint8')

cirle = cv.circle(blank.copy(), (img.shape[1]//2, img.shape[0]//2), 100, 255, -1)
rectangle = cv.rectangle(blank.copy(), (0,0), (img.shape[1]//2, img.shape[0]), 255, -1)

cv.imshow('rectangle', rectangle)
cv.imshow('circle', cirle)

shape1 = cv.bitwise_and(cirle, rectangle)
cv.imshow('shape', shape1)

masked = cv.bitwise_and(img, img, mask=shape1)
cv.imshow('masked', masked)

cv.waitKey(0)