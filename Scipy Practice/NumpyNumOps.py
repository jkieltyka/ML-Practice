import numpy as np
import matplotlib.pyplot as plt
'''
Practice the use of numpy array numerical operations
'''

#transpose
a = np.triu(np.ones((3, 3)), 1)
print a.T

#element sum
x = np.sum(a)
# print a.sum(axis=0)
# print a.sum(axis=1)
# print x

#Diffusion random walk
n_stories = 200
t_max = 200

t = np.arange(t_max)
steps = 2 * np.random.random_integers(0, 1, (n_stories, t_max)) - 1

positions = np.cumsum(steps, axis=1)
distance_sq = positions**2
mean_distance = np.mean(distance_sq, axis=0)
plt.plot(t, np.sqrt(mean_distance), 'g.', t, np.sqrt(t), 'y-')
#plt.show()

#shape maniputlaction
a = np.array([[1, 2, 3], [4, 5, 6]])
# print a
b = a.ravel() # flattens array
c = b.reshape((2, 3))
# print b
# print c

#dimension shuffling/resizing
a = np.arange(4*2).reshape(4, 2)
# print a
# print b.flatten()
# print a
# print c.ravel()
# print a

a = np.array([[3, 6, 7], [2, 1, 4]])
b = np.sort(a, axis=1)
print b
j = np.argsort(a)
print j
print np.concatenate((a[0, :][j[0, :]], a[1, :][j[1, :]])).reshape(2,3)

#Test Polynomial functions
p = np.poly1d([4,3,2])
print p.roots
