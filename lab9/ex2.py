from scipy.io import loadmat
import numpy as np
import matplotlib.pyplot as plt

try:
    data = loadmat('ekg.mat')
    tf = data['tf'][0][0]
    fs = data['fs'][0][0]
    t = data['t'].flatten()
    x = data['x'].flatten()
    h = data['h'].flatten()

    corelatie = np.correlate(x, h, mode='valid')
    corelatie_normata = corelatie / (np.linalg.norm(x) * np.linalg.norm(h))

    prag = 0.98
    detectie = corelatie_normata > prag

    plt.figure(figsize=(10, 5))
    plt.plot(t, x, label='Semnal EKG')
    plt.plot(t[:len(corelatie)], detectie * max(x), label='Detecție (corelație)')
    plt.legend()
    plt.title('Identificarea bătăilor inimii folosind corelația')
    plt.xlabel('Timp [s]')
    plt.ylabel('Amplitudine')
    plt.grid()
    plt.show()


