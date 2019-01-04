import cv2
import numpy as np
import time

def emptyFunction():
    pass

def main():
    
    impath = 'D:\\Docs\\Data Science\\Databases\\OpenCV_db\\misc\\'
    imgpath1 = impath + 'lena_color_512.tif'
    imgpath2 = impath + 'woman_blonde.tif'
    
    img2 = cv2.imread(imgpath1, 1)
    img1 = cv2.imread(imgpath2, 1)
    
    win = 'Blending Slider'
    cv2.namedWindow(win)
    
    output = cv2.addWeighted(img1, 0.5, img2, 0.5, 0)
    
    cv2.createTrackbar('Alpha', win, 0, 100, emptyFunction)
    
    while True:
        cv2.imshow(win, output)
        
        if cv2.waitKey(1) == 27:
            break
        
        alpha = cv2.getTrackbarPos('Alpha', win)/100
        beta = 1 - alpha
        
        output = cv2.addWeighted(img1, alpha, img2, beta, 0)
        
        
    cv2.destroyAllWindows()
    
    
    
    
    
if __name__ == '__main__':
    main()