import cv2
import numpy as np
import matplotlib.pyplot as plt

def show_histogram(image):
    """
    Menampilkan histogram citra (Grayscale atau RGB)
    """
    plt.figure("Histogram Citra")

    # Jika gambar grayscale
    if len(image.shape) == 2:
        plt.hist(image.ravel(), 256, [0, 256])
        plt.title("Histogram Grayscale")
        plt.xlabel("Intensitas Pixel")
        plt.ylabel("Jumlah Pixel")

    # Jika gambar RGB
    else:
        colors = ('b', 'g', 'r')
        for i, color in enumerate(colors):
            hist = cv2.calcHist([image], [i], None, [256], [0, 256])
            plt.plot(hist, color=color)
            plt.xlim([0, 256])

        plt.title("Histogram RGB")
        plt.xlabel("Intensitas Pixel")
        plt.ylabel("Jumlah Pixel")

    plt.tight_layout()
    plt.show()
