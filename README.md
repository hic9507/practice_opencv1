# opencv 연습

## 마우스를 이용해 이미지 좌표 획득 후 그 형태로 crop
111.py
 
## 이진화 이미지 얻기
binary.py

## 이미지 contour 그리기
### computer_vision.py
### draw_contour.py

## 이미지 워핑
### 이미지 꼭지점 좌표 얻기
coordinates.py

corner.py(goodFeaturesToTrack, FastFeatureDetector_create 사용)

findcontour.py

get_coordinates_with_mouse.py(마우스 사용해 좌표 얻고 json 파일에 저장 및 좌표를 통해 이미지 crop 후 해당 이미지 저장)

get_coordinates_with_mouse.WLs.py(위와 같음)

warping.py

warping2.py


## 파일 형식 변경 및 파일 이름 변경
name_change.py
png_to_jpg.py

## 두 폴더를 비교하여 이름이 같은 파일이 있으면 다른 폴더에 저장
pick.py

## 파일 지우기
### 중복된 파일 이름 삭제
delete_duplicate.py

## 이미지의 배경 지우기
canny edge detection

## 이미지 읽어와서 train:valid:test 비율 나누기
find_dir.py

## morphoogy 등 opencv 연산
crop.py
moment.py

## json 파일의 좌표 읽어와서 이미지 crop 후 저장
cropping_valid.py

## 동영상 프레임 추출
extraction.py

## 파일에 특정 문자가 들어있는 것 찾고 지우기
file_remove.py

## json 형태의 .lst 파일 병합
merge_lst.py

## 1. 이미지 이진화 및 배경 제거
## 2. 이진화 이미지에 canny 적용
## 3. canny 적용한 이미지에 contour 그리기
## 4. contour 채우기
convert.py
edge_detection.py
