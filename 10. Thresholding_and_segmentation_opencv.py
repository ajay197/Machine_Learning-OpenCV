import cv2
import matplotlib.pyplot as plt

path = 'D:\\Docs\\Data Science\\Databases\\OpenCV_db\\misc\\'
#imgpath = path + 'Disha-Patani.jpg'
imgpath = path + '7.1.10.tiff'
img = cv2.imread(imgpath, 1)

#img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

thresh = 122
maxval = 255

ret, o1 = cv2.threshold(img, thresh, maxval, cv2.THRESH_BINARY)
ret, o2 = cv2.threshold(img, thresh, maxval, cv2.THRESH_BINARY_INV)
ret, o3 = cv2.threshold(img, thresh, maxval, cv2.THRESH_TOZERO)
ret, o4 = cv2.threshold(img, thresh, maxval, cv2.THRESH_TOZERO_INV)
ret, o5 = cv2.threshold(img, thresh, maxval, cv2.THRESH_TRUNC)

output = [img, o1, o2, o3, o4, o5]
titles = ['Original', 'Binary', 'Binary Inv', 'Zero', 'Zero Inv', 'Trunc']

for i in range(len(output)):
    plt.subplot(2, 3, i+1)
    plt.imshow(output[i])
    plt.title([titles[i]])
    plt.xticks([])
    plt.yticks([])
plt.show()


