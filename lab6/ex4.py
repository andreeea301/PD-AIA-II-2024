import numpy as np
import matplotlib.pyplot as plt

    tf=2
    fs=1
    t=np.arange(0,tf,1/fs)
    x=10*np.sin(2*np.pi*t*5+(np.pi/3))
    q=2
    x=np.round(x/q)*q
    xc= np.floor(x / q) * q
    plt.plot(t,x,"*")
    plt.grid()
    plt.show()