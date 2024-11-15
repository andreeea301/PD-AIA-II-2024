import numpy as np
import matplotlib.pyplot as plt
def interpolate_linear(t,x,tt):
    N=len(t)
    NN=len(tt)
    y=np.zeros((NN,))

    for k in range (0,NN):
        for i in range (0,N-1):
            if(t[i]<=tt[k] and tt[k]<= t[i+1]) or i==N-2:
                y[k]=x[i]+(x[i+1])/(t[i+1]-t[i])*(tt[k]-t[i])
                break
    return y

tf=1
fs1,fs2=5,20
t=np.arange(0,tf,1/fs1)
x=np.sin(2* np.pi*t)
tt= np.arange(0, tf, 1/fs2)
y= interpolate_linear(t,x,tt)
plt.plot(t,x,"*",tt,y,'o')
plt.grid()
plt.legend(["fs1", "fs2"])
plt.show()
