import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import firwin, lfilter, freqz

fs = 1000
t = np.arange(0, 1, 1/fs)
x = 5 * np.sin(2 * np.pi * 5 * t) + np.sin(2 * np.pi * 200 * t) + np.sin(2 * np.pi * 300 * t)
ft = 100
coefficients = [11, 51, 101]

plt.figure(figsize=(15, 10))
for i, num_coef in enumerate(coefficients):
    fir_coeff = firwin(num_coef, ft/(fs/2), pass_zero=True)
    y = lfilter(fir_coeff, 1, x)
    w, h = freqz(fir_coeff, worN=8000, fs=fs)

    plt.subplot(len(coefficients), 2, 2*i+1)
    plt.plot(t, x, label='Semnal inițial')
    plt.plot(t, y, label='Semnal filtrat')
    plt.title(f"Semnal filtrat cu {num_coef} coeficienți")
    plt.xlabel("Timp (s)")
    plt.ylabel("Amplitudine")
    plt.legend()

    plt.subplot(len(coefficients), 2, 2*i+2)
    plt.plot(w, 20 * np.log10(abs(h)))
    plt.title(f"Caracteristica de frecvență ({num_coef} coeficienți)")
    plt.xlabel("Frecvență (Hz)")
    plt.ylabel("Amplitudine (dB)")
    plt.grid()

plt.tight_layout()
plt.show()
