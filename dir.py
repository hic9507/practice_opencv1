import os
import cv2
import numpy as np
import imutils

for i in os.listdir('C:/Users/user/Desktop/img_dataset_for_edge_detection/imgs/'):
    path = 'C:/Users/user/Desktop/img_dataset_for_edge_detection/imgs/' + i
    # print(path)


# for (path, dir, files) in os.walk('C:/Users/user/Desktop/img_dataset_for_edge_detection/imgs/train/'):
#     for filename in files:
#         ext = os.path.splitext(filename)[-1]
#         if ext == '.jpg':
#             print("%s/%s" % (path, filename))


# for i in os.walk('C:/Users/user/Desktop/img_dataset_for_edge_detection/imgs/train/'):
#     print(i)

images_path_ = 'C:/Users/user/Desktop/img_dataset_for_edge_detection/imgs/'
# for i in os.walk('C:/Users/user/Desktop/img_dataset_for_edge_detection/imgs/train/'):
#     print(i)
images_path = [file for file in os.walk('C:/Users/user/Desktop/img_dataset_for_edge_detection_/imgs/')]
# images_path = [file for file in os.walk(".jpg")]
# print(images_path)

q = os.listdir('C:/Users/user/Desktop/img_dataset_for_edge_detection_/imgs/')
print(q)