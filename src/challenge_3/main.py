from djitellopy import Tello
import cv2
import numpy as np

tello = Tello()
tello.connect()
tello.streamon()

tello.takeoff()
rotated = False
while not rotated:
    bg_frame = tello.get_frame_read()
    if bg_frame:
        img = cv2.resize(bg_frame.frame, (640, 480))
        imgHsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        lower, higher =  np.array([31, 111, 63]), np.array([179, 255, 255])
        mask = cv2.inRange(imgHsv, lower, higher)
        contours, hierarchy  = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        

        sending = False
        for contour in contours:
            arcLength = cv2.arcLength(contour, False)
            print(arcLength)
            if (arcLength > 200 and not sending):
                approx = cv2.approxPolyDP(contour, 0.01*arcLength, False)
                cv2.drawContours(img ,[approx] ,0 ,(255, 0, 255), 2)
                sending = True
                tello.rotate_clockwise(360)
                


        blended = cv2.bitwise_and(img, img, mask= mask)
        cv2.imshow("mask", mask)
        cv2.imshow("blended", blended)
        cv2.imshow("img", img)

    if (cv2.waitKey(1) & 0xFF == ord('q')):
        tello.land()
        break

