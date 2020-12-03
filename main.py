import cv2
import numpy as np
print('done')

def empty(a):
    pass

path='traffic.jpg'
path1='1.jpg'




# img = cv2.imread('traffic.jpg')
# img=cv2.resize(img,(400,500))
# cv2.imshow('anh',img)


# cap = cv2.VideoCapture(0)
# cap.set(3,640)
# cap.set(4,480)
#
# while True :
#     success, img = cap.read()
#     cv2.imshow("video",img)
#     if cv2.waitKey(1) & 0xFF==ord('k'):
#         break
#     print(success)


def detection(path):

    cv2.namedWindow("TrackBar")
    cv2.resizeWindow("TrackBar", 640, 240)
    cv2.createTrackbar("Hue Min", "TrackBar", 0, 179, empty)
    cv2.createTrackbar("Hue Max", "TrackBar", 111, 179, empty)
    cv2.createTrackbar("Sat Min", "TrackBar", 145, 255, empty)
    cv2.createTrackbar("Sat Max", "TrackBar", 255, 255, empty)
    cv2.createTrackbar("Val Min", "TrackBar", 105, 255, empty)
    cv2.createTrackbar("Val Max", "TrackBar", 255, 255, empty)
    while True:
        img = cv2.imread(path)
        img = cv2.resize(img, (400, 500))
        imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

        h_min = cv2.getTrackbarPos("Hue Min", "TrackBar")
        h_max = cv2.getTrackbarPos("Hue Max", "TrackBar")
        s_min = cv2.getTrackbarPos("Sat Min", "TrackBar")
        s_max = cv2.getTrackbarPos("Sat Max", "TrackBar")
        v_min = cv2.getTrackbarPos("Val Min", "TrackBar")
        v_max = cv2.getTrackbarPos("Val Max", "TrackBar")
        print(h_min, h_max, s_min, s_max, v_min, v_max)
        lower = np.array([h_min, s_min, v_min])
        upper = np.array([h_max, s_max, v_max])
        mask = cv2.inRange(imgHSV, lower, upper)
        imgResult = cv2.bitwise_and(img, img, mask=mask)

        # cv2.imshow('anh Goc', img)
        # cv2.imshow('anh HSV', imgHSV)
        # cv2.imshow('Mask', mask)
        # cv2.imshow('Result', imgResult)

        Total = np.hstack((img, imgHSV, imgResult))
        cv2.imshow('Result', Total)
        cv2.waitKey(1)

detection(path1)