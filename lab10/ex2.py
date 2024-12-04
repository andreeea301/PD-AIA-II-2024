import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import butter, filtfilt, freqz

fs = 1000
t = np.arange(0, 1, 1/fs)
x = 5 * np.sin(2 * np.pi * 5 * t) + np.sin(2 * np.pi * 200 * t) + np.sin(2 * np.pi * 300 * t)
ft = 100
order = 10

b, a = butter(order, ft / (fs / 2), btype='low')
y_iir = filtfilt(b, a, x)
w, h = freqz(b, a, worN=8000, fs=fs)

plt.figure(figsize=(12, 6))

plt.subplot(2, 1, 1)
plt.plot(t, x, label='Semnal inițial')
plt.plot(t, y_iir, label='Semnal filtrat IIR', color='orange')
plt.title("Semnal filtrat cu filtru IIR de ordin 10")
plt.xlabel("Timp (s)")
plt.ylabel("Amplitudine")
plt.legend()

plt.subplot(2, 1, 2)
plt.plot(w, 20 * np.log10(abs(h)), color='orange')
plt.title("Caracteristica de frecvență (filtru IIR de ordin 10)")
plt.xlabel("Frecvență (Hz)")
plt.ylabel("Amplitudine (dB)")
plt.grid()

plt.tight_layout()
plt.show()



