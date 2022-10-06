import cv2 as cv

# img = cv.imread("Photos/audience.jpg")
# cv.imshow("audience", img)

# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow("gray", gray)

haar_cascade = cv.CascadeClassifier("haar_cascade.xml")

capture = cv.VideoCapture("Videos/People2.mp4")
while True:
    isTrue, frame = capture.read()
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    #frame = cv.resize(frame, (720, 720), interpolation=cv.INTER_AREA)

    faces_rect = haar_cascade.detectMultiScale(
        gray, scaleFactor=1.1, minNeighbors=5)

    cv.putText(frame, str(len(faces_rect)), (100, 200),
               cv.FONT_HERSHEY_PLAIN, 2, (0, 0, 255), 2)

    for (x, y, w, h) in faces_rect:
        cv.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    cv.imshow("Video", frame)

    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows()


# faces_rect = haar_cascade.detectMultiScale(
#     gray, scaleFactor=1.01, minNeighbors=1)
# print(len(faces_rect))

# for (x, y, w, h) in faces_rect:
#     cv.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

# cv.imshow("audience", img)


cv.waitKey(0)
