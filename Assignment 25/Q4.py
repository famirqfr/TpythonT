from typing import ValuesView
import cv2
import numpy as np 

counter = 0

def convolution (image , c_fade, coutnt):
    filter   = np.ones((c_fade , c_fade)) / c_fade **2 
    output_image = np.ones(image.shape)
    rows , cols = image.shape
    for i in range(c_fade //2 ,rows-(c_fade //2)):
        for j in range(c_fade//2 ,cols-(c_fade // 2 )):
            small_img = image[i-(c_fade//2):i+1+(c_fade//2) ,j-(c_fade//2):j+1+(c_fade//2)]
            output_image[i ,j] = np.sum (small_img * filter)
    cv2.imwrite(f"Images/outputQ4-{coutnt}.jpg" , output_image)

image = cv2.imread("Images/garfild.jpg" , 0)
while True:
    counter += 1
    print('Enter Your Opertions\npress 1 to Apply Filter 3*3\tpress 2 to Apply Filter 5*5\npress 3 to Apply Filter 7*7\tpress 4 to Apply Filter 9*9')
    option = int(input() )
    if option==1:
        convolution(image, 3, counter)

    elif option==2:
        convolution(image, 5, counter)
        
    elif option==3:
        convolution(image, 7, counter)
        
    elif option==4:
        convolution(image, 15, counter)
    else:
        print('SORRY !!, This opertions is not defined\nplease try again')
        