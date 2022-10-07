import cv2 as cv

cap = cv.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 640)
cap.set(10, 60)

while True:
    success, img = cap.read()
    cv.imshow("video from webcam", img)

    if cv.waitKey(1) & 0xFF == ord('q'):
        break
