import cv2
import matplotlib.pyplot as plt

path = 'D:\\Docs\\Data Science\\Databases\\OpenCV_db\\misc\\'
#imgpath = path + 'Disha-Patani.jpg'
#imgpath = path + '7.1.07.tiff'
imgpath = path + 'cameraman.tif'
img = cv2.imread(imgpath, 0) # set value = 0 when using OTSU Threshold

#img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

thresh = 0 # set thresh = 0 when using OTSU Threshold
maxval = 255

ret, o1 = cv2.threshold(img, thresh, maxval, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
ret, o2 = cv2.threshold(img, thresh, maxval, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
ret, o3 = cv2.threshold(img, thresh, maxval, cv2.THRESH_TOZERO + cv2.THRESH_OTSU)
ret, o4 = cv2.threshold(img, thresh, maxval, cv2.THRESH_TOZERO_INV + cv2.THRESH_OTSU)
ret, o5 = cv2.threshold(img, thresh, maxval, cv2.THRESH_TRUNC + cv2.THRESH_OTSU)

output = [img, o1, o2, o3, o4, o5]
titles = ['Original', 'Binary', 'Binary Inv', 'Zero', 'Zero Inv', 'Trunc']

for i in range(len(output)):
    plt.subplot(2, 3, i+1)
    plt.imshow(output[i], cmap = 'gray') # set cmap = 'gray' when using OTSU Threshold
    plt.title([titles[i]])
    plt.xticks([])
    plt.yticks([])
plt.show()


