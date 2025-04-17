import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.signal import find_peaks
plt.rc('font',family='serif')

# Carica i dati da un file Excel
df = pd.read_excel('period_acier.xlsx', engine='openpyxl')

# Estrai le colonne x e y
x = df.iloc[:, 0].values
y = df.iloc[:, 1].values

# Applica un offset ai dati
offset_dati = 1.8
y_offset = y + offset_dati

# Trova i massimi locali
indici_picchi, _ = find_peaks(y_offset)

# Plot
plt.figure(figsize=(8, 5))
plt.plot(x, y_offset, label='Tension', color='royalblue')

# Aggiungi punti arancioni sui massimi
plt.plot(x[indici_picchi], y_offset[indici_picchi], 'o', color='red')
# Etichette e grafico4
plt.tick_params(axis='both', labelsize=14)
plt.xlabel('t [s]', fontsize=15)
plt.ylabel('U [V]', fontsize=15)
plt.savefig('l_varie_m_fixe.png')
plt.legend(fontsize=15, loc='lower right')
plt.grid(True)
plt.tight_layout()
plt.savefig('period_acier.png')
plt.show()

print(df.head())     # prime righe
print(df.tail())     # ultime righe
