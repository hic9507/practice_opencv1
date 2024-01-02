import cv2 as cv
import imutils
import numpy as np
import json
import os

pts = [] #마우스로 클릭한 포인트를 저장
resultforJSON = [] # pts에 저장된 포인트를 json형태로 저장
file_path = 'C:/Users/user/Desktop/get_coordinates_with_mouse_using_opencv/1124/coordinates/vidoes_frame_4_sample2_0.json' #json으로 저장하기 위한 파일경로
base_dir = 'C:/Users/user/Desktop/get_coordinates_with_mouse_using_opencv/1124/2/0/' # 이미지 읽어오는 경로
img_list = os.listdir(base_dir)

global img_file
def draw_roi(event, x, y, flags, param):  # roi검출을 위한 함수 정의
    img2 = img.copy()
    black = np.zeros((img.shape[0],img.shape[1],3), dtype=np.uint8)
    global img_file
    if event == cv.EVENT_LBUTTONDOWN:  # 마우스 왼쪽버튼을 클릭하면
        pts.append((x, y))  # pts에 (x,y)좌표를 추가한다
        print('이미지:', img_file)
        print('포인트 #%d 좌표값(%d,%d)' % (len(pts), x, y))  # 정상적으로 추가되는지 출력으로 확인
        resultforJSON.append({'image': img_file,
                            'point': [len(pts)],
                            'coordinate': [[int(x), int(y)]]})
        # 포인트 순서와 좌표값을 딕셔너리 형태로 추가해준다

        if event == cv.EVENT_RBUTTONDOWN:  # 마우스 오른쪽버튼을 클릭하면
            pts.pop()  # 클릭했던 포인트를 삭제한다

        if event == cv.EVENT_MBUTTONDOWN:  # 마우스 중앙(휠)버튼을 클릭하면
            print('총 %d개의 포인트 설정' % len(pts))
        mask = np.zeros(img.shape, np.uint8)  # 컬러를 다루기 때문에 np로 형변환
        points = np.array(pts, np.int32)
        points = points.reshape((-1, 1, 2))  # pts 2차원을 이미지와 동일하게 3차원으로 재배열

        mask = cv.polylines(mask, [points], True, (255, 255, 255), 2)  # 포인트와 포인트를 연결하는 라인을 설정
        mask2 = cv.fillPoly(mask.copy(), [points], (255, 255, 255))  # 폴리곤 내부 색상 설정

        mask_black = np.zeros(black.shape, np.uint8)
        mask_black = cv.polylines(mask_black, [points], True, (255, 255, 255), 2)

        ROI = cv.bitwise_and(mask2, img)  # mask와 mask2에 중첩된 부분을 추출

        if len(pts) == 4:
            with open(file_path, 'a') as outfile:  # resultforJSON에 저장된 내용을 json파일로 추출
                json.dump(resultforJSON, outfile, indent=4)

                # cv.imwrite('ROI.png', ROI)
                # cv.imwrite('C:/Users/user/Desktop/bs_coordinate_with_mouse/warping/6/{}'.format(img_file), ROI)
                cv.imwrite('C:/Users/user/Desktop/get_coordinates_with_mouse_using_opencv/1124/coordinates/mask/{}'.format(img_file), mask_black)
        # cv.imshow('ROI', ROI)
        # cv.imshow('black', mask_black)
        # cv.waitKey(0)

    if len(pts) > 0:  # 포인트를 '원'으로 표시
        cv.circle(img2, pts[-1], 3, (0, 0, 255), -1)

    if len(pts) > 1:
        for i in range(len(pts) - 1):
            cv.circle(img2, pts[i], 5, (0, 0, 255), -1)
        cv.line(img=img2, pt1=pts[i], pt2=pts[i + 1], color=(255, 255, 255), thickness=2)



    cv.imshow('image', img2)

a = 0
for img_file in img_list:
    img = cv.imread(base_dir+img_file)
    # img = imutils.resize(img, width=500)
    cv.namedWindow('image')
    cv.setMouseCallback('image', draw_roi)
    print(len(img_list) - a)

    while True:
        key = cv.waitKey(1) & 0xFF
        # key = cv.waitKey(0)
        # print(key)

        if key == 1:
            break
        if key == ord('s'):
            saved_data = {'ROI': pts}
            # print(type(pts))
            break
    if len(pts) == 4:
        pts.clear()
    a += 1

    # print(len(pts))
    cv.destroyAllWindows()