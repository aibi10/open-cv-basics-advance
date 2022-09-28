import cv2 as cv
import numpy as np

img = cv.imread("Photos/cat.jpg")
cv.imshow("img", img)


# translation

def translate(img, x, y):
    trans_mat = np.float32([[1, 0, x], [0, 1, y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, trans_mat, dimensions)


translate = translate(img, 25, 30)
cv.imshow("translate", translate)


# rotation

def rotate(img, angle, rotPoint=None):
    (height, width) = img.shape[: 2]

    if rotPoint is None:
        rotPoint = (width//2, height//2)

    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = (width, height)

    return cv.warpAffine(img, rotMat, dimensions)


rotate = rotate(img, 45)
cv.imshow("rotate", rotate)


cv.waitKey(0)
