import cv2

img1 = cv2.imread('Images/c.tif',0)
mask = cv2.imread('Images/d.tif',0)
mask = mask // 255

result = img1 * mask

cv2.imshow('t',result)
cv2.waitKey()

