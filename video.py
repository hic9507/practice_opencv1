import numpy as np
import cv2
import os

# Read image
for i in os.listdir('./140s/'):
    path = './140s/' + i
    image = cv2.imread(path, cv2.IMREAD_COLOR)

