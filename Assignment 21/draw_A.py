import cv2
import numpy as np

img = np.zeros((500,500))
img[::] = 170
cv2.line(img, pt1=(250,100), pt2=(160,350), color=(0,0,255), thickness=20)
cv2.line(img, pt1=(250,100), pt2=(340,350), color=(0,0,255), thickness=20)
cv2.line(img, pt1=(195,275), pt2=(310,275), color=(0,0,255), thickness=20)

cv2.imwrite('images/result/amirmohammad.jpg',img)
cv2.waitKey()