import cv2
import numpy as np

def main():
    cap = cv2.VideoCapture(0)
    
    if cap.isOpened():
        ret, frame = cap.read()
    else:
        ret = False
        
    while ret:
        ret, frame = cap.read()
        
        #cvt clr BGR - HSV
        # HSV - Hue Saturation Value 
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) 
        
        #Blue clr range
        low = np.array([100, 50, 50])
        high = np.array([140, 255, 255])
        
        image_mask = cv2.inRange(hsv, low, high)
        
        output = cv2.bitwise_and(frame, frame, mask = image_mask)
        
        cv2.imshow('Image Mask', image_mask)
        cv2.imshow('Original Frame', frame)
        cv2.imshow('Color Tracking', output)
        if cv2.waitKey(1) == 27:
            break;
            
    cv2.destroyAllWindows()        
    cap.release()
        
        
        

if __name__ == '__main__':
    main()
