#Basic OPENCV image recognition
import cv2
import numpy as np
import matplotlib.pyplot as plt

#SIMPLE RECOGNITION OF A FACE IMAGE / WHERE IS THE FACE IN THIS IMAGE?
face_cascade = cv2.CascadeClassifier('D:\\Program files\\anaconda\\envs\\tensorflow\\Lib\\site-packages\\cv2\\data\\haarcascade_frontalface_default.xml')
img = cv2.imread('jm_test_pic.jpg')
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray_img, scaleFactor=1.05, minNeighbors=5)
for x, y, w, h in faces:
    img = cv2.rectangle(img, (x, y), (x+w, y+h), (0,255,0), 3)
resized = cv2.resize(img, (int(img.shape[1]/7), int(img.shape[0]/7)))
cv2.imshow('gray', resized)
cv2.waitKey(0)
cv2.destroyAllWindows()




#img = cv2.imread('f1car.jpg', cv2.IMREAD_GRAYSCALE)

#show image
# cv2.imshow('image', img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


#print graph on top of image
# plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
# plt.plot([700,500,300],[60, 200, 300], 'c', linewidth = 5)
# plt.show()


#save CV2 image
# cv2.imwrite('f1cargray.png',img)



