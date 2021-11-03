import cv2
import numpy as np


chess_board = np.zeros([800,800])
height,width=chess_board.shape
is_odd_row = False

for row in range(0,height,80):
    if is_odd_row:
        is_odd_row = False
        for cloum in range(80,width,160):
            chess_board[row:row+80,cloum:cloum+80] = 255
    
    else:
        is_odd_row = True
        for cloum in range(0,width,160):
            chess_board[row:row+80,cloum:cloum+80] = 255
        

         
cv2.imwrite('images/result/chessboard.jpg',chess_board)
cv2.waitKey()
        