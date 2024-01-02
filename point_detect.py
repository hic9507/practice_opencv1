import cv2
import imutils
import numpy as np
import json

cap = cv2.VideoCapture("36.mp4")

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 700)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 800)
while True:
    #성공적으로 읽어들였는지의 flag, 캡쳐한 이미지
    success, img = cap.read()
    cv2.imshow("Video", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break