import cv2

img1 = cv2.imread('Images/d1.jpg',0)
img2 = cv2.imread('Images/d2.jpg',0)

result = img1 - img2

cv2.imshow('t',result)
cv2.waitKey()

