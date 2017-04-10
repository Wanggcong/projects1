#coding=utf-8

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
from scipy.misc import imread, imresize, imsave
from base import * 

dots_raw = np.matrix([[0,0,0,0,0,0,0,0,0],
                      [0,1,0,0,0,0,0,0,0],
                      [0,1,0,0,0,0,0,0,1],
                      [1,1,0,0,0,0,0,0,1],
                      [1,1,0,0,0,0,1,0,1],
                      [1,1,1,0,0,0,1,0,1],
                      [1,1,1,0,0,1,1,0,1],
                      [1,1,1,0,0,1,1,1,1],
                      [1,1,1,1,0,1,1,1,1],
                      [1,1,1,1,1,1,1,1,1]]).astype(np.uint8)

dots = [dots_raw[i,:].reshape(3,3) for i in range(10)]

def halftoning(im, w, h):
    row, col = im.shape
    r1 = (h / 3.0) * 1.0 / row 
    r2 = (w / 3.0) * 1.0 / col
    r = min(r1, r2)
    nw = int(r * col)
    nh = int(r * row)
    # 缩放后的图像
    sim = imresize(im, (nh, nw))
    # scale gray level
    g = np.clip(np.round(sim / (25.5)), 0, 9).astype(np.int)
    res = np.zeros((nh * 3, nw * 3)).astype(np.uint8)
    for r in range(nh):
        for c in range(nw):
            sr = r * 3
            sc = c * 3
            res[sr:sr+3,sc:sc+3] = dots[g[r,c]]
    return (res * 255).astype(np.uint8)



dpi = 96
w = int(round(8.5 * dpi))
h = int(round(11 * dpi))
print (w, h)

plt.subplot(1,2,1)
im = np.tile(range(256), (256,1)).astype(np.uint8)
plt.imshow(im, "gray")
plt.subplot(1,2,2)
ht = halftoning(im, w , h)
plt.imshow(ht, "gray")
plt.show()

imsave("halftoning.jpg", ht)

def halftoning_p(filename):
    im = mpimg.imread(filename)
    plt.subplot(1,2,1)
    plt.imshow(im, "gray")
    plt.subplot(1,2,2)
    ht = halftoning(im, w , h)
    plt.imshow(ht, "gray")
    plt.show()
    imsave("halftoning_%s" % filename.split('/')[-1], ht)

for c in ['a','b','c']:
    filename = "pic/Fig2.22(%c).jpg" % c
    print ("open %s" % filename)
    halftoning_p(filename)
