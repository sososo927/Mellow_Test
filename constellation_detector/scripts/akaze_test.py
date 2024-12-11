import cv2

img1 = cv2.imread("constellation_images/cassiopeia.jpg")
img2 = cv2.imread("constellation_images/formated_cassiopeia.jpg")

img1 = cv2.resize(img1, None, fx=0.5, fy=0.5)
img2 = cv2.resize(img2, None, fx=0.5, fy=0.5)

akaze = cv2.AKAZE_create()

kp1, des1 = akaze.detectAndCompute(img1, None)
kp2, des2 = akaze.detectAndCompute(img2, None)

bf = cv2.BFMatcher()
matches = bf.knnMatch(des1, des2, k=2)

ratio = 0.1
good = []
for m, n in matches:
    if m.distance < ratio * n.distance:
        good.append([m])

img3 = cv2.drawMatchesKnn(img1, kp1, img2, kp2, good, None, flags=2)

cv2.imshow("result", img3)
cv2.waitKey(0)
cv2.destroyAllWindows()