import cv2

pic1 = cv2.imread('Pictures/a.tif')
pic2 = cv2.imread('Pictures/b.tif' )

fpic = pic2 - pic1 

cv2.imwrite('Final Pictures/decryption.jpg',fpic)