import cv2
import matplotlib.pyplot as plt

def main():
    
    win = 'Live Streaming'
    cv2.namedWindow(win)
    
    cap = cv2.VideoCapture(0)
    
    if cap.isOpened():
        ret, frame = cap.read()
    else:
        ret = False
        
    while ret:
        ret, frame = cap.read()
        cv2.imshow(win, frame)
        if cv2.waitKey(1) == 27:
            break
        
    cv2.destroyAllWindows()
    cap.release()
    
    
if __name__ == '__main__':
    main()