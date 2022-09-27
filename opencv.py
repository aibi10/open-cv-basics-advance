import cv2 as cv

"""Reading images start here"""

img = cv.imread("Photos/cat.jpg")
cv.imshow("cat", img)
cv.waitKey(0)
img1 = cv.imread("Photos/cat1.jpg")
cv.imshow("cat1", img1)
cv.waitKey(0)

"""Reading images end here"""

"""Reading videos"""

capture = cv.VideoCapture("Videos/dog.mp4")

while True:
    isTrue, frame = capture.read()
    cv.imshow("Video", frame)

    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyALlWindows()

def rescale(frame, scale = 0.75):
    height = int(frame.shape[0] * scale)
    width = int(frame.shape[1] * scale)
    dimensions = (height, wodth)
    
    return cv.resize(frame, dimensions, interpolation = cv.INTER_AREA)


cv.waitKey(0)