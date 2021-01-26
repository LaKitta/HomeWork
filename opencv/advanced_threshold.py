import cv2 as cv

img = cv.imread('media/cat.jpg')

# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('cat', gray)

# # Simple Thresholding
# threshold, thresh = cv.threshold(gray, 150, 255, cv.THRESH_BINARY)

# cv.imshow('thresh', thresh)

# adaptive thresholding
adaptive_thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 1)

cv.imshow('adp_thresh', adaptive_thresh)

cv.waitKey(0)