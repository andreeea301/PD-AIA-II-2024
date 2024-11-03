import math
import numpy as np
from matplotlib import pyplot as plt

x = np.arange(0, 8 * np.pi, 0.01)
y3 = math.sin(1.5 * x)
plt.subplot(2, 2, 1)
plt.plot(x, y3)
y4 = math.cos(x / 2)
plt.subplot(2, 2, 2)
plt.plot(x, y4)
