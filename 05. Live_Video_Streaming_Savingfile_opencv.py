import cv2
import matplotlib.pyplot as plt

def main():
    win1 = 'Live Video Capture'
    win2 = 'Gray Frame'
    cv2.namedWindow(win1)
    #cv2.namedWindow(win2)
    
    cap = cv2.VideoCapture(0)
    
    # ------ Fetch resolution
    print('Width : ' + str(cap.get(3)))
    print('Height : ' + str(cap.get(4)))
    
    # ------ Set resolution
    #cap.set(3, 1024)  
    #cap.set(4, 768)
    
    #print('Width : ' + str(cap.get(3)))
    #print('Height : ' + str(cap.get(4)))
    
#---------------- save file----------------
    
    filename = 'D:\\Docs\\Data Science\\Databases\\OpenCV_db\\misc\\output.avi'
    codec = cv2.VideoWriter_fourcc('X', 'V', 'I', 'D') 
    # fourcc = Four Character Code - WMV2, WMV1, MJPG, DIVX, XVID, H264
    framerate = 30
    resolution = (640, 480)
    
    VideoFileOutput = cv2.VideoWriter(filename, codec, framerate, resolution)
    
#------------------------------------------------
    
    if cap.isOpened():
        ret, frame = cap.read()
    else:
        ret = False
        
    while ret:
        
        ret, frame = cap.read()
        
        #greyFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # convert frames to grey
        
        cv2.imshow(win1, frame)
        VideoFileOutput.write(frame)
        #cv2.imshow(win2, greyFrame)
        if cv2.waitKey(1) == 27:
            break
        
    cv2.destroyAllWindows()
    VideoFileOutput.release()
    cap.release()
    
if __name__ == "__main__":
    main()