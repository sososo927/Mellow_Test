import os
import numpy as np
import cv2

## 必要関数設定
def generate_blank_image(_height, _width):
    img = np.ones((_height, _width, 3), np.uint8)
    for _h in range(0, height):
        for _w in range(0, width):
            img[_h, _w] = [0,0,0]
    return img

def skip_pos(target_a, target_b, pos_a, pos_b):
    if (target_a == pos_a and target_b == pos_b) or (target_a == pos_b and target_b == pos_a):
        return True

## 各種設定項目
image_path = "constellation_images/cassiopeia.jpg"
image = cv2.imread(image_path)
height, width, _ = image.shape
print(height, width)
save_filename, save_file_ext = os.path.basename(image_path).split('.')
save_path_blank = "constellation_images/simplified"
CONSTELLATION_NAME = "cassiopeia"
write_line=True
display_pos=False

blank_image = generate_blank_image(height, width)


## 画像処理
# image = cv2.resize(image, None, fx=2, fy=2)
image = cv2.GaussianBlur(image, (5,5), -1)
# _, image = cv2.threshold(image, 130, 255, cv2.THRESH_BINARY_INV)
_, image = cv2.threshold(image, 130, 255, cv2.THRESH_BINARY)
image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

## 特徴点抽出と描写(線・点)
akaze = cv2.AKAZE_create()
kp1 = akaze.detect(image_gray)
pts = list()
for i, _kp in enumerate(kp1):
    print(str(i).zfill(3), _kp.pt, _kp.size, _kp.angle, _kp.response, _kp.octave, _kp.class_id)
    pts.append((int(_kp.pt[0]), int(_kp.pt[1])))
    blank_image = cv2.circle(blank_image, (int(_kp.pt[0]), int(_kp.pt[1])), 1, (255,255,255), 2)
    if display_pos:
        image = cv2.putText(image, f"({int(_kp.pt[0]), int(_kp.pt[1])})", (int(_kp.pt[0]), int(_kp.pt[1])), 1, 0.8, (255,255,255))
blank_image_line = blank_image.copy()
cv2.imwrite(os.path.join(save_path_blank, f"simple_{CONSTELLATION_NAME}_noline.{save_file_ext}"), blank_image_line)
if write_line:
    for pti in pts:
        for ptj in pts:
            ### 不要線の削除
            if skip_pos(pti, ptj, (126,111), (165,471)): continue
            if skip_pos(pti, ptj, (126,111), (225,293)): continue
            if skip_pos(pti, ptj, (126,111), (247,273)): continue
            if skip_pos(pti, ptj, (126,111), (339,440)): continue
            if skip_pos(pti, ptj, (283,133), (201,308)): continue
            if skip_pos(pti, ptj, (283,133), (225,293)): continue
            if skip_pos(pti, ptj, (283,133), (339,440)): continue
            if skip_pos(pti, ptj, (283,133), (165,471)): continue
            if skip_pos(pti, ptj, (165,471), (225,293)): continue
            if skip_pos(pti, ptj, (165,471), (247,273)): continue
            if skip_pos(pti, ptj, (339,440), (201,308)): continue
            if skip_pos(pti, ptj, (339,440), (225,293)): continue
            if skip_pos(pti, ptj, (201,308), (247,273)): continue
            image = cv2.line(image, pti, ptj, (255,255,255))
            blank_image_line = cv2.line(blank_image, pti, ptj, (255, 255, 255))

## 画像の保存・ウィンドウ描画
image_akaze = cv2.drawKeypoints(image, kp1, None, flags=4)
cv2.imshow("blank", blank_image)
cv2.imwrite(os.path.join(save_path_blank, f"simple_{CONSTELLATION_NAME}.{save_file_ext}"), blank_image)
cv2.imwrite(os.path.join(save_path_blank, f"simple_{CONSTELLATION_NAME}_with_line.{save_file_ext}"), blank_image_line)
# cv2.imshow("result", image)
cv2.waitKey(0)
cv2.destroyAllWindows()