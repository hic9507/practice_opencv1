import os
import random

n_train = 0
n_validation = 0
n_test = 0
if __name__ == "__main__":
    root_dir = "D:/OCR/Training/ori_Training_printed/form/"
    for (root, dirs, files) in os.walk(root_dir):
        print("# root : " + root)
        # if len(dirs) > 0:
        #     for dir_name in dirs:
        #         print("dir: " + dir_name)

        # if len(files) > 0:
        #     for file_name in files:
        #         print("file: " + file_name)
        # print(len(files))
        random.shuffle(files)

        n_train += int(len(files) * 0.6)
        n_validation += int(len(files) * 0.2)
        n_test += int(len(files) * 0.2)

    print(n_train, n_validation, n_test)
    # print("# root : " + root)
# import numpy as np
#
#
# def X(x1, x2):
#     x = np.array([x1, x2])
#     w = np.array([0.3, -0.8])
#     b = -0.1
#     tmp = np.sum(w*x) + b
#
#     if tmp <= 0:
#         return 0
#     else:
#         return 1
#
# print(X(0,0))
# print(X(0,1))
# print(X(1,0))
# print(X(1,1))
