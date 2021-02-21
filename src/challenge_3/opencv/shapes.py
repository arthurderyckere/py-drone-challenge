import cv2
import numpy as np

cap = cv2.VideoCapture(-1)
lower = np.array([85, 91, 129])
upper = np.array([179, 255, 255])


def drawContours(contours, img):
    for contour in contours:
        approx = cv2.approxPolyDP(contour, 0.01*cv2.arcLength(contour, True), True)
        if cv2.arcLength(contour, True) < 500:
            continue
        cv2.drawContours(img ,[approx] ,0 ,(255, 0, 255) ,2)
        labelApproximatePoly(approx, img)
    return img

def labelApproximatePoly(approx, img):
    x = approx.ravel()[0]
    y = approx.ravel()[1] - 5

    if len(approx) == 3:
        cv2.putText(img, "triangle", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))
    elif len(approx) == 4:
        cv2.putText(img, "rectangle", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))
    else:
        cv2.putText(img, "circle", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))

    
while True:
    success, img = cap.read()
    if success:
        imgHsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(imgHsv, lower, upper)
        imgBlended = cv2.bitwise_and(img, img, mask= mask)
        contours, hierachy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        
        drawContours(contours, img)

        cv2.imshow("contours", img)

    cv2.waitKey(1)