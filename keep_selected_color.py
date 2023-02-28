#importing the necessary libraries
import cv2 
import numpy as np

#capturing the camera
capture = cv2.VideoCapture(0)

# setting the default color range 
lower = np.array([0, 0, 0])
upper = np.array([10, 255, 255])

#running an infinite loop
while True:
    
    #reading from the camera
    _, frame = capture.read()
    
    #converting the image to hsv
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    #setting the mask
    mask = cv2.inRange(hsv, lower, upper)
    
    #showing the masked image
    cv2.imshow('image', mask)
    
    #setting a trackbar to adjust the color range
    cv2.createTrackbar('low_h', 'image', 0, 180, lambda v: None)
    cv2.createTrackbar('low_s', 'image', 0, 255, lambda v: None)
    cv2.createTrackbar('low_v', 'image', 0, 255, lambda v: None)
    
    cv2.createTrackbar('high_h', 'image', 0, 180, lambda v: None)
    cv2.createTrackbar('high_s', 'image', 0, 255, lambda v: None)
    cv2.createTrackbar('high_v', 'image', 0, 255, lambda v: None)
    
    #assigning values to the lower and upper range from the trackbar
    low_h = cv2.getTrackbarPos('low_h', 'image')
    low_s = cv2.getTrackbarPos('low_s', 'image')
    low_v = cv2.getTrackbarPos('low_v', 'image')
    
    high_h = cv2.getTrackbarPos('high_h', 'image')
    high_s = cv2.getTrackbarPos('high_s', 'image')
    high_v = cv2.getTrackbarPos('high_v', 'image')
    
    #assigning the values to the lower and upper arrays
    lower = np.array([low_h, low_s, low_v])
    upper = np.array([high_h, high_s, high_v])
    
    #breaking the loop on pressing escape
    if cv2.waitKey(1) == 27:
        break

#releasing the capture
capture.release()

#destroying all windows
cv2.destroyAllWindows()
