import numpy as np
import cv2

video_capture = cv2.VideoCapture(0)

while True:
    _,frame = video_capture.read()
    if _ == False:
        break
 
    frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    frame = cv2.equalizeHist(frame)
    area = frame[100:350,200:450]
    filter = np.ones((30,30),np.float32)/900
    output = cv2.filter2D(frame,-1,filter)
    output[100:350,200:450] = area
    cv2.rectangle(output,(200,101), (450,350), (0, 255, 255),6)
    color_detection = output[100:350,200:450]

    if  0 < np.average(color_detection) <= 85:
        cv2.putText(output, "Black", (25, 50), cv2.FONT_HERSHEY_COMPLEX_SMALL, 2, (0, 0, 0), 2) 
    elif 85 < np.average(color_detection) <= 170:
        cv2.putText(output, "Gray", (25, 50), cv2.FONT_HERSHEY_COMPLEX_SMALL, 2, (0, 0, 0), 2)
    else:
        cv2.putText(output, "White", (25, 50), cv2.FONT_HERSHEY_COMPLEX_SMALL, 2, (0, 0, 0), 2) 

    click = cv2.waitKey(1)
    if click == 27:
        break

    cv2.imshow('Camera',output)
       
