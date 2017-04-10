#coding=utf-8
import numpy as np

def get_cnts(im, L):
    # 对灰度值进行计数
    row, col = im.shape
    cnts = np.zeros(L)
    for c in range(col):
        for r in range(row):
            gray = im[r, c]
            cnts[gray] += 1
    return cnts

def get_gray(im):
    dim = im.astype(np.int) 
    return ((dim[:,:,0] * 299 + dim[:,:,1] * 587 + dim[:,:,2] * 114 + 500) / 1000).astype(np.uint8)

# 卷积结果不对图像进行标准化, 返回值可以存在负数
def conv2(im, mask):
    dim = im.astype(np.double)
    row, col = im.shape
    mrow, mcol = mask.shape
    hr = mrow // 2
    hc = mcol // 2
    res = np.zeros((row, col))
    ms = {}
    res = np.zeros((row, col))
    for r in range(mrow):
        for c in range(mcol):
            z = mask[r, c]
            if z == 0:
                continue
            if z not in ms:
                ms[z] = dim * z 
            m = ms[z]
            dr = r - hr
            dc = c - hc
            res[max(0, dr):min(row, dr + row), max(0, dc):min(col, dc + col)] += m[max(0, -dr):min(row, row - dr), max(0, -dc):min(col, col - dc)]
    return res

# 标准化为uint8类型
def normal_pic(im):
    tim = np.clip(im, 0, 255)
    return tim.astype(np.uint8)

def dec_pic(a, b):
    return np.clip((a.astype(np.int) - b.astype(np.int)), 0, 255).astype(np.uint8)

def add_pic(a, b):
    return np.clip((a.astype(np.int) + b.astype(np.int)), 0, 255).astype(np.uint8)

if __name__ == "__main__":
    a = np.zeros([10,10])
    a[9,0] = 1
    b = np.array([[1,2,3], [4,5,6], [7,8,9]])
    c = conv(a, b)
    print (c)
