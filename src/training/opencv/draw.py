import cv2
import numpy as np

img = np.zeros((512, 512, 3), np.uint8)
# img[0:100, 0:100]=255,0,0

cv2.line(img, (0,0), (img.shape[1],img.shape[0]), (255,0,255), 1)

cv2.rectangle(img, (0, 0), (100, 100), (255, 0, 125), cv2.FILLED)

cv2.imshow("image", img)


cv2.waitKey(0)