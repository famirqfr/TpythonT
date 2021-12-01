import cv2
import numpy as np

img = cv2.imread('Images/building.tif')
img = cv2.cvtColor(img , cv2.COLOR_BGR2GRAY)
output_filter1_image = np.ones(img.shape)
output_filter2_image = np.ones(img.shape)
rows, cols = img.shape
filter1 = np.array([[-1 , 0 , 1],
                    [-1 , 0 , 1],
                    [-1 , 0 , 1]])

filter2 = np.array([[-1 , -1 , -1],
                    [0 , 0 , 0],
                    [1 , 1 , 1]])



for i in range(1, rows-1):
    for j in range(1 , cols-1):
        part_of_img = img[i-1:i+2 , j-1:j+2]
        output_filter1_image[i,j] = np.sum(part_of_img * filter1)
        output_filter2_image[i,j] = np.sum(part_of_img * filter2)

cv2.imwrite('Images/filter1Onbuilding.jpg' , output_filter1_image)
cv2.imwrite('Images/filter2Onbuilding.jpg' , output_filter2_image)