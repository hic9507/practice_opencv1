import cv2
import os
import imutils
import numpy as np

for i in os.listdir('C:/Users/user/Desktop/test/'):
    path = 'C:/Users/user/Desktop/test/' + i

    edged = cv2.imread(path, cv2.IMREAD_COLOR)
    edged = cv2.resize(edged, (700, 800))
    blur = cv2.GaussianBlur(edged, (11, 11), sigmaX=0.2)
    edged = cv2.Canny(blur, 3, 50)
    cv2.imshow('edged', edged)
    cv2.waitKey(0)
    # inverted_image = np.invert(image)

    # blur = cv2.GaussianBlur(image, (11,11), sigmaX=0.2)

    k = cv2.getStructuringElement(cv2.MORPH_RECT, (5,5))

    # canny = cv2.Canny(blur, 50, 150)
    # edged = cv2.resize(canny, (700, 800))

    # cnts = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    # cnts = imutils.grab_contours(cnts)
    # cnts = sorted(cnts, key=cv2.contourArea, reverse=True)
    #
    # findCnt = None
    # try:
    #
    #     # 정렬된 contours를 반복문으로 수행하며 4개의 꼭지점을 갖는 도형을 검출
    #     for c in cnts:
    #         # print(c)
    #         peri = cv2.arcLength(c, True)
    #         # print(peri)
    #         approx = cv2.approxPolyDP(c, 0.01 * peri, True)
    #
    #         # contours가 크기순으로 정렬되어 있기때문에 제일 첫번째 사각형을 영역으로 판단하고 break
    #         if len(approx) == 4:
    #             findCnt = approx
    #             break
    #
    #     # 만약 추출한 윤곽이 없을 경우 오류
    #     if findCnt is None:
    #         raise Exception(("Could not find outline."))
    # except:
    #     continue
    #
    # output = edged.copy()
    # # print(output.shape)
    # cv2.drawContours(output, [findCnt], -1, (0, 255, 0), 2)
    # # print(image.shape[0])
    # tmp = np.zeros([edged.shape[0], edged.shape[1], 3], dtype=np.uint8)
    # tmp.fill(0)
    # cv2.drawContours(tmp, [findCnt], -1, (255, 255, 255), 2)
    #
    # cv2.imshow('s', tmp)
    cv2.waitKey()