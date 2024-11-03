import math
import matplotlib.pyplot as plt
import numpy as np


x= np.arange( -5, 5, 0.01)
y1= (x+1)/(x**2-2)
plt.plot(x,y1, "r-")
plt.show()
y2= x* math.log2(x**2)
plt.plot(x,y2, "g--")
plt.show()
