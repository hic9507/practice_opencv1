import os

file_path = 'C:/Users/user/Desktop/false_1'
dup_path = 'C:/Users/user/Desktop/train'

# for file in file_path:
#     for files in dup_path:
#         if files == file:
#             print(files)

for f in os.listdir(file_path):
    for j in os.listdir(dup_path):
        os.remove(f)