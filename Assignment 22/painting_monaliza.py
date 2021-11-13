import cv2

pic = cv2.imread('Pictures/Mona_Lisa.jpg', 0)

inverted = 255 - pic
blurred = cv2.GaussianBlur(inverted, (21, 21), 0)
inverted_blurred = 255 - blurred

painting = pic / inverted_blurred
painting = painting * 255

cv2.imwrite('Final Pictures/painting_monaliza.jpg', painting)