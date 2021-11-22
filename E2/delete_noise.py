import cv2
import numpy as np
imgs= [6]
for i in range(1,7):
    img = cv2.imread(f'Images/galaxy/g{i}.jpg',0)
    imgs.append(img)
    height, width = img.shape

result = np.zeros((height,width),dtype='uint8')
for img in imgs:
    result += img//6

cv2.imwrite('Images/galaxy/resualt.jpg', result)
cv2.waitKey()