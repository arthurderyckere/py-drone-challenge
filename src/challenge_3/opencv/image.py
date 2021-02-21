import cv2

img = cv2.imread("resources/car.jpg")

img = cv2.resize(img, (640, 480))


# cropping by only showing part of the image vector
cv2.imshow("image", img[0:200, 200:400])

cv2.waitKey(0)