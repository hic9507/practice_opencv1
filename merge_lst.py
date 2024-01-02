import cv2
import imutils
import numpy as np
import json, sys
import os, glob
from PIL import Image
import natsort


# for i in os.listdir('C:/Users/user/Desktop/binary_frame_remove_back/'):
#     path = 'C:/Users/user/Desktop/binary_frame_remove_back/' + i
#     #
#     image = cv2.imread(path, cv2.IMREAD_COLOR)
#     # os.rename((i), i + '.jpg')
#     f = open('C:/Users/user/Desktop/binary_frame_remove_back.lst', 'a')
#     f.write(path + '\n')
#     f.close()
#     # # cv2.imwrite("C:\\Users\\user\\Desktop\\frame_png_to_jpg\\" + i + '.jpg', image)
#     # print(path)
#     # with open('image.text', 'w', encoding='utf-8') as f:
#     #     for path in os.listdir('C:/Users/user/Desktop/frame_png_to_jpg/aa/'):
#     #         f.write(path + '\n')

# tmp = 'C:/Users/user/Desktop/frame_png_to_jpg.lst'
# list = []
# with open('C:/Users/user/Desktop/binary_frame_remove_back.lst', 'r', encoding='utf-8') as f:
#     example = f.read().splitlines()
#     print(example)
#     list.append(example.split(' '))
#     tmp2 = example.split(' ')
#     f = open('C:/Users/user/Desktop/total', 'a')
#     f.write(tmp2 + '\n')
#     f.close()
#
# for i in example:
#     # print(i)
#     list.append(i.split(' '))
# print(type(example))

f1 = open('C:/Users/user/Desktop/rgb.lst', 'r', encoding='utf-8')
list = []
f2 = open('C:/Users/user/Desktop/edge_maps.lst', 'r', encoding='utf-8')
a = f1.read().splitlines()
b = f2.read().splitlines()
# print(len(a))
# print(len(a))
# print(len(a))
# print(len(a))
# print(len(a.read().splitlines()))
for i in range(len(a)):
    # list.append([a[i], b[i]])
    list.append([a[i], b[i]])


    # if (list[a[i] == a[i-1]]) and (list[b[i] == b[i-1]]):
    #     del a[0]
    #     del b[0]
    # list = natsort.natsorted(list, reverse=False)
    # print(natsort.natsorted(list[i])) # jpg 뒤에 png를 추가해야하는데 이렇게 하면 png 뒤에 jpg가 추가됨. j 다음 p. binary 때문에 오름차순 정렬하면 b를 읽어와서 그런 듯?
    # print(list[i].sort(key=len(str(i))))
    # print(list[i])
    # list = [str(x) for x in list]
    # list.sort()
    # list(a[i])
    # if a[0] in list:
    #     del a[0]
    # sys.stdout = open('C:/Users/user/Desktop/train.lst', 'a')
    print(a[i], b[i])
    # print(list[i])
    # sys.stdout.close()


# print(f1.read())
# list.append(f1.read().splitlines())
# print(list)
# list.insert(f2.read().splitlines())

# print(example)
# list.append(f1)
# print(example)
# list.append(example)
# print(type(list))
# print(list)

# tmp2 = list.split(' ')

    # list.append(example.split(" "))
    # tmp2 = example.split(" ")
    # f = open('C:/Users/user/Desktop/total.lst', 'a')
    # f.write(tmp2 + '\n')
    # f.close()

# for i in example:
#     print(i)
    # list.append(i.split(' '))
# print(type(example))