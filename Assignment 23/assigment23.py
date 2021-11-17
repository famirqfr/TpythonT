import cv2 
import cvzone

# Mask

tongue = cv2.imread("emoji/tongue.png",cv2.IMREAD_UNCHANGED)
eye = cv2.imread("emoji/eye.png",cv2.IMREAD_UNCHANGED)
lip = cv2.imread("emoji/lip.png",cv2.IMREAD_UNCHANGED)

# Creating the cascade objects 
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_alt.xml") 
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_eye_tree_eyeglasses.xml") 
mouth_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_smile.xml") 
 

def set_tongue():
    while True: 
        _, frame = video_capture.read() 
        grayscale_image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) 
        detected_faces = face_cascade.detectMultiScale(grayscale_image, 1.2,minNeighbors=10)     
        
        for (x, y, width, height) in detected_faces: 
            tongue_resize = cv2.resize(tongue , (width,height))
            frame = cvzone.overlayPNG(detected_faces, tongue_resize, [x,y])
        cv2.imshow('Webcam Face Detection', frame) 
         
        # Press the ESC key to exit the loop 
        # 27 is the code for the ESC key 
        if cv2.waitKey(1) == 27: 
            break 
     

# Capturing the Video Stream 
video_capture = cv2.VideoCapture(0) 
 

 
while True: 
    # Get individual frame 
    _, frame = video_capture.read() 
    # Covert the frame to grayscale 
    grayscale_image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) 
     
    input_key = cv2.waitKey(1) 
    if input_key == ord("1") : 
        set_tongue() 
 
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