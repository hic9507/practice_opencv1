import os, cv2
import matplotlib.pyplot as plt
for i in os.listdir('C:/Users/user/Desktop/env/U-2-Net/test_data/u2net_results/'):
    path = 'C:/Users/user/Desktop/env/U-2-Net/test_data/u2net_results/' + i

    image = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    img1 = image.copy().astype("uint8")
    img2 = image.copy().astype("uint8")
    ret, imthres = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY_INV)

    # contour, hierarchy = cv2.findContours(imthres, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    #
    contour2, _ = cv2.findContours(img2, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    cv2.drawContours(img2, contour2, -1, (0,255,0), 4)

    for j in contour2:
        for k in j:
            cv2.circle(img2, tuple(k[0]), 1, (255, 0, 0), -1)

    c0 = contour2[0]

    x, y, w, h = cv2.boundingRect(c0)
    img1 = cv2.rectangle(img1, (x,y), (x+w, y+h), 7)

    rect = cv2.minAreaRect(c0)
    box = cv2.boxPoints(rect)
    box = box.astype('int')
    img2 = cv2.drawContours(img2, [box], -1, 7)

    cv2.imshow('CHAIN_APPROX_SIMPLE', img2)
    # print(i)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # cv2.imwrite("C:\\Users\\user\\Desktop\\bs_u2net_draw_contour\\" + i, img2)

    # plt.subplot(1, 2, 1)
    # plt.imshow(img1, cmap="gray")
    # plt.axis('off')
    # plt.title("Straight Rectangle")
    # plt.subplot(1, 2, 2)
    # plt.imshow(img2, cmap="gray")
    # plt.axis('off')
    # plt.title("Rotated Rectangle")
    # plt.show()