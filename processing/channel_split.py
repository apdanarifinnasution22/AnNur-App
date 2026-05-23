import numpy as np

def channel_r(img):
    r = img[:, :, 0]
    zero = np.zeros_like(r)
    return np.stack((r, zero, zero), axis=-1)

def channel_g(img):
    g = img[:, :, 1]
    zero = np.zeros_like(g)
    return np.stack((zero, g, zero), axis=-1)

def channel_b(img):
    b = img[:, :, 2]
    zero = np.zeros_like(b)
    return np.stack((zero, zero, b), axis=-1)
