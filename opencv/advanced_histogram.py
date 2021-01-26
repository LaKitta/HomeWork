import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread('media/cat.jpg')

# # bgr2gray
# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('gray', gray)

# Mask
blank = np.zeros(img.shape[:2], dtype='uint8')
circle = cv.circle(blank, (img.shape[1]//2, img.shape[0]//2), 100, 255, -1)
cv.imshow('circle', circle)

# mask = cv.bitwise_and(gray, gray, mask=circle)
# cv.imshow('mask', mask)

# # Grayscale histogram 
# gray_hist = cv.calcHist([gray],[0],mask,[256],[0,256])

plt.figure()
plt.title('Color Histogram')
plt.xlabel('bins')
plt.ylabel('# of lables')
# plt.plot(gray_hist)
# plt.xlim([0,256])
# plt.show()

# color histogram
colors = ('b', 'g', 'r')
for i,col in enumerate(colors):
    hist = cv.calcHist([img], [i], circle, [256], [0,256])
    plt.plot(hist, color=col)
    plt.xlim([0,256])

plt.show()

cv.waitKey(0)