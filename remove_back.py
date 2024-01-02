import cv2

src = cv2.imread("nonbbox.jpg", cv2.IMREAD_COLOR)

gray = cv2.cvtColor(src, cv2.COLOR_RGB2GRAY)
blur = cv2.GaussianBlur(gray, (11,11), sigmaX=0.2)
ret, dst = cv2.threshold(blur, 100, 255, cv2.THRESH_BINARY)

cv2.imshow("dst", dst)
cv2.waitKey(0)
cv2.destroyAllWindows()