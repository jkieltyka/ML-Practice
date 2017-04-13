import numpy as np
import matplotlib.pyplot as plt
X = np.linspace(-np.pi, np.pi, 256, endpoint=True)
Cos, Sin = np.cos(X), np.sin(X)
# create figure
plt.figure(figsize=(8, 8), dpi=80)
ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data',0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data',0))
plt.plot(X, Sin, color="blue", linestyle="--", label="sine")
plt.plot(X, Cos, color="red", linestyle="-", label="cosine")
plt.legend(loc='upper left')

plt.show()
