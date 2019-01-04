import cv2
import numpy as np

def emptyFunction(self):
    pass
    
img1 = np.zeros((512, 512, 3), np.uint8)
win = 'Image Palette'
cv2.namedWindow(win)
    
cv2.createTrackbar('B', win, 0, 255, emptyFunction)
cv2.createTrackbar('G', win, 0, 255, emptyFunction)
cv2.createTrackbar('R', win, 0, 255, emptyFunction)
     
while(True):    

    cv2.imshow(win, img1)
    if cv2.waitKey(1) == 27:
        break
        
    blue = cv2.getTrackbarPos('B', win)
    green = cv2.getTrackbarPos('G', win)
    red = cv2.getTrackbarPos('R', win)
        
    img1[:] = [blue, green, red]
    print(blue, green, red)
        
cv2.destroyAllWindows()
