import numpy as np
from scipy import linalg, fftpack, misc, optimize, stats
import pylab as plt
from mpl_toolkits.mplot3d import Axes3D

#test linalg function
a = np.array( [[1, 2], [3, 4]])
b = linalg.det(a)
c = linalg.inv(a)
print np.allclose(c.dot(a), np.eye(2))

#Remove periodic noise from an image
image = plt.imread('../moonlanding.png')

#Clean up an image
result = fftpack.fft2(image)
result[400:,:] = 0
image = fftpack.ifft2(result[:,:]).real
img2 = np.clip(image, 0, 1) #clip to within the correct range
# plt.imshow(img2)
# plt.show()

#curve fitting test
max_temp_data = np.array([17,  19,  21,  28,  33,  38, 37,  37,  31,  23,  19,  18])
min_temp_data = np.array([-62, -59, -56, -46, -32, -18, -9, -13, -25, -46, -52, -58])
time = np.arange(0, 12)
# plt.plot(max_temp_data)
# plt.plot(min_temp_data)


def temp(x, a, b, c):
    return a*np.cos((np.pi/6)*x - c) - b

guess= [20, 40, np.pi]
params, params_covariance = optimize.curve_fit(temp, time, min_temp_data, guess)
# print params
result = temp(time, params[0], params[1], params[2])
# plt.plot(result)
params, params_covariance = optimize.curve_fit(temp, time, max_temp_data, guess)
# print params
result = temp(time, params[0], params[1], params[2])
# plt.plot(result)
# plt.show()


def six_hump(x):
    return (4- 2.1*x[0]**2+ x[0]**4/3)*x[0]**2 + x[0]*x[1] +(4*x[1]**2 - 4)* x[1]**2

x_values = np.arange(-2, 2, 0.05)
y_values = np.arange(-1, 1, 0.05)
xg, yg = np.meshgrid(x_values, y_values)
# plt.imshow(six_hump([xg, yg]))
# plt.colorbar()
# plt.show()

result = optimize.fmin_bfgs(six_hump, [-1.9, 0])
print result

gamma_result = np.random.gamma(1,1,(1000))
bins = np.arange(-4, 5)
histogram = np.histogram(gamma_result, bins=bins, normed=True)[0]
print histogram
bins = 0.5*(bins[1:] + bins[:-1])
pdf_value = stats.norm.pdf(bins)
print pdf_value
plt.plot(bins, histogram)
plt.plot(bins, pdf_value)
plt.show()
