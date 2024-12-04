import numpy as np
import matplotlib.pyplot as plt

fs = 1000
T = 1
t = np.linspace(0.01, T, int(fs * T), endpoint=False)

x_t = np.sin(2 * np.pi * t * 20) / (1 - t)

plt.figure(figsize=(12, 6))
plt.plot(t, x_t, label="x(t)")
plt.title("Reprezentarea semnalului x(t) în domeniul timp")
plt.xlabel("Timp (s)")
plt.ylabel("Amplitudine")
plt.grid()
plt.legend()
plt.show()

X_f = np.fft.fft(x_t)
frequencies = np.fft.fftfreq(len(t), 1/fs)

magnitude = np.abs(X_f) / len(t)

plt.figure(figsize=(12, 6))
plt.st

