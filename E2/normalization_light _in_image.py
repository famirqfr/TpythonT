import cv2

img1 = cv2.imread('Images/e.tif',0)
img2 = cv2.imread('Images/f.tif',0)

result = img1 / img2

cv2.imshow('t',result)
cv2.waitKey()

