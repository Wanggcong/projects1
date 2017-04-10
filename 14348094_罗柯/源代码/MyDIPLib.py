import matplotlib.pylab as plt
import numpy as np

IMAGE_FOLDER='images'

def calHist(im):
	# calculate and return the histogram of a given image
	histogram = np.zeros((256,), dtype=np.uint32)
	for row in im:
		for pixel in row:
			histogram[pixel] += 1
	return histogram

def histChart(histogram):
	# draw the histogram chart
	plt.bar(np.arange(0, 256), histogram, color='g')

def histEqual(histogram):
	# apply equalization to a histogram and return the mapping
	length = len(histogram)
	acc = np.zeros(length, dtype=np.float32)
	
	acc[0] = histogram[0]
	tot = np.float32(histogram[0])
	for idx in range(1, length):
		acc[idx] = acc[idx - 1] + histogram[idx]
		tot += histogram[idx]
	
	mapping = np.zeros(length, dtype=np.uint8)
	for idx in range(length):
		mapping[idx] = np.uint8(length * (acc[idx] / tot) - 0.5)

	return mapping

def spatialFilter3x3(kernel, im, co=1.):
	# operating convolution on a given image with 3x3 kernel
	kernel = np.array(kernel)
	im = np.array(im)
	new_im = np.zeros(im.shape, dtype=np.uint8)

	ix = im.shape[0]
	iy = im.shape[1]

	for x in range(ix):
		for y in range(iy):
			temp = 0.
			for i in range(-1, 2):
				for j in range(-1, 2):
					if x + i >= 0 and x + i < ix and \
					   y + j >= 0 and y + j < iy:
					   temp += kernel[i + 1, j + 1] * im[x + i, y + j]
			temp *= co
			if temp < 0:
				temp = 0
			elif temp >= 255:
				temp = 255
			new_im[x, y] = np.uint8(temp)

	return new_im

def spatialFilter3x3_(kernel, im, co=1.):
	# unbound version
	# operating convolution on a given image with 3x3 kernel
	kernel = np.array(kernel)
	im = np.array(im)
	new_im = np.zeros(im.shape, dtype=np.int32)

	ix = im.shape[0]
	iy = im.shape[1]

	for x in range(ix):
		for y in range(iy):
			temp = 0.
			for i in range(-1, 2):
				for j in range(-1, 2):
					if x + i >= 0 and x + i < ix and \
					   y + j >= 0 and y + j < iy:
					   temp += kernel[i + 1, j + 1] * im[x + i, y + j]
			temp *= co
			new_im[x, y] = np.int16(temp)

	return new_im

def bound(im):
	# truncate the values out of [0, 255]
	im = np.array(im)
 	ix, iy = im.shape
	for i in range(ix):
		for j in range(iy):
			if im[i, j] < 0:
				im[i, j] = 0
			elif im[i, j] >= 255:
				im[i, j] = 255

	return np.uint8(im)

def halftoning(im):
	im = np.array(im)
	row, col = im.shape
	res = np.zeros((row * 3, col * 3), dtype=np.uint8)
	
	def grayLevel(x, y, level):
		if level >= 1:
			res[x][y + 1] = 1 		# (0, 1)
		if level >= 2:
			res[x + 2][y + 2] = 1	# (2, 2)
		if level >= 3:
			res[x][y] = 1			# (0, 0)
		if level >= 4:
			res[x + 2][y] = 1		# (2, 0)
		if level >= 5:	
			res[x][y + 2] = 1		# (0, 2)
		if level >= 6:
			res[x + 1][y + 2] = 1	# (1, 2)
		if level >= 7:
			res[x + 2][y + 1] = 1	# (2, 1)
		if level >= 8:
			res[x + 1][y] = 1		# (1, 0)
		if level >= 9:
			res[x + 1][y + 1] = 1	# (1, 1)

	for iidx in range(0, row):
		for jidx in range(0, col):
			grayLevel(3*iidx, 3*jidx, 10. * im[iidx][jidx] / 255.)

	return res

def proj0302(image_name='Fig3.08(a).jpg'):
	im1 = plt.imread(IMAGE_FOLDER + '/' + image_name)
	im2 = np.zeros(im1.shape, dtype=np.uint8)
	
	# histogram equalization
	histogram1 = calHist(im1)
	mapping = histEqual(histogram1)
	for row in range(im1.shape[0]):
		for col in range(im1.shape[1]):
			im2[row, col] = mapping[im1[row, col]]
	histogram2 = calHist(im2)

	ax11 = plt.subplot(2, 2, 1)
	ax12 = plt.subplot(2, 2, 2)
	ax21 = plt.subplot(2, 2, 3)
	ax22 = plt.subplot(2, 2, 4)

	plt.sca(ax11)
	plt.title("Original")
	ax11.set_xticks([])
	ax11.set_yticks([])
	plt.imshow(im1, cmap=plt.cm.gray)

	plt.sca(ax12)
	plt.title("Histogram of the Original")
	histChart(histogram1)

	plt.sca(ax21)
	plt.title("Result")
	ax21.set_xticks([])
	ax21.set_yticks([])
	plt.imshow(im2, cmap=plt.cm.gray)

	plt.sca(ax22)
	plt.title("Histogram of the Result")
	histChart(histogram2)

	plt.subplots_adjust(0.125, 0.1, 0.9, 0.9, 0.4, 0.4)
	plt.savefig('proj0302.png', dpi=600, cmap=plt.cm.gray)
	plt.show()

def proj0305(image_name='Fig3.40(a).jpg'):
	im = plt.imread(IMAGE_FOLDER + '/' + image_name)

	# Laplacian Enhancement
	kernel = np.array(
		[[-1, -1, -1],
		 [-1, 9, -1],
		 [-1, -1, -1]]
	)
	new_im = spatialFilter3x3(kernel, im)

	ax11 = plt.subplot(1, 2, 1)
	ax11.set_xticks([])
	ax11.set_yticks([])
	ax12 = plt.subplot(1, 2, 2)
	ax12.set_xticks([])
	ax12.set_yticks([])

	plt.sca(ax11)
	plt.title('Original')
	plt.imshow(im, cmap=plt.cm.gray)

	plt.sca(ax12)
	plt.title('Result')
	plt.imshow(new_im, cmap=plt.cm.gray)

	plt.subplots_adjust(0.125, 0.1, 0.9, 0.9, 0.4, 0.4)
	plt.savefig('proj0305.png', dpi=600, cmap=plt.cm.gray)
	plt.show()

def proj0306(image_name='Fig3.43(a).jpg'):
	im = plt.imread(IMAGE_FOLDER + '/' + image_name)
	A = input()

	avgKernel = np.array(
		[[1, 1, 1],
		 [1, 1, 1],
		 [1, 1, 1]])
	co = 1. / 9.

	avg_im = spatialFilter3x3_(avgKernel, im, co)

	lapKernel = np.array(
		[[-1, -1, -1],
		 [-1, A + 8, -1],
		 [-1, -1, -1]])
	lap_im = spatialFilter3x3_(lapKernel, im)

	res_im = bound(np.int16(lap_im))

	ax11 = plt.subplot(1, 2, 1)
	ax11.set_xticks([])
	ax11.set_yticks([])

	ax12 = plt.subplot(1, 2, 2)
	ax12.set_xticks([])
	ax12.set_yticks([])

	plt.sca(ax11)
	plt.title('Original')
	plt.imshow(im, cmap=plt.cm.gray)

	plt.sca(ax12)
	plt.title('Result with A=' + str(A))
	plt.imshow(res_im, cmap=plt.cm.gray)


	plt.subplots_adjust(0.125, 0.1, 0.9, 0.9, 0.4, 0.4)
	plt.savefig('proj0306_'+str(A)+'.png', dpi=600, cmap=plt.cm.gray)
	plt.show()

def proj0201(image_name='Fig2.22(a).jpg', image=None):
	if not image == None:
		im = image
		image_name = ''
	else:
		im = plt.imread(IMAGE_FOLDER + '/' + image_name)

	res = halftoning(im)

	ax11 = plt.subplot(1, 2, 1)
	ax11.set_xticks([])
	ax11.set_yticks([])

	ax12 = plt.subplot(1, 2, 2)
	ax12.set_xticks([])
	ax12.set_yticks([])

	plt.sca(ax11)
	plt.title('Original')
	plt.imshow(im, cmap=plt.cm.gray)

	plt.sca(ax12)
	plt.title('Halftoning')
	plt.axis('off')
	plt.imshow(res, cmap=plt.cm.gray, interpolation='none')

	plt.subplots_adjust(0.125, 0.1, 0.9, 0.9, 0.4, 0.4)
	plt.savefig('proj0201_'+image_name+'.png', dpi=1200, cmap=plt.cm.gray)
	plt.show()

def genPic(n=256):
	im = np.zeros((n, n), dtype=np.uint8)
	for col in range(n):
		for row in range(n):
			im[row][col] = col

	return im
