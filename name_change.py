##### 파일명 바꾸기 #####
import os
import cv2

file_path = 'C:/Users/user/Desktop/false_contour/'
file_names = os.listdir(file_path)
i = 0
for name in file_names:
    src = os.path.join(file_path, name)
    dst = 'false_' + str(i) + '.jpg'
    # dst = str(i) + '.jpg'
    dst = os.path.join(file_path, dst)
    os.rename(src, dst)
    i += 1