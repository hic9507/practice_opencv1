# img = cv2.imread('test.jpg')
# cropped_img = img[y: y + h, x: x + w]
import cv2
import numpy as np
import os
import json
import matplotlib.pyplot as plt


for i in os.listdir('C:/Users/user/Desktop/seo/'):
    path = 'C:/Users/user/Desktop/seo/' + i

    large = cv2.imread(path, cv2.IMREAD_COLOR)
    rgb = cv2.pyrDown(large)
    small = cv2.cvtColor(rgb, cv2.COLOR_BGR2GRAY)
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))
    grad = cv2.morphologyEx(small, cv2.MORPH_GRADIENT, kernel)
    _, bw = cv2.threshold(grad, 0.0, 255.0, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (9, 1))
    connected = cv2.morphologyEx(bw, cv2.MORPH_CLOSE, kernel)
    # using RETR_EXTERNAL instead of RETR_CCOMP
    contours, hierarchy = cv2.findContours(connected.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    mask = np.zeros(bw.shape, dtype=np.uint8)
    for idx in range(len(contours)):
        x, y, w, h = cv2.boundingRect(contours[idx])
        mask[y:y+h, x:x+w] = 0
        cv2.drawContours(mask, contours, idx, (255, 255, 255), -1)
        r = float(cv2.countNonZero(mask[y:y+h, x:x+w])) / (w * h)
        if r > 0.45 and w > 8 and h > 8:
            cv2.rectangle(rgb, (x, y), (x+w-1, y+h-1), (0, 255, 0), 2)
    # show image with contours rect
    cv2.imshow('rects', rgb)
    cv2.waitKey()

root_dir = "D:/OCR/Training/ori_Training_printed/form/"
for (root, dirs, files) in os.walk(root_dir):
    f = open(root)
    print(f)

# f =open("D:/OCR/Training/label_Training_printed/001/00110011001.json", 'r', encoding='utf-8')
#
# bbox = []
# lines = f.readlines()
#
# for line in lines:
#     line = line.strip()
#     if line == '':
#         continue
#     bbox.append(list(map(str, line.split(','))))
#
# img = cv2.imread('D:/OCR/Training/ori_Training_printed/form/001/00110011001.jpg')
# for idx, box in enumerate(bbox):
#     box = list(map(int( box)))
#     w = max(box[2]-box[0], box[4]-box[6])
#     h = max(box[5]-box[3], box[7]-box[1])
#     y = min(box[5],box[3], box[7],box[1])
#     x = min(box[2],box[0], box[4],box[6])
#     crop_img = img[y:y+h, x:x+w]
#     cv2.imwrite('C:/Users/user/Desktop/result/result{}.jpg'.format(idx), crop_img)
for i in os.listdir('D:/OCR/Training/label_Training_printed/001/'):
    path = 'D:/OCR/Training/label_Training_printed/001/' + i

    json_file = open(path, encoding='utf-8')
    json_data = json.load(json_file)
