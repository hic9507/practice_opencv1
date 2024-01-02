import cv2
import os

videoPath = 'C:/Users/user/Desktop/video/'
imagePath = 'C:/Users/user/Desktop/frame/'
file_list = os.listdir(videoPath)
img_list = []
for file in file_list:
    print(file[:-4])

    # if not (os.path.isdir(videoPath + file)):
    #     os.makedirs(os.path.join(imagePath + file))

    cap = cv2.VideoCapture(videoPath + file)

    count = 0
    # a=0
    while True:
        ret, image = cap.read()
        # cv2.imshow('aaa',image)
        # cv2.waitKey()

        if not ret:
            break
        if count%2==0:
            cv2.imwrite(imagePath + file[:-4] + str(count) +".jpg", image)
            img_list.append(image)

        print('%d.jpg done' % count)
        count += 1
    # a+=1
    # print(len(img_list))
    # print(img_list)
    # cv2.imshow('aaa',img_list[0])
    # cv2.imshow('aaa2',img_list[50])
    # cv2.waitKey()
    cap.release()

        



# import cv2
# import os

# filepath= 'C:/Users/user/Desktop/video/1.mp4'
# video = cv2.VideoCapture(filepath)



# if not video.isOpened():
#     print("Could not Open :", filepath)
#     exit(0)


# #불러온 비디오 파일의 정보 출력
# length = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
# width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
# height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
# fps = video.get(cv2.CAP_PROP_FPS)

# print("length :", length)
# print("width :", width)
# print("height :", height)
# print("fps :", fps)


# try:
#     if not os.path.exists(filepath[:-4]):
#         os.makedirs(filepath[:-4])
# except OSError:
#     print ('Error: Creating directory. ' +  filepath[:-4])


# count = 0

# while(video.isOpened()):
#     ret, image = video.read()
#     if(int(video.get(1)) % fps == 0): #앞서 불러온 fps 값을 사용하여 1초마다 추출
#         cv2.imwrite(filepath[:-4] + "/frame%d.jpg" % count, image)
#         print('Saved frame number :', str(int(video.get(1))))
#         count += 1
        
# video.release()