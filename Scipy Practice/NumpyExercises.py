import numpy as np
from scipy import misc
import pylab as plt
a = np.arange(1,16).reshape(3,5).T
b = a[1:4:2,:]
#print a
#print b

a = np.arange(25).reshape(5, 5)
b = np.array([1., 5, 10, 15, 20])

# print a
# print a / b[:, np.newaxis]

#find closest value to 0.5 in each row
a = np.random.rand(30).reshape(10, 3)
# print a
persistent = a.copy()
b = np.abs(a - 0.5)
order = np.argsort(b)
i = np.arange(10)[:, np.newaxis]
# print persistent[i, order[:,0][:, np.newaxis]]

#try creating mask around image
face = misc.face(gray=True)
crop_face = face[100:-100,100:-100]
sy, sx = crop_face.shape
y, x = np.ogrid[0:sy, 0:sx]
centrex, centrey = (550,230)
mask = (1.5*(y - centrey)**2 + (x - centrex)**2) > 230**2
crop_face[mask] = 0
plt.imshow(crop_face, cmap=plt.cm.gray)
# plt.show()

data = np.loadtxt('../populations.txt')
year, hares, lynxes, carrots = data.T  # trick: columns to variables
# print hares.mean(axis=0)
# print hares.std(axis=0)
# print lynxes.mean(axis=0)
# print lynxes.std(axis=0)
# print carrots.mean(axis=0)
# print carrots.std(axis=0)

j = np.argmax(data[:, 1:], axis=1)
species = np.array(['H', 'L', 'C'])
# print species[j]
# print year[np.any(data[:, 1:]>50000, axis=1)]

j = np.argsort(data[:, 1:].T, axis=1)
# print 'Hares: ' + str(year[j[0, 0]]) + ',' + str(year[j[0, 1]])
# print 'Lynxes: ' + str(year[j[1, 0]]) + ',' + str(year[j[1, 1]])
# print 'Carrots: ' + str(year[j[2, 0]]) + ',' + str(year[j[2, 1]])
# print np.gradient(hares)

def f(a, b, c):
    return a**b - c
a = np.linspace(0, 1, 24)
b = np.linspace(0, 1, 12)
c = np.linspace(0, 1, 6)
result = f(a[:, np.newaxis, np.newaxis],
            b[np.newaxis, :, np.newaxis],
            c[np.newaxis, np.newaxis, :])
# print np.mean(result)

def markov(steps = 50):
    '''
    Defines the calculation of a random stae
    '''
    size = 5
    steps = 50
    tolerance = 1e-5
    position = np.random.rand(size)
    position /= position.sum(axis=0)
    rand_matrix = np.random.rand(size, size)
    rand_matrix /= rand_matrix.sum(axis=1)[:, np.newaxis]
    for i in range(steps):
        position = rand_matrix.T.dot(position)
    print position
    w, v = np.linalg.eig(rand_matrix.T)
    j_stationary = np.argmin(abs(w - 1.0))
    p_stationary = v[:,j_stationary].real
    p_stationary /= p_stationary.sum()
    print p_stationary

    if all(abs(position - p_stationary) < tolerance):
        print "Tolerance satisfied"
markov()
