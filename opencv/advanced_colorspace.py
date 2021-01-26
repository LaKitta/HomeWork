import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('media/cat.jpg')
cv.imshow('CAT', img)

# BGR 2 RGB
# bgr2rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)

# BGR img

# plt.imshow(bgr2rgb)
# plt.show()

# cv.imshow('bgr2rgb', bgr2rgb)

# BGR To Grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)

# Grayscale to BGR

gray2bgr = cv.cvtColor(gray, cv.COLOR_GRAY2BGR)
cv.imshow('gray2bgr', gray2bgr)

# # BGR to HSV
# hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
# cv.imshow('hsv', hsv)

# ## BGR to l*a*b
# lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
# cv.imshow('lab', lab)

cv.waitKey(0)
