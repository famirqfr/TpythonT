import cv2

wolf = cv2.imread('images/4.jpg',0)
height, width = wolf.shape

for i in range(height):
    for j in range(width):
        if wolf[i,j] < 180:
            wolf[i,j]=0

cv2.imwrite('images/result/wolfdetected.jpg',wolf)
cv2.waitKey()