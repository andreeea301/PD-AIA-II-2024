import numpy as np
import matplotlib.pyplot as plt



time = np.arange(0, 20, 0.1)
temperature_signal = np.random.normal(loc=20, scale=1, size=len(time))  # Temperaturi simulate

plt.figure(figsize=(12, 6))
plt.plot(time, temperature_signal, color='green')
plt.title('Semnalul de temperatura de la al doilea senzor')
plt.xlabel('Timp (s)')
plt.ylabel('Temperatura (°C)')
plt.grid()
plt.show()



plt.figure(figsize=(12, 6)
plt.hist(temperature_signal, bins=20, color='purple', alpha=0.7)
plt.title('Histograma semnalului de temperatura')
plt.xlabel('Temperatura (°C)')
plt.ylabel('Frecventa')
plt.grid()
plt.show()

plt.figure(figsize=(12, 6))
plt.hist(temperature_signal, bins=20, density=True, color='orange', alpha=0.7)
plt.title('Distributia de probabilitate a semnalului de temperatura')
plt.xlabel('Temperatura (°C)')
plt.ylabel('Probabilitate')
plt.grid()
plt.show()



mean_temp = np.mean(temperature_signal)
median_temp = np.median(temperature_signal)
std_temp = np.std(temperature_signal)
min_temp = np.min(temperature_signal)
max_temp = np.max(temperature_signal)

print(f'Media: {mean_temp:.2f} °C')
print(f'Mediana: {median_temp:.2f} °C')
print(f'Abaterea standard: {std_temp:.2f} °C')
print(f'Minimum: {min_temp:.2f} °C')
print(f'Maximum: {max_temp:.2f} °C')


