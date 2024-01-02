from PIL import Image
import os
import cv2

path = './'
os.chdir(path)
files = os.listdir(path)
for filename in os.listdir(path):
        if(filename.endswith("pdf")):
            new_filename = filename.replace("pdf", "jpg")
            os.rename(filename, new_filename)
# base_dir = 'C:/Users/user/Desktop/frame_remove_background(RGB)/'
# def get_files_count(base_dir):
# 	dirListing = os.listdir(base_dir)
#
# 	return len(dirListing)
# a = get_files_count(base_dir)
#
# base_dir = 'C:/Users/user/Desktop/frame_remove_background(RGB)/'
# os.chdir(base_dir)
# files = os.listdir(base_dir)
#
# # for i in (os.listdir(base_dir)):
# for i in range(a+1):
#     path = base_dir + i
#     image = cv2.imread(path, cv2.IMREAD_COLOR)
#     # a = len((os.listdir(base_dir)))
#
    # cv2.imwrite("C:\\Users\\user\\Desktop\\frame_remove_background(RGB)_sort\\" + a, image)