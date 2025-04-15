import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.signal import find_peaks

# Carica i dati da un file Excel
df = pd.read_excel('natalia-giulia-alu1.xlsx')
# Filtra i dati tra 34 e 44 secondi
df_filtrato = df[(df.iloc[:, 1] >= 36.5) & (df.iloc[:, 1] <= 43)]

# Estrai le colonne x e y filtrate
x = df_filtrato.iloc[:, 1].values
y = df_filtrato.iloc[:, 2].values
# Estrai le colonne x e y

# Applica un offset ai dati
offset_dati = -2.1
y_offset = y + offset_dati

# Trova i massimi locali
indici_picchi, _ = find_peaks(y_offset)

# Plot
plt.figure(figsize=(8, 5))
plt.plot(x, y_offset, label='Tension', color='royalblue')

# Aggiungi punti arancioni sui massimi
plt.plot(x[indici_picchi], y_offset[indici_picchi], 'o', color='orange')
# Etichette e grafico
plt.xlabel('t [s]')
plt.ylabel('U [V]')
plt.legend(loc='upper right')
plt.grid(True)
plt.tight_layout()
plt.show()
