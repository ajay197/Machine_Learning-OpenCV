import cv2

imgpath = 'D:\\Docs\\Data Science\\Databases\\OpenCV_db\\misc\\lena_color_512.tif'
img = cv2.imread(imgpath,0)
#img = cv2.imread(imgpath, 1)  -- 1,0,-1 could be used for change in color

outpath = 'D:\\Docs\\Data Science\\Databases\\OpenCV_db\\misc\\lena.jpg'

cv2.imshow('Lena', img)
cv2.imwrite(outpath, img)   # to save image
cv2.waitKey(0)
cv2.destroyWindow('Lena')