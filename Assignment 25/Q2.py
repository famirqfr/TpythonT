import cv2
import numpy as np

image = cv2.imread('Images/lion.png')
img = cv2.cvtColor(image , cv2.COLOR_BGR2GRAY)
output_image = np.zeros(img.shape)
mask = np.array([[0 , -1 , 0],
                 [-1 , 4 , -1],
                 [0 , -1 , 0]])
rows, cols = img.shape


for i in range(1, rows-1):
    for j in range(1 , cols-1):
        part_of_img = img[i-1:i+2 , j-1:j+2]
        output_image[i,j] = np.sum(part_of_img * mask)

cv2.imwrite('Images/filterOnLoin.jpg' , output_image)