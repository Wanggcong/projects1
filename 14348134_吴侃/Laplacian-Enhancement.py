#coding=utf-8

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
from base import *

m4 = np.matrix([[0,1,0],[1,-4,1],[0,1,0]])
m8 = np.matrix([[1,1,1],[1,-8,1],[1,1,1]])

im = mpimg.imread("pic/Fig3.40(a).jpg")
d4 = normal_pic(conv2(im, m4))
d8 = normal_pic(conv2(im, m8))
im4 = dec_pic(im, conv2(im, m4))
im8 = dec_pic(im, conv2(im, m8))

plt.subplot(2, 3, 1)
plt.title("source")
plt.imshow(im, "gray")

plt.subplot(2, 3, 2)
plt.title("m4")
plt.imshow(im4, "gray")

plt.subplot(2, 3, 3)
plt.title("m8")
plt.imshow(im8, "gray")

plt.subplot(2, 3, 5)
plt.imshow(d4, "gray")
plt.subplot(2, 3, 6)
plt.imshow(d8, "gray")

plt.show()
