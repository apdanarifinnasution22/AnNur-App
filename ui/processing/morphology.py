import cv2
import numpy as np

def to_gray(img):
    if len(img.shape) == 3:
        return cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    return img

def erosion(img):
    img = to_gray(img)
    return cv2.erode(img, np.ones((3,3),np.uint8))

def dilation(img):
    img = to_gray(img)
    return cv2.dilate(img, np.ones((3,3),np.uint8))

def opening(img):
    img = to_gray(img)
    return cv2.morphologyEx(img, cv2.MORPH_OPEN, np.ones((3,3),np.uint8))

def closing(img):
    img = to_gray(img)
    return cv2.morphologyEx(img, cv2.MORPH_CLOSE, np.ones((3,3),np.uint8))
