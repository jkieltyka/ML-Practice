import numpy as np
import matplotlib.pyplot as plt

'''
Practice Numpy Arr functions
'''

# compare length methods
a = np.array([[0, 1, 2], [3, 4, 5]])
print a.shape
print a.ndim
print len(a)

# Compare array constructors
a = np.arange(10)
b = np.linspace(0, 1, 6) #like matlab linspace
c = np.ones((3, 3)) #same as MATLAB ones can create zeros as well
d = np.eye(3) #Creates a nxn identity matrix
e = np.diag(np.array([1, 2, 3, 4, 5]))

print a
print b
print c
print d
print e

# Create a random array
a = np.random.randn(4) # creates a random array of 4 values in a Gaussian Distributiom
print a

# Setting the Data Type
a = np.array([1, 2, 3], dtype=float)
print a
print a.dtype

#1d plot using matlab lib
x = np.linspace(0, 6, 20)
y = np.cos(x)
#plt.plot(x,y)
#plt.show()

# Slicing and indexing Practice
a = np.arange(9)
b = a[0:8:2]
c = a[1:8:2]
c = c[::-1]

print b
print c

#Array Creating
a = np.ones((4, 4))
a[3, 1] = 6
print a

a = np.array([[4, 3], [2, 1], [4, 3], [2, 1]])
a = np.tile(a, 3)
print a

# Testing memory
a = np.arange(10)
b = a[::2]
print np.may_share_memory(a, b)
c = a[::2].copy()
print np.may_share_memory(a, c)
