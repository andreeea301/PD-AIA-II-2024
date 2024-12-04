import numpy as np
import matplotlib.pyplot as plt


fs = 100
T = 50
t = np.arange(0, T, 1/fs)

x_t = 25 + 10 * np.sin(2 * np.pi * t * 5) + 2 * np.sin(2 * np.pi * t * 20 + np.pi / 4)

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
plt.stem(frequencies[:len(frequencies)//2], magnitude[:len(magnitude)//2], basefmt=" ", use_line_collection=True)
plt.title("Reprezentarea semnalului x(t) în domeniul frecvență")
plt.xlabel("Frecvență (Hz)")
plt.ylabel("Amplitudine")
plt.grid()
plt.show()
