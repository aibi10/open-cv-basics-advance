import cv2 as cv
def rescale(frame, scale = 0.75):
    height = int(frame.shape[0] * scale)
    width = int(frame.shape[1] * scale)
    dimensions = (width, height)
    
    return cv.resize(frame, dimensions, interpolation = cv.INTER_AREA)

capture = cv.VideoCapture("Videos/dog.mp4")

# while True:
#     isTrue, frame = capture.read()
#     frame = rescale(frame, 0.1)
#     cv.imshow("Video", frame)

#     if cv.waitKey(20) & 0xFF == ord('d'):
#         break

# capture.release()
# cv.destroyALlWindows()

img1 = cv.imread("Photos/cat1.jpg")
print(img1.shape)
img1 = rescale(img1, 0.5)
cv.imshow("cat1", img1)
print(img1.shape)
cv.waitKey(0)
cv.waitKey(0)

