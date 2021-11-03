import cv2

img = cv2.imread('images/3.jpg')
img = cv2.rotate(img, cv2.ROTATE_180)

cv2.imwrite('images/result/rotate.jpg',img)
cv2.waitKey()