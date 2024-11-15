import numpy as np
import matplotlib.pyplot as plt
from fontTools.misc.cython import returns

tf=0.1
fs=25
fs2=40
t=np.arange(0, 0.1+1/fs,1/fs)
t2= np.arange(0,0.1+1/fs2,1/fs2)
x=np.arange(0, 2*np.pi ,tf)
y=1*np.sin(2* np.pi*1*t+np.pi/6)
plt.plot(x,y(t), "r:")
plt.show()
