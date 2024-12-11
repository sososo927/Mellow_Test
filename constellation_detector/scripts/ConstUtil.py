import cv2

class ConstUtil:

    def __init__(self, image_path):
        self.image = self._read_img(image_path)

    def __del__(self):
        pass

    @staticmethod
    def _read_img(image_path):
        return cv2.imread(image_path)

    def _read_img_to_rgb(self, image_path):
        return cv2.cvtColor(self._read_img(image_path), cv2.COLOR_BGR2RGB)

    def _read_img_to_gray(self, image_path):
        return cv2.cvtColor(self._read_img(image_path), cv2.COLOR_BGR2GRAY)

    def median_bluring(self, ksize):
        if ksize % 2 == 0:
            ksize += 1
            print(f"[MET] median_bluring ksize + 1 => {ksize}")