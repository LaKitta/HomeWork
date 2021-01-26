import cv2 as cv

img = cv.imread('media/city.jpg')
cv.imshow('cat',img)

# averaging --> average intense of surrounding pixels
average = cv.blur(img, (3,3))
cv.imshow('average', average)

# gaussian blur --> weight each surronding pixels
gaussian = cv.GaussianBlur(img, (3,3), 0)
cv.imshow('gaussian', gaussian)

# median --> median intense of surrounding pixels --> reduce certain amount of noise
median = cv.medianBlur(img, 3)
cv.imshow('median', median)

# bilateral --> retain edge
bilateral = cv.bilateralFilter(img, 3, 15, 15)
cv.imshow('bilateral', bilateral)

cv.waitKey(0)