import cv2 as cv
import numpy as np
import dlib

video = cv.VideoCapture("Videos/People2.mp4")
detector = dlib.get_frontal_face_detector()

while True:

    isTrue, frame = video.read()
    frame = cv.flip(frame, 1)
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    faces = detector(gray)

    num = 0

    for face in faces:
        x, y = face.left(), face.top()
        hi, wi = face.right(), face.bottom()

        cv.rectangle(frame, (x, y), (hi, wi), (0, 255, 0), 2)

        num += 1

        cv.putText(frame, 'face' + str(num), (x - 12, y - 12),
                   cv.FONT_HERSHEY_PLAIN, 2, (0, 0, 255), 2)

        cv.imshow("frame", frame)

        if cv.waitKey(20) & 0xFF == ord('d'):
            break

video.release()
cv.destroyAllWindows()
