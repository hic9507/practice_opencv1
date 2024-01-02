import os
import cv2
import numpy as np
import imutils

for i in os.listdir('C:/Users/user/Desktop/bs/'):
    path = 'C:/Users/user/Desktop/bs/' + i

    image = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    mb_image = cv2.medianBlur(image, 7)
    equ = cv2.equalizeHist(mb_image)
    blur = cv2.GaussianBlur(equ, (15, 15), sigmaX=0)
    canny = cv2.Canny(blur, 50, 50)

    try:
        img = image.copy().astype("uint8")
        ret, imthres = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV)
        
        contour2, _ = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

        cv2.drawContours(img, contour2, -1, (0, 255, 0), 4)

        for j in contour2:
            for k in j:
                cv2.circle(img, tuple(k[0]), 1, (255, 0, 0), -1)

        c0 = contour2[0]

        x, y, w, h = cv2.boundingRect(c0)
        img = cv2.rectangle(img, (x, y), (x + w, y + h), 7)

        rect = cv2.minAreaRect(c0)
        box = cv2.boxPoints(rect)
        box = box.astype('int')
        canny = cv2.drawContours(img, [box], -1, 7)

        cnts = cv2.findContours(canny.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        cnts = imutils.grab_contours(cnts)
        cnts = sorted(cnts, key=cv2.contourArea, reverse=True)

        findCnt = None
    except:
        continue

    try:
        # 정렬된 contours를 반복문으로 수행하며 4개의 꼭지점을 갖는 도형을 검출
        for c in cnts:
            peri = cv2.arcLength(c, True)
            approx = cv2.approxPolyDP(c, 0.01 * peri, True)

            # contours가 크기순으로 정렬되어 있기때문에 제일 첫번째 사각형을 영역으로 판단하고 break
            if len(approx) == 4:
                findCnt = approx
                break

        # 만약 추출한 윤곽이 없을 경우 오류
        if findCnt is None:
            raise Exception(("Could not find outline."))
    except: # 오류 발생 시 무시하고 진행
        continue

    output = image.copy()
    
    cv2.drawContours(output, [findCnt], -1, (0, 255, 0), 2)
    
    black = np.zeros([image.shape[0], image.shape[1], 3], dtype=np.uint8)
    black.fill(0)
    cv2.drawContours(black, [findCnt], -1, (255, 255, 255), 2)

    cv2.imshow('contour', black)
    cv2.waitKey()
    cv2.destroyAllWindows()
    cv2.imwrite("C:\\Users\\user\\Desktop\\false_contour\\" + i, black)