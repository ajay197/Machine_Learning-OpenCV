import cv2
import numpy as np

img = np.zeros((512,512,3), np.uint8)
#---------------shape------data type = unsighned int of 8 bits

cv2.line(img, (0, 99), (99, 0), (255, 0, 0), 2)
#----------start point, end point, color, thickness

cv2.rectangle(img, (50, 50), (150, 150), (0, 255, 0), 2)

cv2.circle(img, (100, 100), 50, (0, 0, 255), 2)
#---------------- center, radius, clr,    thickness 

cv2.circle(img, (220, 100), 50, (0, 0, 225), -1)
#--------------- center, radius, clr, -1 will fill the circle

cv2.ellipse(img, (400, 100), (100, 50), 0, 0, 360, (127, 127, 127), -1 )
#cv2.ellipse()

cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyWindow('Image')