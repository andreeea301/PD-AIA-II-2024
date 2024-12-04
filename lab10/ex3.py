import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import butter, freqz

fs = 1000
ft1, ft2 = 100, 250
orders = [3, 5, 10]

plt.figure(figsize=(12, 6))

for order in orders:
    b, a = butter(order, [ft1 / (fs / 2), ft2 / (fs / 2)], btype='band')
    w, h = freqz(b, a, worN=8000, fs=fs)

    plt.plot(w, 20 * np.log10(abs(h)), label=f"Ordin {order}")

plt.title("Caracteristica de frecvență pentru filtrele IIR trece-bandă")
plt.xlabel("Frecvență (Hz)")
plt.ylabel("Amplitudine (dB)")
plt.legend()
plt.grid()
plt.tight_layout()
plt.show()



