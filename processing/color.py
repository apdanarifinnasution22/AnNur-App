import cv2

def adjust_brightness(img, value):
    return cv2.convertScaleAbs(img, alpha=1, beta=value)

def adjust_contrast(img, value):
    alpha = max(value / 50, 0.1)
    return cv2.convertScaleAbs(img, alpha=alpha, beta=0)
