import cv2 as cv

img = cv.imread('media/fff.jpg')

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

haar_cascade = cv.CascadeClassifier('haarcascade_frontface.xml')

face_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3)

# print(f'faces found = {len(face_rect)}')

for (x,y,w,h) in face_rect:
    cv.rectangle(img, (x,y), (x+w, y+h), (0,255,0), thickness=3)

cv.imshow('result', img)

cv.waitKey(0)
