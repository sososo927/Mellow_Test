import cv2

def format_constellation(_image_path: str):
    _gaussian_kernel_size = 15
    _image = cv2.imread(_image_path) # 画像読み込み
    # _image = cv2.resize(_image,None, fx=0.8, fy=0.8)
    _image = cv2.cvtColor(_image, # BGR(3)からGRAY(2)
                          cv2.COLOR_BGR2GRAY)
    _image = cv2.medianBlur(_image, 9)
    _image = cv2.GaussianBlur(_image,(_gaussian_kernel_size, _gaussian_kernel_size), -1)
    _image = cv2.GaussianBlur(_image, (9, 9), 0)
    _ret, _image = cv2.threshold( _image, 100, 255, cv2.THRESH_BINARY_INV)
    cv2.imshow("result", _image)
    # cv2.imwrite("constellation_images/formated_cassiopeia.jpg", _image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return None


if __name__ == "__main__":
    image_path = "constellation_images/orion2.webp"
    format_constellation(image_path)
