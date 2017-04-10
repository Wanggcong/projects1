import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from PIL import Image

A = 2.6


def Unsharp(img):
    mask = np.array([[1, 1, 1], [1, 1, 1], [1, 1, 1]])
    trans_img = np.zeros(img.shape)
    pad_img = np.lib.pad(img, (1, 1), 'constant', constant_values=0)
    for i in range(1, pad_img.shape[0] - 1):
        for j in range(1, pad_img.shape[1] - 1):
            acc = A * img[i - 1, j - 1] - \
                np.sum(pad_img[i - 1:i + 2, j - 1:j + 2] * mask) / 9
            if acc < 0:
                trans_img[i - 1, j - 1] = 0
            elif acc > 255:
                trans_img[i - 1, j - 1] = 255
            else:
                trans_img[i - 1, j - 1] = acc
    return trans_img


img = mpimg.imread('Fig3.43(a).jpg')
plt.imshow(img, cmap='gray')
plt.figure(2)
trans = Unsharp(img)
plt.imshow(trans, cmap='gray')
plt.show()
