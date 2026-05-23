import cv2
import numpy as np

# =========================
# RGB (IDENTITY)
# =========================
def to_rgb(img):
    if len(img.shape) == 2:
        return cv2.cvtColor(img, cv2.COLOR_GRAY2RGB)
    return img

# =========================
# HSV
# =========================
def to_hsv(img):
    if len(img.shape) == 2:
        img = cv2.cvtColor(img, cv2.COLOR_GRAY2RGB)
    hsv = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)
    return hsv

def hsv_to_rgb(hsv):
    return cv2.cvtColor(hsv, cv2.COLOR_HSV2RGB)

# =========================
# HSI (MANUAL)
# =========================
def to_hsi(img):
    img = img.astype(np.float32) / 255
    R, G, B = img[:,:,0], img[:,:,1], img[:,:,2]

    I = (R + G + B) / 3
    min_rgb = np.minimum(np.minimum(R, G), B)
    S = 1 - (3 / (R + G + B + 1e-6)) * min_rgb

    num = 0.5 * ((R - G) + (R - B))
    den = np.sqrt((R - G)**2 + (R - B)*(G - B)) + 1e-6
    theta = np.arccos(num / den)

    H = np.where(B <= G, theta, 2*np.pi - theta)
    H = H / (2*np.pi)

    hsi = np.dstack((H, S, I))
    return (hsi * 255).astype(np.uint8)

# =========================
# YCbCr
# =========================
def to_ycbcr(img):
    if len(img.shape) == 2:
        img = cv2.cvtColor(img, cv2.COLOR_GRAY2RGB)
    return cv2.cvtColor(img, cv2.COLOR_RGB2YCrCb)

# =========================
# CMYK
# =========================
def to_cmyk(img):
    img = img.astype(float) / 255
    R, G, B = img[:,:,0], img[:,:,1], img[:,:,2]

    K = 1 - np.max(img, axis=2)
    C = (1 - R - K) / (1 - K + 1e-6)
    M = (1 - G - K) / (1 - K + 1e-6)
    Y = (1 - B - K) / (1 - K + 1e-6)

    cmyk = np.dstack((C, M, Y, K))
    return (cmyk[:,:,:3] * 255).astype(np.uint8)
