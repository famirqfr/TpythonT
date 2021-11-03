
import cv2

img1 = cv2.imread('images/1.jpg',0)
img2 = cv2.imread('images/2.jpg',0)

result_img1 = 255 - img1
cv2.imwrite('images/result/female.jpg',result_img1)
result_img2 = 255 - img2
cv2.imwrite('images/result/male.jpg',result_img2)
