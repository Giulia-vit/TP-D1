import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Carica i dati da un file Excel, saltando le righe iniziali
df = pd.read_excel('natalia-giulia2-alu.xlsx')

# Estrai le colonne x e y
x = df.iloc[:, 0].values
y = df.iloc[:, 1].values

# Parametri del fit esponenziale
A = 8.2
A_err = 0.2
B = -28.9e-3
B_err = 0.9e-3
C = -2.5  # <-- OFFSET VERTICALE (modifica questo valore a piacere)

offset_dati = 0.5  # <-- modifica qui per traslare i dati
y_offset = y + offset_dati

# Funzione esponenziale con offset
def modello(x, A, B, C):
    return A * np.exp(B * x) + C

# Genera la curva del fit
x_fit = np.linspace(min(x), max(x), 500)
y_fit = modello(x_fit, A, B, C)

# Plot
plt.figure(figsize=(8, 5))
plt.plot(x, y_offset, label='Tension', color='royalblue')
plt.plot(x_fit, y_fit, label=(
    fr'Fit: $y = ({A:.1f} \pm {A_err:.1f}) \cdot e^{{({B*1e3:.1f} \pm {B_err*1e3:.1f}) \cdot 10^{{-3}} x}} + {C:.1f}$'
), color='red')

# Mostra le incertezze in legenda o nel titolo
plt.xlabel('t [s]')
plt.ylabel('U [V]')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
