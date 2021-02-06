import cv2
import numpy as np

kernel = np.ones((5,5), np.uint8)
# cap = cv2.VideoCapture("resources/road.mp4");
cap = cv2.VideoCapture(-1)
cap.set(3, 640)
cap.set(4, 480)
cap.set(10, 100)

while True:
    success, img = cap.read()
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # img = cv2.GaussianBlur(img, (15, 15), 0)
    img = cv2.Canny(img, 150, 200)
    img = cv2.dilate(img, kernel, iterations= 1)

    cv2.imshow("video", img)
    if (cv2.waitKey(1) & 0xFF == ord('q')):
        break
    