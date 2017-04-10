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
print a.sum(axis=0)
print a.sum(axis=1)
print x

#Diffusion random walk
n_stories = 200
t_max = 200

t = np.arange(t_max)
steps = 2 * np.random.random_integers(0, 1, (n_stories, t_max)) - 1

positions = np.cumsum(steps, axis=1)
distance_sq = positions**2
mean_distance = np.mean(distance_sq, axis=0)
plt.plot(t, np.sqrt(mean_distance), 'g.', t, np.sqrt(t), 'y-')
plt.show()
