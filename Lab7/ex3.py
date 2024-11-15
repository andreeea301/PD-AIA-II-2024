import pandas as pd
import matplotlib.pyplot as plt




df_vf_omu = df1[df1['Station'] == 'Vârfu Omu']


fig, axs = plt.subplots(2, 1, figsize=(10, 8))


axs[0].hist(df_vf_omu['Avg_Temperature'], bins=20, color='blue', alpha=0.7)
axs[0].set_title('Histograma temperaturilor medii la Vârfu Omu')
axs[0].set_xlabel('Temperatura (°C)')
axs[0].set_ylabel('Frecventa')


axs[1].hist(df_vf_omu['Max_Temperature'], bins=20, color='red', alpha=0.7)
axs[1].set_title('Histograma temperaturilor maxime la Vârfu Omu')
axs[1].set_xlabel('Temperatura (°C)')
axs[1].set_ylabel('Frecventa')

plt.tight_layout()
plt.show():




plt.figure(figsize=(12, 6))
df1.boxplot(column='Avg_Temperature', by='Station', grid=False)
plt.title('Boxplot al temperaturilor medii pe statii')
plt.suptitle('')
plt.xlabel('Statie')
plt.ylabel('Temperatura medie (°C)')
plt.show()


