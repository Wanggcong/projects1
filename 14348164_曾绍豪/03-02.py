
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
from PIL import Image

img = mpimg.imread('Fig3.08(a).jpg')
# Display original image
plt.figure(1)
imgplot = plt.imshow(img, cmap='gray')

# Build histogram
count = np.zeros(256, dtype=np.int32)
for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        count[img[i, j]] += 1
plt.figure(2)
plt.bar(left=np.arange(256), height=count)

# Histogram equalization
cumu = np.zeros(256, dtype=np.float64)
cumu[0] = count[0]
for i in range(1, 256):
    cumu[i] += cumu[i - 1] + count[i]
print(cumu[0], cumu[255])
for i in range(0, 256):
    cumu[i] /= cumu[255]
    cumu[i] *= 255
cumu = np.ceil(cumu)

# Perform transformation and show the image
trans = cumu
trans_img = [[trans[pix] for pix in row] for row in img]
plt.figure(3)
plt.imshow(trans_img, cmap='gray')

plt.show()
