#coding=utf-8

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
from base import *

m4 = np.matrix([[0,1,0],[1,-4,1],[0,1,0]])
m8 = np.matrix([[1,1,1],[1,-8,1],[1,1,1]])

# 平滑图像卷积核
msn = 3
ms = np.ones((msn,msn)) / (msn * msn) 

im = mpimg.imread("pic/Fig3.43(a).jpg")
# 平滑后的图像
mf = normal_pic(conv2(im, ms))
fs = dec_pic(im, mf)

plt.subplot(1,3,1)
plt.title("source")
plt.imshow(im, "gray")
plt.subplot(1,3,2)
plt.title("smooth")
plt.imshow(mf, "gray")
plt.subplot(1,3,3)
plt.title("fs")
plt.imshow(fs, "gray")

plt.show()

def High_Boost_filter(im, A, c):
    fhb = A * im.astype(np.double) - conv2(im, c)
    return normal_pic(fhb)
def Unsharp_Mark_filter(im, A, blur):
    fhb = A * im.astype(np.double) - blur 
    return normal_pic(fhb)

fhb0 = High_Boost_filter(im, 0, m4)
fhb1 = High_Boost_filter(im, 1, m4)
fhb1_7 = High_Boost_filter(im, 1.7, m4)

fhb80 = High_Boost_filter(im, 0, m8)
fhb81 = High_Boost_filter(im, 1, m8)
fhb81_7 = High_Boost_filter(im, 1.7, m8)

plt.subplot(2, 4, 1)
plt.title("source")
plt.imshow(im, "gray")

plt.subplot(2, 4, 2)
plt.title("A = 0 (m4)")
plt.imshow(fhb0, "gray")

plt.subplot(2, 4, 3)
plt.title("A = 1 (m4)")
plt.imshow(fhb1, "gray")

plt.subplot(2, 4, 4)
plt.title("A = 1.7 (m4)")
plt.imshow(fhb1_7, "gray")

plt.subplot(2, 4, 5)
plt.title("fs")
plt.imshow(fs, "gray")

plt.subplot(2, 4, 6)
plt.title("A = 0 (m8)")
plt.imshow(fhb80, "gray")

plt.subplot(2, 4, 7)
plt.title("A = 1 (m8)")
plt.imshow(fhb81, "gray")

plt.subplot(2, 4, 8)
plt.title("A = 1.7 (m8)")
plt.imshow(fhb81_7, "gray")

plt.show()

plt.subplot(4, 4, 1)
plt.title("source")
plt.imshow(im,"gray")

for i in range(15):
    print ("compute: #%d / 15" % (i + 1))
    plt.subplot(4, 4, i + 2)
    u = i * 0.3
    plt.title("A = %.2f (fs)" % u)
    hb = Unsharp_Mark_filter(im, u, mf)
    plt.imshow(hb, "gray")
plt.show()


