import cv2

def empty(a):
    pass

def createCannyWindow():
    cv2.namedWindow("CANNY")
    cv2.resizeWindow("CANNY", 640, 480)
    cv2.createTrackbar("Canny min", "CANNY", 0, 255, empty)
    pass

createCannyWindow()
# cap = cv2.VideoCapture("./resources/square_and_ellipse.mp4")
cap = cv2.VideoCapture(-1)
while True: 
    success, img = cap.read()
    if success:
        img = cv2.resize(img, (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)//2), int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)//2)))
        imgGrey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        imgBlur = cv2.GaussianBlur(imgGrey, (5, 5), 1)
        imgCanny = cv2.Canny(imgBlur, cv2.getTrackbarPos("Canny min", "CANNY"), int(cv2.getTrackbarPos("Canny min", "CANNY"))*3)
        cv2.imshow("img", img)
        cv2.imshow("imgCanny", imgCanny)
    else:
       print('no video')
       cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
    
    cv2.waitKey(1)