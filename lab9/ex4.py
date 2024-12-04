import numpy as np
import matplotlib.pyplot as plt
import scipy.io as sio

fs = 100
tf = 10
t = np.linspace(0, tf, int(fs * tf), endpoint=False)
x = t**3 - 8 * t**2 - 3 * t - 4

dx = np.gradient(x, t)

h = [1/3, 1/3, 1/3]
h = np.array(h)

y = np.convolve(x, h, mode='same')

plt.figure(figsize=(10, 6))

plt.subplot(2, 1, 1)
plt.plot(t, x, label='Semnal x(t)')
plt.plot(t, y, label='Convoluție cu h')
plt.legend()
plt.title('Semnalul și convoluția')
plt.xlabel('Timp [s]')
plt.ylabel('Amplitudine')
plt.grid()

plt.subplot(2, 1, 2)
plt.plot(t, dx, label='Derivata semnalului')
plt.legend()
plt.title('Derivata semnalului')
plt.xlabel('Timp [s]')
plt.ylabel('Amplitudine')
plt.grid()

plt.tight_layout()
plt.show()
