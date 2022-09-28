# converting an image to grayscale

import cv2 as cv

img = cv.imread("Photos/cat.jpg")
cv.imshow("cat", img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("gray cat", gray)

# blurring an image

blur = cv.GaussianBlur(img, (9, 9), cv.BORDER_DEFAULT)
cv.imshow("blur", blur)

# edge cascader

canny = cv.Canny(img, 125, 175)
cv.imshow("canny", canny)

# dilating the images

dilate = cv.dilate(canny, (3, 3), iterations=7)
cv.imshow("dilation", dilate)

resize = cv.resize(img, (100, 100))
cv.imshow("resized", resize)

cropped = img[10: 100, 30: 90]
cv.imshow("cropped", cropped)

cv.waitKey(0)
