import cv2 
import cvzone
 
# Capturing the Video Stream 
video_capture = cv2.VideoCapture(0) 

#stikers

# Creating the cascade objects 
faces_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml") 
eyes_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_eye_tree_eyeglasses.xml")
lip_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_smile.xml") 
 
#def
def set_stiker_on_image(face,image):
    neutralface = cv2.imread('picture/neutralface.png')
    for (x, y, width, height) in face: 
            resize_neutralface = cv2.resize(neutralface,(width,height))         
            image[y:y+height ,x:x+width] = resize_neutralface
            return image

operation = 0

while True: 
    # Get individual frame 
    _, frame = video_capture.read() 
    # Covert the frame to grayscale 
    grayscale_image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) 
     
    # Detect all the faces in that frame 
    detected_faces = faces_cascade.detectMultiScale(image=grayscale_image, scaleFactor=1.3, minNeighbors=4) 
    # Detect eyes on the faces in that frame 
    detected_eyes = eyes_cascade.detectMultiScale(image=grayscale_image, scaleFactor=1.3, minNeighbors=4)
    # Detect lip on the faces in that frame 
    detected_lip = lip_cascade.detectMultiScale(image=grayscale_image, scaleFactor=1.5, minNeighbors=25) 
    

    # Get the user key to perform the operation
    click = cv2.waitKey(1)
    
    if click == 49 or operation == 49:
        operation = 49
        neutralface = cv2.imread('picture/neutralface.png')
        
        for (x, y, width, height) in detected_faces:
            resize_neutralface = cv2.resize(neutralface,(width,height))
            frame[y:y+height, x:x+width] = resize_neutralface
        
        click = cv2.waitKey(2)
        if click == 27:
            operation = 0

    elif click == 50 or operation ==50:
        operation = 50
        eye = cv2.imread('picture/eye.png')
        lip = cv2.imread('picture/lip.png')

        for (x, y, width, height) in detected_eyes:
            resize_eye = cv2.resize(eye, (width,height))
            frame[y:y+height, x:x+width] = resize_eye
        for (x, y, width, height) in detected_lip:
            resize_lip = cv2.resize(lip, (width,height))
            frame[y:y+height, x:x+width] = resize_lip
        
        click = cv2.waitKey(2)
        if click == 27:
            operation = 0

    elif click == 51 or operation ==51:
        operation = 51

        for (x, y, width, height) in detected_faces:
            face = cv2.blur(frame[y:y+height, x:x+width],(20,20))
            frame[y:y+height, x:x+width] = face
        
        click = cv2.waitKey(2)
        if click == 27:
            operation = 0

    elif click == 52 or operation ==52:
        operation = 52

        for (x, y, width, height) in detected_faces:
            face = cv2.rotate(frame[y:y+height, x:x+width],cv2.ROTATE_90_CLOCKWISE)
            frame[y:y+height, x:x+width] = face
        
        click = cv2.waitKey(2)
        if click == 27:
            operation = 0
    # Display the updated frame as a video stream 
    
    
    cv2.imshow('Webcam Face Detection', frame) 
 
    # Press the ESC key to exit the loop 
    # 27 is the code for the ESC key 
    if cv2.waitKey(1) == 27: 
        break 
 
# Releasing the webcam resource 
video_capture.release() 
 
# Destroy the window that was showing the video stream 
cv2.destroyAllWindows()