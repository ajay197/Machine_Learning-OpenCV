import cv2
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

impath = 'D:\\Docs\\Data Science\\Databases\\OpenCV_db\\misc\\'
imgpath1 = impath + 'lena_color_512.tif'
imgpath2 = impath + 'peppers_color.tif'

#img1 = mpimg.imread(img1)
#img2 = mpimg.imread(img2)

img1 = cv2.imread(imgpath1)
img2 = cv2.imread(imgpath2)

img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)

plt.subplot(1, 2, 1) # first position
# subplot is used to format the images in grid format
# subplot(no_of_rows, columns, position_of_image)
plt.imshow(img1)
plt.xticks([])
plt.yticks([])

plt.subplot(1, 2, 2) # second position
plt.imshow(img2)
plt.xticks([])
plt.yticks([])
plt.show()



# ----------Using for loop---------
titles = ['dishu', 'lena']
images = [img1, img2]
for i in range(2):
    plt.subplot(1, 2, i+1)
    plt.title(titles[i])
    plt.imshow(images[i])
    plt.xticks([])
    plt.yticks([])
plt.show()
    

# ---------------------------------