import cv2
import numpy as numPy


me = cv2.resize(cv2.imread('Pictures/Amirmohammad.jpg',0), (500,500))
monaliza = cv2.resize(cv2.imread('Pictures/Mona_Lisa.jpg',0),(500,500))



cmbpic1 = me//2 + monaliza//4
cmbpic2 = me//8 + monaliza//2


final_pic = numPy.concatenate((me,cmbpic1,cmbpic2,monaliza),axis=1)

cv2.imwrite('Final Pictures/me&monaliza.jpg',final_pic)
