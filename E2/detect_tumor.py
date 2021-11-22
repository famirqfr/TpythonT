import cv2

img1 = cv2.imread('Images/a.tif',0)
img2 = cv2.imread('Images/b.tif',0)

result = cv2.subtract(img1,img2)

cv2.imshow('t',result)
cv2.waitKey()

