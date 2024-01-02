import copy
import math
import cv2
import numpy as np

try:
    from cv2 import cv2
except ImportError:
    pass

def piexel_generator(M, N, space, num_of_pixel, shape):
    x1, y1 = M[0][0], M[0][1]
    x2, y2 = N[0][0], N[0][1]

    for i in range(1, int(num_of_pixel + 1)):
        if (x1 != x2) and (y1 == y2):
            M.append([x1, y1 + space*i])
            N.append([x2, y2 + space*i])
            M.insert(0, [x1, y1 - space*i])
            N.insert(0, [x2, y2 - space*i])

        if (x1 == x2) and (y1 != y2):
            M.append([x1 + space * i, y1])
            N.append([x2 + space * i, y2])
            M.insert(0, [x1 - space * i, y1])
            N.insert(0, [x2 - space * i, y1])

            # if M[0][0] < int(image.shape[0] - 3/5 * image.shape[0]):
            if M[0][1] < 0:
                del M[0]
            if M[int(len(M)-1)][1] >= int(3/5 * shape[0]):
                del M[int(len(M) - 1)]
            # if M[0][1] < image.shape[1] - int(3/5 * image.shape[1]):
            if M[0][0] < 0:
                del M[0]
            if M[int(len(M)-1)][0] >= int(3/5 * shape[1]):
                del M[int(len(M) - 1)]

            # if N[0][0] < int(image.shape[0] - 3/5 * image.shape[0]):
            if N[0][1] < 0:
                del N[0]
            if N[int(len(N)-1)][1] >= int(3/5 * shape[0]):
                del N[int(len(N) - 1)]
            # if N[0][0] < image.shape[1] - int(3/5 * image.shape[1]):
            if N[0][0] < 0:
                del N[0]
            if N[int(len(N)-1)][0] >= int(3/5 * shape[1]):
                del N[int(len(N) - 1)]
    return M, N

image = cv2.imread('nonbbox.jpg')
image_gray = cv2.imread('nonbbox.jpg', cv2.IMREAD_GRAYSCALE)

x1, y1 = 0, 0
x2, y2 = image.shape[1]-1, 0
x3, y3 = 0, image.shape[0]-1
x4, y4 = image.shape[1]-1, image.shape[0]-1

A = [[x1, y1]]
B = [[x2, y2]]
C = [[x3, y3]]
D = [[x4, y4]]

space = 5
num_of_pixel = 10

def dist(P, A, B):
    area = abs((A[0] - P[0]) * (B[1] - P[1]) - (A[1] - P[1]) * (B[0] - P[0]))
    AB = ((A[0] - B[0]) ** 2 + (A[1] - B[1]) ** 2) ** 0.5
    return (area / AB)

def detector(A, B, image, image_gray):
    print('-------------------------- 탐색 시작 --------------------------')
    for i in range(len(A)):
        image = cv2.circle(image, (int(A[i][0]), int(A[i][1])), 4, (255, 0, 0), 3)
    for i in range(len(B)):
        image = cv2.circle(image, (int(B[i][0]), int(B[i][1])), 4, (255, 0, 0), 3)

    blur = cv2.GaussianBlur(image_gray, (3, 3), sigmaX=4.5)

    k = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))

    erosion = cv2.erode(blur, k)
    erosion2 = cv2.erode(erosion, k)
    erosion3 = cv2.erode(erosion2, k)
    closed = cv2.Canny(erosion3, 200, 200)

    index = 0
    pre_cnt = 0
    cnt = 0

    for q in range(len(A)):
        for w in range(len(B)):

            img = copy.deepcopy(image)

            index = 0
            pre_cnt = 0
            cnt = 0

            if A[q][1] <= B[w][1]:
                for i in range(A[q][1], B[w][1] + 1):
                    if A[q][0] <= B[w][0]:
                        for j in range(A[q][0], B[w][0] + 1):
                            if closed[i][j] == 255:
                                dist((j, i), A[q], B[w])
                                if dist < 3:
                                    img = cv2.circle(img, (j, i), 4, (0, 255, 255), 1)
                        if pre_cnt < cnt:
                            pre_cnt = cnt
                            index = q * len(A) + w
                            print(index)

                    else:
                        for j in range(B[w][0], A[q][0] + 1):
                            if closed[i][j] == 255:
                                dist((j, i), A[q], B[w])
                                if dist < 3:
                                    img = cv2.circle(img, (j, i), 4, (0, 255, 255), 1)
                        if pre_cnt < cnt:
                            pre_cnt = cnt
                            index = q * len(A) + w
                            print(index)

            else:
                for i in range(B[w][1], A[q][1] + 1):
                    if A[q][0] <= B[w][0]:
                        for j in range(A[q][0], B[w][0] + 1):
                            if closed[i][j] == 255:
                                dist((j, i), A[q], B[w])
                                if dist < 3:
                                    img = cv2.circle(img, (j, i), 4, (0, 255, 255), 1)
                        if pre_cnt < cnt:
                            pre_cnt = cnt
                            index = q * len(A) + w
                            print(index)

                    else:
                        for j in range(B[w][0], A[q][0] + 1):
                            if closed[i][j] == 255:
                                dist((j, i), A[q], B[w])
                                if dist < 3:
                                    img = cv2.circle(img, (j, i), 4, (0, 255, 255), 1)
                        if pre_cnt < cnt:
                            pre_cnt = cnt
                            index = q * len(A) + w
                            print(index)

    qq = int(math.trunc(float(index/len(A))))
    ww = int(index%len(B))

    cv2.line(image, (A[qq][0], A[qq][1]), (B[ww][0], B[ww][1]), (255, 255, 0), 4)
    print("----------------- 탐색 완료 -----------------")

    return [A[qq][0], A[qq][1]], [B[ww][0], B[ww][1]]

Z, X = piexel_generator(copy.deepcopy(A), copy.deepcopy(B), space, num_of_pixel, image.shape)
print(detector(Z, X, image, image_gray))

Z, X = piexel_generator(copy.deepcopy(A), copy.deepcopy(C), space, num_of_pixel, image.shape)
print(detector(Z, X, image, image_gray))

Z, X = piexel_generator(copy.deepcopy(B), copy.deepcopy(D), space, num_of_pixel, image.shape)
print(detector(Z, X, image, image_gray))

Z, X = piexel_generator(copy.deepcopy(C), copy.deepcopy(D), space, num_of_pixel, image.shape)
print(detector(Z, X, image, image_gray))

cv2.imshow('dasd', image)
k = cv2.waitKey()
while(1):
    if k == 27:
        break