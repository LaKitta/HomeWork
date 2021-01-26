# https://docs.opencv.org/master/d4/dc6/tutorial_py_template_matching.html
# res = It returns a grayscale image, where each pixel denotes how much does the neighbourhood of that pixel match with template.

import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img_rgb = cv.imread('appgalary.png')
img_gray = cv.cvtColor(img_rgb, cv.COLOR_BGR2GRAY)

# img2 = cv.imread('main.png', 0)

# print(img2.shape[:3])
# print(img_gray.shape[:3])

# cv.imshow('cvt', img_gray)
# cv.imshow('0', img2)

template = cv.imread('template_phone.png',0)

w, h = template.shape[::-1]
res = cv.matchTemplate(img_gray,template,cv.TM_CCOEFF_NORMED)

# print(res)
# print(res.shape)

# Set threshold to 0.95 for app galary icons
threshold = 1

loc = np.where( res >= threshold)

if loc[0].size > 0:
    print('not empty')
else:
    print('empty')

# is_empty(loc[0])

# print(len(loc))
print(loc)

# print(loc[::1])
# print(loc[::-1])

# for pt in zip(*loc[::-1]):
#     print(pt)
#     cv.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,0,255), 1)

# cv.imshow('res.png',img_rgb)

# # cv.imshow('res', res)

# cv.waitKey(0)