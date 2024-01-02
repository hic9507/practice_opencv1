import json
import pandas as pd
import os
import glob

base_label_path = 'D:/OCR/Training/label_Training_printed/'
base_image_path = 'D:/OCR/Training/ori_Training_printed'
# filenames = os.listdir(base_path)
# for filename in filenames:
#     full_filename = os.path.join(base_path, filename)
#     ext = os.path.splitext(full_filename)[-1]
#     if ext == 'json':
#         print(full_filename)
#
#
# for i in os.walk(base_path):
#     print(i)
#
# for i in os.listdir(base_path):
#     for j in os.walk(base_path):
#
# all_dir = glob.glob('D:/OCR/Training/label_Training_printed/**/*.json', recursive=True)
all_label = glob.glob(base_label_path + '/**/*.json', recursive=True)
all_image = glob.glob(base_image_path + '/**/*.jpg', recursive=True)

for i in os.listdir('D:/OCR/Training/ori_Training_printed'):
    path = base_image_path + i
    print(i)