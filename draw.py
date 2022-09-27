import cv2 as cv
import numpy as np

cat = cv.imread("Photos/cat.jpg")
cv.imshow("cat", cat)

cv.waitKey(0)