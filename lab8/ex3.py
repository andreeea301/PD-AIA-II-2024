import numpy as np
import simpleaudio as sa
from scipy.io.wavfile import write

fs = 48000  # Frecvența de eșantionare (Hz)
T = 1  # Durata semnalului (s)
note_number = 49  # Nota F4 (nota 49 în tabel)

f = 440 * 2 ** ((note_number - 49) / 12)

t = np.linspace(0, T, int(fs * T), endpoint=False)
note = np.sin(2 * np.pi * f * t)

note_int16 = (note * 32767).astype(np.int16)

write("note.wav", fs, note_int16)

print("Redare audio...")
play_obj = sa.play_buffer(note_int16, 1, 2, fs)  # 1 canal, 2 octeți per eșantion, frecvență fs
play_obj.wait_done()
print("Redarea s-a terminat.")



