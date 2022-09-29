import cv2 as cv

# img = cv.imread("Photos/audience.jpg")
# cv.imshow("audience", img)

# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow("gray", gray)

haar_cascade = cv.CascadeClassifier("haar_cascade.xml")

capture = cv.VideoCapture("Videos/People.mp4")
while True:
    isTrue, frame = capture.read()

    faces_rect = haar_cascade.detectMultiScale(
        frame, scaleFactor=1.01, minNeighbors=1)

    frame = cv.resize(frame, (720, 480), interpolation=cv.INTER_AREA)

    cv.putText(frame, str(len(faces_rect)), (60, 20),
               cv.FONT_HERSHEY_PLAIN, 2, (0, 0, 255), 1)

    cv.imshow("Video", frame)

    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyALlWindows()


# faces_rect = haar_cascade.detectMultiScale(
#     gray, scaleFactor=1.01, minNeighbors=1)
# print(len(faces_rect))

# for (x, y, w, h) in faces_rect:
#     cv.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

# cv.imshow("audience", img)


cv.waitKey(0)
