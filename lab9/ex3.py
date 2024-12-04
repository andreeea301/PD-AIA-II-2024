import numpy as np
import matplotlib.pyplot as plt

fs = 200
tf = 1
t = np.linspace(0, tf, int(fs * tf), endpoint=False)
x = 5 * np.sin(2 * np.pi * 5 * t)
x += np.random.uniform(-1, 1, len(x))

coeficienti = [
    [1 / 2, 1 / 2],
    [1 / 3, 1 / 3, 1 / 3],
    [1 / 6, 1 / 6, 1 / 6, 1 / 6, 1 / 6, 1 / 6]
]

plt.figure(figsize=(10, 8))
for i, h in enumerate(coeficienti, 1):
    h = np.array(h)
    y = np.convolve(x, h, mode='same')

    plt.subplot(3, 1, i)
    plt.plot(t, x, label='Semnal x(t)')
    plt.plot(t, y, label=f'Convoluție cu h{i}')
    plt.legend()
    plt.title(f'Convoluție cu h{i}')
    plt.xlabel('Timp [s]')
    plt.ylabel('Amplitudine')
    plt.grid()

plt.tight_layout()
plt.show()
