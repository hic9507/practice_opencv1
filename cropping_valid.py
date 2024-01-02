import json
import os
import cv2, numpy as np
import matplotlib.pyplot as plt

# base_label_path = 'D:/ocr_share/Training/label_Training_printed/'
# base_image_path = 'D:/OCR/Training/ori_Training_printed/form/'
base_label_path = 'D:/ocr_share/various_shape_OCR/Validation/label_form/'
base_image_path = 'D:/ocr_share/various_shape_OCR/Validation/image_form/'

labeling_f = open('C:/Users/user/Desktop/test/label_valid.txt', 'w', encoding='utf-8')
count = 0

################################## json 파일 읽어오기
for q in os.listdir(base_label_path):
    num_folder = q
    # print(num_folder) # 001~050

    for w in os.listdir(base_label_path + num_folder):
        label_file_name = w
        # print(label_file_name) ### 00110011001.json~05010103040.json

        ### 모든 폴더에 있는 json 파일 다 읽어와서 f에 저장
        f = (open(base_label_path + num_folder + '/' + label_file_name, 'r', encoding='utf-8'))
        file_json = json.load(f)

        for id in range(len(file_json['text']['word'])):
            bbox = file_json['text']['word'][id]['wordbox']

            # 이미지 이름 가져오기
            labeling = file_json['image']['file_name']
            # 이미지의 한 단어 가져오기
            value = file_json['text']['word'][id]['value']

            img = cv2.imread('D:/ocr_share/various_shape_OCR/Validation/image_form/' + num_folder + '/' + labeling, 0)

            x = bbox[0]
            y = bbox[1]
            w = bbox[2] - bbox[0]
            h = bbox[3] - bbox[1]

            crop_img = img[y:y + h, x:x + w]

            cv2.imwrite('D:/ocr_share/various_shape_OCR(crop)_valid/' + labeling[:-4] + '_' + str(count) + '.jpg', crop_img)

            labeling_f.write('D:/ocr_share/various_shape_OCR(crop)_valid/' + labeling[:-4] + '_' + str(count) + '.jpg' + '\t' + value + '\n')

            count += 1
