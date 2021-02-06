import cv2
import numpy as np

# in gimp select colors > components > decompose
# change the values of saturation, hue, value with colors > threshold
lower = np.array([0, 100, 100])
upper = np.array([100, 255, 240])

img = cv2.imread("resources/car.jpg")
img = cv2.resize(img, (640, 480))

imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)


mask = cv2.inRange(imgHSV, lower, upper)

img = cv2.bitwise_and(img, img, mask= mask)

cv2.imshow("image", img)

cv2.waitKey(0)