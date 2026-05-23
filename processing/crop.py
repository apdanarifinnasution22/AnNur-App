def crop_center(img, percent=0.8):
    h, w = img.shape[:2]
    nh, nw = int(h*percent), int(w*percent)
    y = (h-nh)//2
    x = (w-nw)//2
    return img[y:y+nh, x:x+nw]
