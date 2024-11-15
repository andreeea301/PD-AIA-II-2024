import numpy as np
import matplotlib.pyplot as plt




time_sensor1 = np.arange(0, 90, 0.1)  # 90 de secunde
temperature_signal_sensor1 = np.random.normal(loc=60, scale=5,
                                              size=len(time_sensor1))  # Temperaturi simulate cu incalzitorul setat


plt.figure(figsize=(12, 6)
plt.plot(time_sensor1, temperature_signal_sensor1, color='blue')
plt.title('Semnalul de temperatura de la primul senzor')
plt.xlabel('Timp (s)')
plt.ylabel('Temperatura (°C)')
plt.grid()
plt.show()


plt.figure(figsize=(12, 6))
plt.hist(temperature_signal_sensor1, bins=20, color='red', alpha=0.7)
plt.title('Histograma semnalului de temperatura de la primul senzor')
plt.xlabel('Temperatura (°C)')
plt.ylabel('Frecventa')
plt.grid()
plt.show()


plt.figure(figsize=(12, 6))
plt.hist(temperature_signal_sensor1, bins=20, density=True, color='green', alpha=0.7)
plt.title('Distributia de probabilitate a semnalului de temperatura de la primul senzor')
plt.xlabel('Temperatura (°C)')
plt.ylabel('Probabilitate')
plt.grid()
plt.show()


statistici = {
    'Media': np.mean(temperaturi),
    'Mediana': np.median(temperaturi),
    'Deviatia Standard': np.std(temperaturi),
    'Minim': np.min(temperaturi),
    'Maxim': np.max(temperaturi),
    'Variante': np.var(temperaturi),
    '25% Percentil': np.percentile(temperaturi, 25),
    '75% Percentil': np.percentile(temperaturi, 75



for key, value in statistici.items():
    print(f"{key}: {value:.2f}")


