##### 파일 몇 개 뽑아서 다른 폴더로 다시 작성 #####

import os
import random
import cv2

file_list = os.listdir('C:/Users/user/Desktop/false_1')
file_list = random.sample(file_list, 106)

# print(file_list)

for file in file_list:
    img = cv2.imread('C:/Users/user/Desktop/false_1/'+file)
    cv2.imwrite('C:/Users/user/Desktop/val/'+file, img)