from PIL import Image
import time
import numpy as np
import matplotlib.image as mpimg
import matplotlib.pyplot as plt


def Laplace(img):
    mask = np.array([[-1, -1, -1], [-1, 8, -1], [-1, -1, -1]])
    trans_img = np.zeros(img.shape)
    pad_img = np.lib.pad(img, (1, 1), 'constant', constant_values=0)
    for i in range(1, img.shape[0] - 1):
        for j in range(1, img.shape[1] - 1):
            sum1 = np.sum(img[i - 1:i + 2, j - 1:j + 2] * mask)
            if sum1 > 255:
                trans_img[i, j] = 255
            elif sum1 < 0:
                trans_img[i, j] = 0
            else:
                trans_img[i, j] = sum1
    return trans_img


img = mpimg.imread('Fig3.40(a).jpg')
plt.imshow(img, cmap='gray')
trans = Laplace(img)
plt.figure(2)
plt.imshow(trans, cmap='gray')
plt.figure(3)
plt.imshow(img + trans, cmap='gray')
plt.show()
