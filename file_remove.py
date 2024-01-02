##### 파일에 특정한 문자가 들어가있는 것 찾고 지우기 #####

import os
pick_files = ['true']
org_dir = r'C:/Users/user/Desktop/train'

for i in range(0, len(pick_files)):
    file_list = os.listdir(org_dir)
    delete_num = [n for n in range(len(file_list)) if pick_files[i] in file_list[n]]
    for j in delete_num:
        os.remove('{}/{}'.format(org_dir, file_list[j]))