import cv2
import numpy as np

picture = np.zeros((240,320), dtype=np.uint8)

for i in range(1,15):
    pic = cv2.imread(f'Pictures/highway/h{i}.jpg', 0)
    picture += pic//14

cv2.imwrite('Final Pictures/highway.jpg', picture)
