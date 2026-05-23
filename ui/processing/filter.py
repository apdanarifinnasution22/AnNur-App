import cv2

def grayscale(img):
    if len(img.shape) == 2:
        return img
    return cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

def blur(img):
    return cv2.GaussianBlur(img, (7,7), 0)

def edge(img):
    if len(img.shape) == 3:
        img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    return cv2.Canny(img, 100, 200)
