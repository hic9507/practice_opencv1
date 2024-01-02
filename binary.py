import cv2
import os


for i in (os.listdir('C:/Users/user/Desktop/false')):
    path = 'C:/Users/user/Desktop/false/' + i

    gray = cv2.imread(path, cv2.IMREAD_GRAYSCALE)

    clahe = cv2.createCLAHE(clipLimit=1.2, tileGridSize=(4,4))
    cll = clahe.apply(gray)
    equ = cv2.equalizeHist(cll)
    equ = cv2.GaussianBlur(equ, (19, 19), sigmaX=0)


    blur = cv2.GaussianBlur(equ, (11, 11), sigmaX=0)
    k = cv2.getStructuringElement(cv2.MORPH_RECT, (9, 9))

    canny = cv2.Canny(blur, 50, 50)

    cv2.imshow('Erode',  canny)
    cv2.waitKey()
    # cv2.imwrite("C:\\Users\\user\\Desktop\\false_canny\\" + i, canny)
