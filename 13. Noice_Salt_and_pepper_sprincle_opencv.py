import cv2
import matplotlib.pyplot as plt
import numpy as np
import random


    
path = 'D:\\Docs\\Data Science\\Databases\\OpenCV_db\\misc\\'
imgpath = path + 'lena_color_512.tif'
img = cv2.imread(imgpath)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
#output = img
rows, columns, channels = img.shape
output = np.zeros(img.shape, np.uint8)

p = 0.05

for row in range(rows):
    for col in range(columns):
        r = random.random()
        if r < p/2:
            output[row][col] = [0, 0, 0]
        elif r < p:
            output[row][col] = [255, 255, 255]
        else:
            output[row][col] = img[row][col]

plt.subplot(1,2,1)
plt.imshow(img)
plt.title('Original')
plt.xticks([])
plt.yticks([])
plt.subplot(1,2,2)
plt.imshow(output)
plt.title('Salt and Pepper Sprincle')
plt.xticks([])
plt.yticks([])
plt.show()
   
 