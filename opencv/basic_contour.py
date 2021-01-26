import cv2 as cv
import numpy as np

img = cv.imread('media/cat.jpg')
cv.imshow('City', img)

# create a blank img to draw contours
blank = np.zeros(img.shape, dtype='uint8')

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)

# blur = cv.GaussianBlur(gray, (5,5), cv.BORDER_DEFAULT)

canny = cv.Canny(img, 125, 175)
cv.imshow('canny', canny)

# threshold
# ret, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)
# cv.imshow('thresh', thresh)

contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
print(f'{len(contours)} contours found')

drawing = cv.drawContours(blank, contours, -1, (0,0,255), 1)
cv.imshow('drawing', drawing)

cv.waitKey(0)