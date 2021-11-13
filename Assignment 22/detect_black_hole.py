import cv2 as cv
import numpy as np

pictures = []

for i in range(1,5):
    for j in range(1,6):
        picture = cv.imread(f'Pictures/black hole/{i}/{j}.jpg',0)
        pictures.append(picture)
        
pic = np.zeros((1000, 1000), dtype =np.uint)
pic_without_noise_list = []
for i in range(0,5):
    pic += pictures[i]//5
    pic_without_noise_list.append(pic)
for i in range(5,10):
    pic += pictures[i]//5
    pic_without_noise_list.append(pic)

for i in range(10,15):
    pic += pictures[i]//5
    pic_without_noise_list.append(pic)

for i in range(15,20):
    pic += pictures[i]//5
    pic_without_noise_list.append(pic)


final_pic = cv.hconcat([pic_without_noise_list[0],pic_without_noise_list[1],pic_without_noise_list[2],pic_without_noise_list[3]])

cv.imwrite('Final Pictures/blackhole.jpg',final_pic)
cv.waitKey()