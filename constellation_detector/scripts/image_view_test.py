import cv2

image_path = "idol_images/h46-4.jpg"

image = cv2.imread(image_path)

# 画像表示
cv2.imshow("test image", image)
# 画像保存
# cv2.imwrite("filename", image)
# キーを終了する
cv2.waitKey(0)
cv2.destroyAllWindows()