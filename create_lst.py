import os
import cv2

for i in os.listdir('C:/Users/user/Desktop/false_1/'):
    path = 'C:/Users/user/Desktop/false_1/' + i
    #
    image = cv2.imread(path, cv2.IMREAD_COLOR)
    # os.rename((i), i + '.jpg')
    f = open('C:/Users/user/Desktop/false.txt', 'a')
    f.write(path + '\n')
    f.close()