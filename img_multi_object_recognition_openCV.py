#Object detection in image using open CV
#We use a street view image where we detect where red traffic lights are located

import cv2
import numpy as np

#Opening main street view image containing target images
img = cv2.imread("street_traffic_signs.jpg")
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


##########################
#Creating the FIRST template to identify the first image of a red traffic light
template = cv2.imread("red_light.jpg", cv2.IMREAD_GRAYSCALE)
w, h = template.shape[::-1]

result = cv2.matchTemplate(gray_img, template, cv2.TM_CCOEFF_NORMED)
loc = np.where(result >= 0.8)

for pt in zip(*loc[::-1]):
    cv2.rectangle(img, pt, (pt[0] + w, pt[1] + h), (0, 255, 0), 4)


##########################
#Creating the SECOND template to identify the first image of a red traffic light
template2 = cv2.imread('red_light1.jpg', cv2.IMREAD_GRAYSCALE)
w2,h2 = template2.shape[::-1]

result2 = cv2.matchTemplate(gray_img, template2, cv2.TM_CCOEFF_NORMED)
loc2 = np.where(result2 >= 0.9)

for pt in zip(*loc2[::-1]):
    cv2.rectangle(img, pt, (pt[0] + w2,pt[1] + h2), (0,255,0),4)


cv2.imshow("img", img)

cv2.waitKey(0)
cv2.destroyAllWindows()


