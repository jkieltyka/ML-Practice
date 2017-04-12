import numpy as np
import matplotlib.pyplot as plt
X = np.linspace(-np.pi, np.pi, 256, endpoint=True)
Cos, Sin = np.cos(X), np.sin(X)
plt.plot(X, Sin)
plt.plot(X, Cos)
plt.show()
