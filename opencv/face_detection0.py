import cv2 as cv

# face detection on a video

capture = cv.VideoCapture('media/fcb.mp4')

haar_cascade = cv.CascadeClassifier('haarcascade_frontface.xml')

while True:
    isTrue, frame = capture.read()
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    face_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3)

    for (x,y,w,h) in face_rect:
        cv.rectangle(frame, (x,y), (x+w, y+h), (0,255,0), thickness=3)

    cv.imshow('video', frame)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()