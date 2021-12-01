import cv2
import numpy as np

image = cv2.imread('Images/flower_input.jpg')
image = cv2.cvtColor(image , cv2.COLOR_BGR2GRAY)
output_image = np.ones(image.shape)
rows, cols = image.shape
mask = np.ones((21,21)) / 1225



for i in range (10 , rows-10):
    for j in range(10 , cols-10):          
        part_of_img = image[i-10:i+11,j-10:j+11]
        output_image[i,j] = np.sum(part_of_img * mask)

for i in range(rows):
    for j in range(cols):
        if image[i,j] <= 200: 
            image[i,j] = output_image[i,j]
        
cv2.imshow('Portrait' , image)
cv2.imwrite('Images/Portrait.jpg' , image)
cv2.waitKey()
