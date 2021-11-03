import cv2

img = cv2.imread('images/hj.jpg',0)


cv2.line(img, pt1=(150,0), pt2=(0,150), color=(0,0,255), thickness=20)


cv2.imwrite('images/result/hajhasanjamali.jpg', img)
cv2.waitKey()