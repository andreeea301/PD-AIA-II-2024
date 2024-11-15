import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

fs = 500
t = np.arange(0, 2, 1 / fs)
q = 0.5

x = 6 + (5 * np.sin(2 * np.pi * 2 * t)) / (2 * np.pi * 2 * t)


eșantioane = x

cuantizat = np.round(eșantioane / q) * q

plt.figure(figsize=(12, 6))
plt.subplot(2, 1, 1)
plt.plot(t, eșantioane, label='Esantioane inainte de cuantizare', color='blue')
plt.title('Esantioane inainte de cuantizare')
plt.xlabel('Timp (secunde)')
plt.ylabel('Amplitudine')
plt.grid()
plt.legend()

plt.subplot(2, 1, 2)
plt.step(t, cuantizat, label='Esantioane dupa cuantizare', color='orange', where='post')
plt.title('Esantioane dupa cuantizare')
plt.xlabel('Timp (secunde)')
plt.ylabel('Amplitudine')
plt.grid()
plt.legend()
plt.tight_layout()
plt.show()

plt.figure(figsize=(12, 6))
sns.histplot(cuantizat, bins=20, kde=True)
plt.title('Histograma Esantioanelor si Distributia de Probabilitate')
plt.xlabel('Amplitudine')
plt.ylabel('Frecventa')
plt.grid()
plt.show()

statistici = {
    'Media': np.mean(eșantioane),
    'Mediana': np.median(eșantioane),
    'Deviatia Standard': np.std(eșantioane),
    'Minim': np.min(eșantioane),
    'Maxim': np.max(eșantioane),
    'Varianță': np.var(eșantioane),
    '25% Percentil': np.percentile(eșantioane, 25),
    '75% Percentil': np.percentile(eșantioane, 75)
}

for key, value in statistici.items():
    print(f"{key}: {value:.2f}")