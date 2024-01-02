import cv2
import os
import sys
import numpy as np
import imutils

# for i in os.listdir('./140s/'):
#     path = './140s/' + i
#
#     image = cv2.imread(path, cv2.IMREAD_COLOR)
#     if image is None:
#         print('Image load failed')
#         sys.exit()
#     cv2.imshow('image', image)
#     cv2.waitKey(0)

def difference_of_Gaussians(img, k1, s1, k2, s2):
    b1 = cv2.GaussianBlur(img,(k1, k1), s1)
    b2 = cv2.GaussianBlur(img,(k2, k2), s2)
    return b1 - b2

for i in os.listdir('./140s/'):
    path = './140s/' + i

    image = cv2.imread(path, cv2.IMREAD_COLOR)
    gray = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    image = cv2.resize(image, (800,600))
    gray = cv2.resize(gray, (800,600))
    if image is None:
        print('Image load failed')
        sys.exit()

    blur = cv2.GaussianBlur(gray, (3,3), sigmaX=4.5)

    k = cv2.getStructuringElement(cv2.MORPH_RECT, (5,5))

    erosion = cv2.erode(blur, k)
    erosion2 = cv2.erode(erosion, k)
    erosion3 = cv2.erode(erosion2, k)
    edged = cv2.Canny(erosion2, 300, 300)
    '''
    # # Addaptive Gauss Threshholding
    # thresh = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 11, 3)
    # 
    # # median filter
    # median_blur = cv2.medianBlur(thresh, 7)
    # 
    # # Remove small white point
    # nlabels, labels, stats, centroids = cv2.connectedComponentsWithStats(median_blur, None, None, None, 8, cv2.CV_32S)
    # 
    # # get CC_STAT_AREA component as stats[label, COLUMN]
    # areas = stats[1:, cv2.CC_STAT_AREA]
    # result = np.zeros((labels.shape), np.uint8)
    # 
    # for j in range(0, nlabels - 1):
    #     if areas[j] >= 100:  # keep
    #         result[labels == j + 1] = 255

    # blurred = cv2.GaussianBlur(result, ksize, 0)
    '''

    # contours를 찾아 크기순으로 정렬
    cnts = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    cnts = sorted(cnts, key=cv2.contourArea, reverse=True)
    findCnt = None

    # 정렬된 contours를 반복문으로 수행하며 4개의 꼭지점을 갖는 도형을 검출
    for c in cnts:
        # print(c)
        peri = cv2.arcLength(c, True)
        # print(peri)
        approx = cv2.approxPolyDP(c, 0.01 * peri, True)

        # contours가 크기순으로 정렬되어 있기때문에 제일 첫번째 사각형을 영역으로 판단하고 break
        if len(approx) == 4:
            findCnt = approx
            break

    # 만약 추출한 윤곽이 없을 경우 오류
    if findCnt is None:
        raise Exception(("Could not find outline."))

    output = image.copy()
    # print(output.shape)
    cv2.drawContours(output, [findCnt], -1, (0, 255, 0), 2)
    # print(image.shape[0])
    tmp = np.zeros([image.shape[0], image.shape[1], 3], dtype=np.uint8)
    tmp.fill(0)
    cv2.drawContours(tmp, [findCnt], -1, (255, 255, 255), 2)

    # blurred = difference_of_Gaussians(gray, 9, 9, 11, 7)
    # edged = cv2.Canny(blurred, 0, 50)

    # edged = cv2.Canny(erosion3, 3, 50)

    cv2.imshow('edged', tmp)
    cv2.waitKey(0)