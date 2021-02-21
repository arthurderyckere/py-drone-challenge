import cv2
import numpy as np

cap = cv2.VideoCapture(-1)
# orange hsv value
lower = np.array([0, 116, 123])
upper = np.array([37, 255, 255])

def findContours(mask):
    contours, hierachy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    return contours

def drawContours(imgContours, contours):
    for contour in contours:
        cv2.drawContours(imgContours, contour, -1, (255, 0, 255), 3)
    return imgContours

def getBoundingbox(contours):
    x, y, w, h = 0, 0, 0, 0
    for contour in contours:
        perimeter = cv2.arcLength(contour, True)
        approximate = cv2.approxPolyDP(contour, 0.02 * perimeter, True)
        x, y, w, h = cv2.boundingRect(approximate)

    return x + w//2, y


def addPoints(img, points):
    for point in points:
        cv2.circle(img, (point[0], point[1]), 10, (255, 123, 0), cv2.FILLED)


points = []
while True:
    success, img = cap.read()
    img = cv2.resize(img, (640, 480))
    imgHsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(imgHsv, lower, upper)
    imgBlended = cv2.bitwise_and(img, img, mask= mask)
    contours = findContours(mask)

    imgContours = img.copy()

    imgContours = drawContours(imgContours, contours)
    x, y = getBoundingbox(contours)
    points.append([x, y])
    addPoints(imgContours, points)

    cv2.imshow("image", imgBlended)
    cv2.imshow("countours", imgContours)
    cv2.waitKey(1)


