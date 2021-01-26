import cv2 as cv
import numpy as np

img = cv.imread('media/arc.jpg')

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# laplacian
lap = cv.Laplacian(gray, cv.CV_64F)
lap = np.uint8(np.absolute(lap))

cv.imshow('lap', lap)

# sobel
sobelx = cv.Sobel(gray, cv.CV_64F, 1, 0)
sobely = cv.Sobel(gray, cv.CV_64F, 0, 1)
sobel_c = cv.bitwise_or(sobelx, sobely)

cv.imshow('sobel_c', sobel_c)

sobelxy = cv.Sobel(gray, cv.CV_64F, 1, 1)
cv.imshow('sobelxy', sobelxy)

# canny
canny = cv.Canny(gray, 150, 175)
cv.imshow('canny', canny)

cv.waitKey(0)      