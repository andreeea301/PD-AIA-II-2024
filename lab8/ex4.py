import numpy as np
import matplotlib.pyplot as plt
from scipy.io.wavfile import write
from scipy.signal import spectrogram

fs = 48000
T = 1
notes = ['C4', 'D4', 'E4', 'F4', 'G4', 'A4', 'B4']
frequencies = [261.63, 293.66, 329.63, 349.23, 392.00, 440.00, 493.88]

t = np.linspace(0, T, int(fs * T), endpoint=False)
signal = np.array([])

for f in frequencies:
    note = np.sin(2 * np.pi * f * t)
    signal = np.concatenate((signal, note))

write("melody.wav", fs, (signal * 32767).astype(np.int16))

plt.figure(figsize=(12, 6))
plt.plot(np.linspace(0, T * len(notes), len(signal)), signal)
plt.title("Secvența de note (în domeniul timp)")
plt.xlabel("Timp (s)")
plt.ylabel("Amplitudine")
plt.grid()
plt.show()

f, t_spec, Sxx = spectrogram(signal, fs, nperseg=int(0.5 * fs))

plt.figure(figsize=(12, 6))
plt.pcolormesh(t_spec, f, 10 * np.log10(Sxx), shading='auto')
plt.title("Spectrograma secvenței de note")
plt.xlabel("Timp (s)")
plt.ylabel("Frecvență (Hz)")
plt.colorbar(label="Intensitate (dB)")
plt.grid()
plt.show()
