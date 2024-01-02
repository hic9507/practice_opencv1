import os
import cv2
import shutil
base_dir = 'C:/Users/user/Desktop/false_contour/' #커야지
compare_dir = 'C:/Users/user/Desktop/img_dataset_for_edge_detection/imgs/val/false/' #작고

img_list = os.listdir(base_dir)
compare_list = os.listdir(compare_dir)

for img in img_list:
    org_image = cv2.imread(base_dir+img)
    # cv2.imwrite('C:/Users/USER/PycharmProjects/DexiNed/id_data/edges/edge_maps/train/rgbr/real/true_{}.jpg'.format(img[:-4]), org_image)

    for compare in compare_list:
        # print(img)
        # print(compare)
        if img == compare:
        # if img != compare:
            # print(img)
            # print('true')
            cv2.imwrite('C:\\Users\\user\\Desktop\\img_dataset_for_edge_detection\\edge_maps\\val\\false\\{}'.format(img), org_image)
            # shutil.move(compare, 'C:\\Users\\user\\Desktop\\1')
            break