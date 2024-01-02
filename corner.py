# import cv2
# import numpy as np
# import matplotlib.pyplot as plt

# image = cv2.imread('./false_cc10_jpg.rf.dad38dec4b48e5f0b66b10cb9d329671.jpg') # result를 보기 쉽도록 체스판 image을 사용했습니다.
# imageRGB = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
# image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) # 꼭짓점 추출에는 흑백 image이 필요합니다.
# image_corner = cv2.cvtColor(image, cv2.COLOR_BGR2RGB) # 나중에 꼭짓점을 여기에 표시합니다.

# image_gray = np.float32(image_gray) # 넘파이(numpy)를 사용해서 자료형을 부동소수점으로 바꾸어주어야 합니다.
# result = cv2.cornerHarris(image_gray, 2, 3, 0.04) # 2, 3, 0.04는 바꿀 수 있는 인자들입니다.
# result = cv2.dilate(result, None, iterations=6) # 꼭짓점을 표시하기 위해 확장 (dilate) 연산을 합니다.
# image_corner[result>0.01*result.min()]=[255, 0, 0] # 꼭짓점이 빨간색 점으로 image에 표시됩니다.

# # 이 아래 부분은 image을 화면에 출력하기 위한 부분으로, OpenCV 알고리즘과는 상관이 없습니다.
# plt.subplot(1, 2, 1) # 1행 2열에서 1번째 열
# plt.imshow(imageRGB)
# plt.xticks([]) # x축 좌표 숨김
# plt.yticks([]) # y축 좌표 숨김

# plt.subplot(1, 2, 2) # 1행 2열에서 2번째 열
# plt.imshow(image_corner)
# plt.xticks([]) # x축 좌표 숨김
# plt.yticks([]) # y축 좌표 숨김
# plt.show()

##################################################################################################################################################################################

# import cv2
# import numpy as np
# filename = './false_cc10_jpg.rf.dad38dec4b48e5f0b66b10cb9d329671.jpg'

# img = cv2.imread(filename)
# img = cv2.resize(img, (512, 512))

# gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# gray = np.float32(gray)
# dst = cv2.cornerHarris(gray,2,3,0.04)
# img[dst>0.01*dst.max()]=[0,0,255]
# cv2.imshow('dst',img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

##################################################################################################################################################################################
############################################### 결과 제일 좋음
# import cv2
# import numpy as np

# img = cv2.imread('./false_cc10_jpg.rf.dad38dec4b48e5f0b66b10cb9d329671.jpg')
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# img = cv2.resize(img, (512, 512))
# gray = cv2.resize(gray, (512, 512))

# # Harris corner 검출
# corner = cv2.cornerHarris(gray, 2, 3, 0.05) # src= grayscale 이미지, 2: 코너 검출 위해 고려할 이웃 픽셀의 범위, 3: 소벨 미분에 사용된 인자 값, 0.05: 해리스 코너 검출 수학식 R에서 k 값
# img[corner > 0.01 * corner.max()] = [0,255,0]

# # 정규화
# corner_norm = cv2.normalize(corner, None, 0, 255, cv2.NORM_MINMAX, cv2.CV_8U)

# cv2.imshow('Harris', img)
# cv2.imshow('corner', corner_norm)
# cv2.waitKey()
# cv2.destroyAllWindows()

##################################################################################################################################################################################

# import cv2
# import numpy as np

# filename = './false_cc10_jpg.rf.dad38dec4b48e5f0b66b10cb9d329671.jpg'
# img = cv2.imread(filename)
# gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# img = cv2.resize(img, (512, 512))
# gray = cv2.resize(gray, (512, 512))

# # find Harris corners
# gray = np.float32(gray)
# dst = cv2.cornerHarris(gray,2,3,0.04)
# dst = cv2.dilate(dst,None)
# ret, dst = cv2.threshold(dst,0.01*dst.max(),255,0)
# dst = np.uint8(dst)

# # find centroids
# ret, labels, stats, centroids = cv2.connectedComponentsWithStats(dst)

# # define the criteria to stop and refine the corners
# criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 0.001)
# corners = cv2.cornerSubPix(gray,np.float32(centroids),(5,5),(-1,-1),criteria)

# # Now draw them
# res = np.hstack((centroids,corners))
# res = np.int0(res)
# img[res[:,1],res[:,0]] = [0,0,255]
# img[res[:,3],res[:,2]] = [0,255,0]
# cv2.imshow('dst',img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

##################################################################################################################################################################################
###################### 좌표까지 출력됨
import cv2
import os
import json
# src = cv2.imread('./false_cc10_jpg.rf.dad38dec4b48e5f0b66b10cb9d329671.jpg', cv2.IMREAD_GRAYSCALE)

for i in os.listdir('C:/Users/user/Desktop/img_dataset_for_edge_detection_/edge_maps/11/12/'):
    path = 'C:/Users/user/Desktop/img_dataset_for_edge_detection_/edge_maps/11/12/' + i
    
    src = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    src = cv2.resize(src, (512, 512))

    if src is None:
        print('Image load faile!')
        sys.exit()
        
    # 좋은 특징점 검출 방법
    corners = cv2.goodFeaturesToTrack(src, 4, 0.01, 10)

    dst1 = cv2.cvtColor(src, cv2.COLOR_GRAY2BGR)
    dst1 = cv2.resize(dst1, (512, 512))

    coordinates = []
    resultforJSON = []
    json_path = './coordinates_json/coordinates.json' #json으로 저장하기 위한 파일경로

    if corners is not None:
        for j in range(corners.shape[0]): # 코너 갯수만큼 반복문
            pt = (int(corners[j, 0, 0]), int(corners[j, 0, 1])) # x, y 좌표 받아오기
            cv2.circle(dst1, pt, 5, (0, 0, 255), 2) # 받아온 위치에 원
            print('사각형의 4개 꼭지점 좌표 출력')
            print(i)
            print(j)
            # print((int(corners[j, 0, 0]), int(corners[j, 0, 1])))
            # print(pt[0], pt[1])
            coordinates = []
            resultforJSON.append({'image: ':i, 'point: ':[j], 'coordinates: ':[(pt[0]), pt[1]]})
            with open(json_path, 'a') as outfile:  # resultforJSON에 저장된 내용을 json파일로 추출
                json.dump(resultforJSON, outfile, indent=4)
            print(pt)
            # print(pt)
            

    # Fast 코너 검출
    fast = cv2.FastFeatureDetector_create(60) # 임계값 60 지정
    keypoints = fast.detect(src) # Keypoint 객체를 리스트로 받음

    dst2 = cv2.cvtColor(src, cv2.COLOR_GRAY2BGR)
    dst2 = cv2.resize(dst2, (512, 512))

    for kp in keypoints:
        pt = (int(kp.pt[0]), int(kp.pt[1])) # kp안에 pt좌표가 있음
        cv2.circle(dst2, pt, 5, (0, 0, 255), 2)

    # cv2.imshow('src', src)
    cv2.imshow('dst1', dst1)
    # cv2.imshow('dst2', dst2)
    cv2.waitKey()

    cv2.destroyAllWindows()

##################################################################################################################################################################################