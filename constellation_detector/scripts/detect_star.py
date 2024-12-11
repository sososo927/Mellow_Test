import cv2
import numpy as np


def detect_stars(image_path):
    # 画像の読み込み
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    # ノイズ除去
    blurred = cv2.GaussianBlur(image, (5, 5), 0)

    # 閾値処理で星を検出
    _, thresh = cv2.threshold(blurred, 200, 255, cv2.THRESH_BINARY)

    # 輪郭検出
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # 星の座標を格納
    stars = []
    for contour in contours:
        # 小さすぎる/大きすぎる輪郭は除外
        if 5 < cv2.contourArea(contour) < 50:
            M = cv2.moments(contour)
            if M["m00"] != 0:
                cx = int(M["m10"] / M["m00"])
                cy = int(M["m01"] / M["m00"])
                stars.append((cx, cy))

    return stars


# 使用例
star_locations = detect_stars('constellation_images/orion.png')
print(star_locations)