import cv2
import os
import numpy as np

for i in os.listdir('C:/Users/user/Desktop/bs_copy_rembg/'):
    path = 'C:/Users/user/Desktop/bs_copy_rembg/' + i

    # # 이미지 읽어서 그레이스케일 변환, 바이너리 스케일 변환
    # img = cv2.imread(path)
    # imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # ret, th = cv2.threshold(imgray, 127, 255, cv2.THRESH_BINARY_INV)
    #
    # # 컨튜어 찾기
    # contours, hr = cv2.findContours(th, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    # contr = contours[0]
    #
    # # 감싸는 사각형 표시(검정색)
    # # x, y, w, h = cv2.boundingRect(contr)
    # # cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 0), 3)
    #
    # # 최소한의 사각형 표시(초록색)
    # rect = cv2.minAreaRect(contr)
    # box = cv2.boxPoints(rect)  # 중심점과 각도를 4개의 꼭지점 좌표로 변환
    # box = np.int0(box)  # 정수로 변환
    # cv2.drawContours(img, [box], -1, (0, 255, 0), 3)
    #
    # # # 최소한의 원 표시(파랑색)
    # # (x, y), radius = cv2.minEnclosingCircle(contr)
    # # cv2.circle(img, (int(x), int(y)), int(radius), (255, 0, 0), 2)
    #
    # # 최소한의 삼각형 표시(분홍색)
    # # ret, tri = cv2.minEnclosingTriangle(contr)
    # # cv2.polylines(img, [np.int32(tri)], True, (255, 0, 255), 2)
    #
    # # 최소한의 타원 표시(노랑색)
    # # ellipse = cv2.fitEllipse(contr)
    # # cv2.ellipse(img, ellipse, (0, 255, 255), 3)
    #
    # # 중심점 통과하는 직선 표시(빨강색)
    # # [vx, vy, x, y] = cv2.fitLine(contr, cv2.DIST_L2, 0, 0.01, 0.01)
    # # cols, rows = img.shape[:2]
    # # cv2.line(img, (0, 0 - x * (vy / vx) + y), (cols - 1, (cols - x) * (vy / vx) + y), \
    # #          (0, 0, 255), 2)
    #
    # # 결과 출력
    # cv2.imshow('Bound Fit shapes', img)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    img = cv2.imread(path)
    image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # cv2.imshow("GrayScaled", image)
    # cv2.waitKey(0)

    ret, thresh = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY_INV)
    # cv2.imshow("Black&White", thresh)
    # cv2.waitKey(0)

    kernel1 = np.ones((2, 2), np.uint8)
    erosion = cv2.erode(thresh, kernel1, iterations=4)
    # cv2.imshow("AfterErosion", erosion)
    # cv2.waitKey(0)

    kernel2 = np.ones((1, 1), np.uint8)
    dilation = cv2.dilate(erosion, kernel2, iterations=5)
    # cv2.imshow("AfterDilation", dilation)
    # cv2.waitKey(0)

    contours, hierarchy = cv2.findContours(dilation, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    # sort contours
    sorted_ctrs = sorted(contours, key=lambda ctr: cv2.boundingRect(ctr)[1])

    mask = np.zeros_like(img)  # Create mask where white is what we want, black otherwise
    cv2.drawContours(mask, sorted_ctrs, 0, (255, 255, 255), -1)  # Draw filled contour in mask
    out = np.zeros_like(img)  # Extract out the object and place into output image
    out[mask == 255] = [255]

    # Show the output image
    cv2.imshow('Output', out)
    cv2.waitKey(0)

    image1 = cv2.cvtColor(out, cv2.COLOR_BGR2GRAY)

    # noise removal
    kernel = np.ones((10, 10), np.uint8)
    opening = cv2.morphologyEx(image1, cv2.MORPH_OPEN, kernel, iterations=2)

    # sure background area
    sure_bg = cv2.dilate(opening, kernel, iterations=4)

    # Finding sure foreground area
    sure_fg = cv2.erode(opening, kernel, iterations=3)
    cv2.imshow("foreground", sure_fg)
    cv2.waitKey(0)

    # Finding unknown region
    sure_fg = np.uint8(sure_fg)
    unknown = cv2.subtract(sure_bg, sure_fg)
    ret, thresh = cv2.threshold(unknown, 240, 255, cv2.THRESH_BINARY)

    unknown[thresh == 255] = 128

    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
    unknown = cv2.erode(unknown, kernel, iterations=1)

    cv2.imshow("unknown", unknown)
    cv2.waitKey(0)

    final_mask = sure_fg + unknown
    cv2.imwrite("Trimap.jpg", final_mask)
    cv2.imshow("final_mask", final_mask)
    cv2.waitKey(0)
    cv2.destroyAllWindows()