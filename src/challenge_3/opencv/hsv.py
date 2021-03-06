import cv2
import numpy as np

class Hsv:
    def __init__(self):
        self.createHsvWindow()

    def empty(self, a):
        pass

    def createHsvWindow(self):
        cv2.namedWindow("HSV")
        cv2.resizeWindow("HSV", 640, 480)
        cv2.createTrackbar("Hue min", "HSV", 0, 179, self.empty)
        cv2.createTrackbar("Hue max", "HSV", 179, 179, self.empty)
        cv2.createTrackbar("Sat min", "HSV", 0, 255, self.empty)
        cv2.createTrackbar("Sat max", "HSV", 255, 255, self.empty)
        cv2.createTrackbar("Val min", "HSV", 0, 255, self.empty)
        cv2.createTrackbar("Val max", "HSV", 255, 255, self.empty)
        pass
    
    def getHsvHigherLower(self):
        h_min = cv2.getTrackbarPos("Hue min", "HSV")
        h_max = cv2.getTrackbarPos("Hue max", "HSV")
        s_min = cv2.getTrackbarPos("Sat min", "HSV")
        s_max = cv2.getTrackbarPos("Sat max", "HSV")
        v_min = cv2.getTrackbarPos("Val min", "HSV")
        v_max = cv2.getTrackbarPos("Val max", "HSV")
        lower = np.array([h_min, s_min, v_min])
        higher = np.array([h_max, s_max, v_max])
        return higher, lower

cap = cv2.VideoCapture(-1)
hsv = Hsv()

while True:
    success, img = cap.read()
    # img = cv2.imread("resources/car.jpg")
    img = cv2.resize(img, (640, 480))
    imgHsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    higher, lower = hsv.getHsv()
   
    mask = cv2.inRange(imgHsv, lower, higher)
    blended = cv2.bitwise_and(img, img, mask= mask)
    cv2.imshow("mask", mask)
    cv2.imshow("img", img)
    cv2.imshow("blended", blended)
    cv2.waitKey(1)
