import cv2

pic1 = cv2.imread('Pictures/board - origin.bmp',0)
pic2 = cv2.imread('Pictures/board - test.bmp',0)

rotate = cv2.flip(pic2,1)

fpic = cv2.subtract(pic1,rotate)


cv2.imwrite('Final Pictures/Problems_of_Board.jpg', fpic)