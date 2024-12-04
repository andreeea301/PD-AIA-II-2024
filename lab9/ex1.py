import numpy as np
import matplotlib.pyplot as plt

fs = 500
tf = 1
t = np.linspace(0, tf, int(fs * tf), endpoint=False)
x = 5 * np.sin(2 * np.pi * 5 * t)
x += np.random.uniform(-1, 1, len(x))

h = 5 * np.sin(2 * np.pi * 5 * t[:int(fs * 0.1)])

corelatie = np.correlate(x, h, mode='valid')
corelatie_normata = corelatie / (np.linalg.norm(x) * np.linalg.norm(h))

prag = 0.98
detectie = corelatie_normata > prag

plt.figure(figsize=(10, 5))
plt.plot(t, x, label='Semnal x(t)')
plt.plot(t[:len(corelatie)], detectie * max(x), label='Detecție (corelație)')
plt.legend()
plt.title('Corelația semnalului')
plt.xlabel('Timp [s]')
plt.ylabel('Amplitudine')
plt.grid()
plt.show()
