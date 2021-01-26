import cv2 as cv

# img = cv.imread('media/cat.jpg')

# cv.imshow('cat', img)

# # convert to grayscale

# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('gray', gray)

# # blur

# blur = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT)
# cv.imshow('blur', blur)

# edge cascade 

img2 = cv.imread('media/cat.jpg')
cv.imshow('city', img2)

canny = cv.Canny(img2, 125, 175)
# cv.imshow('canny', canny)

# dilating image

dilated = cv.dilate(canny, (3,3), iterations=3)
cv.imshow('dilated', dilated)

# eroding

eroded  = cv.erode(dilated, (3,3), iterations=3)
cv.imshow('eroded', eroded)

# resize

# resized = cv.resize(img2, (500,500), interpolation=cv.INTER_AREA)
# cv.imshow('resized', resized)

# cropping

# cropped = img2[100:200, 200:400]
# cv.imshow('cropped', cropped)

cv.waitKey(0)