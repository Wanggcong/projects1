import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
from PIL import Image


def myprint(img):

    pixel2mat3 = np.array([
        [[255, 255, 255],
         [255, 255, 255],
         [255, 255, 255]],

        [[255, 0, 255],
         [255, 255, 255],
         [255, 255, 255]],

        [[255, 0, 255],
         [255, 255, 255],
         [255, 255, 0]],

        [[0, 0, 255],
         [255, 255, 255],
         [255, 255, 0]],

        [[0, 0, 255],
         [255, 255, 255],
         [0, 255, 0]],

        [[0, 0, 0],
         [255, 255, 255],
         [0, 255, 0]],

        [[0, 0, 0],
         [255, 255, 0],
         [0, 255, 0]],

        [[0, 0, 0],
         [255, 255, 0],
         [0, 0, 0]],

        [[0, 0, 0],
         [0, 255, 0],
         [0, 0, 0]],

        [[0, 0, 0],
         [0, 0, 0],
         [0, 0, 0]],
    ])

# 之前黑色和白色的值写反了。。。
    pixel2mat3 = pixel2mat3[::-1]

    new_map = np.zeros((img.shape[0] * 3, img.shape[1] * 3))

    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            new_map[i * 3:i * 3 + 3, j * 3:j * 3 +
                    3] = pixel2mat3[np.int(img[i, j]) // 26]

    return new_map


greyscale = np.zeros((256, 256)) + range(256)
plt.imshow(greyscale, cmap='gray')
trans = myprint(greyscale)
plt.figure(2)
plt.imshow(trans, cmap='gray')

fig222a = mpimg.imread('Fig2.22(a).jpg')
fig222b = mpimg.imread('Fig2.22(b).jpg')
fig222c = mpimg.imread('Fig2.22(c).jpg')
plt.figure(3)
plt.subplot(121)
plt.imshow(fig222a, cmap='gray')
plt.subplot(122)
plt.imshow(myprint(fig222a), cmap='gray')
plt.figure(4)
plt.subplot(121)
plt.imshow(fig222b, cmap='gray')
plt.subplot(122)
plt.imshow(myprint(fig222b), cmap='gray')
plt.figure(5)
plt.subplot(121)
plt.imshow(fig222c, cmap='gray')
plt.subplot(122)
plt.imshow(myprint(fig222c), cmap='gray')

plt.show()
