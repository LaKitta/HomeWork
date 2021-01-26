import cv2 as cv

# If *windows run-time* erro shows, try `pip install numpy==1.19.0`

# **read image

# img = cv.imread('media/arc.jpg')
# cv.imshow('Image', img)
# cv.waitKey(0)

# **read video

# capture = cv.VideoCapture('media/video.mp4')

# while True:
#     isTrue, frame = capture.read()
#     cv.imshow('video', frame)

#     if cv.waitKey(20) & 0xFF==ord('d'):
#         break

# capture.release()
# cv.destroyAllWindows()

# **resize image

# img = cv.imread('media/arc.jpg')

# cv.imshow('orign', img)

# def rescaleFrame(frame, scale=0.75):
#     width = int(frame.shape[1]*scale) # shape[1] -> width
#     height = int(frame.shape[0]*scale) # shape[1] -> height

#     dimensions = (width, height)

#     return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

# capture = cv.VideoCapture('media/video.mp4')

# while True:
#     isTrue, frame = capture.read()

#     frame_resized = rescaleFrame(frame, 0.1)

#     cv.imshow('video', frame)
#     cv.imshow('Resized', frame_resized)

#     if cv.waitKey(20) & 0xFF==ord('d'):
#         break

# capture.release()
# cv.destroyAllWindows()

