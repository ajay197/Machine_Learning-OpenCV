import cv2
import numpy as np
import time


impath = 'D:\\Docs\\Data Science\\Databases\\OpenCV_db\\misc\\'
imgpath1 = impath + 'lena_color_512.tif'
imgpath2 = impath + '4.2.01.tiff'

img1 = cv2.imread(imgpath1)
img2 = cv2.imread(imgpath2)

#alpha = 0.5
#beta = 0.5
#gama = 0
output = cv2.addWeighted(im1, alpha, im2, beta, gama)

for i in np.linspace(0, 1, 100):
    alpha = i
    beta = 1 - alpha
    output = cv2.addWeighted(im1, alpha, im2, beta, 0)
    cv2.imshow('Transition', output)
    time.sleep(0.1)
    if cv2.waitKey(1) == 27:
        break
cv2.destroyAllWindows()

#titles = ['lena', 'droplet', 'weighted']
#images = [im1, im2, output]
#for i in range(len(images)):
#    plt.subplot(1, len(images), i+1)
#    plt.title(titles[i])
#    plt.imshow(images[i])
#    plt.xticks([])
#    plt.yticks([])
#plt.show()
    