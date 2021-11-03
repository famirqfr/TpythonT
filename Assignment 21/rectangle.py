import cv2
import numpy as np


rectangle = np.zeros((255,255),dtype=np.uint8)

color=255

for i in range(255):
    color -= 1
    for j in range(255):
        rectangle[i,j] = color
        
cv2.imwrite('images/result/rectangle.jpg', rectangle)
cv2.waitKey()