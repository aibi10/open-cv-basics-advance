import cv2 as cv
import numpy as np

# drawing a blank image
blank = np.zeros((200, 200, 3), dtype='uint8')
cv.imshow("blank", blank)

# blank[:] = 255, 0, 0
# cv.imshow("blue", blank)

# blank[10:20, 30:40] = 0, 0, 255
# cv.imshow("red block", blank)

# drawing a rectangle

cv.rectangle(blank, (10, 20), (50, 80), (0, 0, 255), thickness=cv.FILLED)
cv.imshow("blank with recatngle", blank)

cat = cv.imread("Photos/cat.jpg")
cv.imshow("cat", cat)

# draw a circle
cv.circle(blank, (50, 50), 10, (255, 30, 180), thickness=-1)
cv.imshow("circle", blank)

# write text on image

cv.putText(blank, "hello duniya", (60, 20),
           cv.FONT_HERSHEY_SIMPLEX, 0.5, (213, 192, 137), 2)
cv.imshow("text", blank)

cv.waitKey(0)
