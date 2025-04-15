import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Dati
masse = np.array([0, 0.121, 621.8, 1121.8, 1621.8, 1671.8, 1721.8])  # masse in grammi
err_masse = 15  # errore costante di 0.5 g

hauteur_alu = np.array([0.2, 0.5, 2, 2.8, 4.6, 4.75, 4.9])  # altezze in cm
err_hauteur_alu = np.array([0.3, 0.3, 0.2, 0.4, 0.2, 0.3, 0.2])  # errori sulle altezze

hauteur_acier = np.array([0.2, 1.4, 7.85, 14.9, 20.85, 20.95, 22.45])
err_hauteur_acier = np.array([0.25, 0.35, 0.2, 0.35, 0.25, 0.25, 0.2])

L = 138.5  # lunghezza in cm
dL = 0.5   # errore su L

# Funzione per calcolare theta e l'errore

def calcola_theta(hauteur, err_hauteur):
    theta_rad = hauteur / (2 * L)
    theta_deg = np.degrees(theta_rad)
    err_theta = np.zeros_like(theta_deg)
    for i in range(len(theta_deg)):
        if hauteur[i] != 0:
            err_rel = np.sqrt((err_hauteur[i]/hauteur[i])**2 + (dL/L)**2)
            err_theta[i] = theta_deg[i] * err_rel
    return theta_deg, err_theta

# Calcolo theta e errori
theta_alu, err_theta_alu = calcola_theta(hauteur_alu, err_hauteur_alu)
theta_acier, err_theta_acier = calcola_theta(hauteur_acier, err_hauteur_acier)

# Funzione di fit lineare
def retta(x, a, b):
    return a * x + b

# Fit alluminio
popt_alu, pcov_alu = curve_fit(retta, masse, theta_alu, sigma=err_theta_alu, absolute_sigma=True)
a_alu, b_alu = popt_alu
err_a_alu, err_b_alu = np.sqrt(np.diag(pcov_alu))

# Fit acciaio
popt_acier, pcov_acier = curve_fit(retta, masse, theta_acier, sigma=err_theta_acier, absolute_sigma=True)
a_acier, b_acier = popt_acier
err_a_acier, err_b_acier = np.sqrt(np.diag(pcov_acier))

# Retta del fit
masse_fit = np.linspace(min(masse), max(masse), 500)
theta_fit_alu = retta(masse_fit, a_alu, b_alu)
theta_fit_acier = retta(masse_fit, a_acier, b_acier)

# Plot
plt.figure(figsize=(8, 5))
plt.errorbar(masse, theta_alu, yerr=err_theta_alu, xerr=err_masse, fmt=',', color='orange', label='Aluminium')
plt.plot(masse_fit, theta_fit_alu, 'orange', linestyle='--', label=fr'Fit Alu: $y = (5.4 \pm 0.28)\cdot 10^{{-3}}x + (6.8 \pm 3.7)\cdot 10^{{-2}}$')

plt.errorbar(masse, theta_acier, yerr=err_theta_acier, xerr=err_masse, fmt=',', color='steelblue', label='Acier')
plt.plot(masse_fit, theta_fit_acier, 'steelblue', linestyle='--', label=fr'Fit Acier: $y = (2.6\pm 0.03)\cdot 10^{{-3}}x + (8.2 \pm 3.5)\cdot 10^{{-2}}$')

# Etichette
plt.xlabel(r' $m$ [g]', fontsize=14)
plt.ylabel(r' $\theta$ [deg]', fontsize=14)
plt.ylim(0, 5)
plt.grid(True)
plt.legend(loc='upper left',  fontsize=11)
plt.tight_layout()
plt.show()

# Stampa i risultati
print("\nAlluminio:")
for m, h, t, et in zip(masse, hauteur_alu, theta_alu, err_theta_alu):
    print(f"Massa = {m:7.2f} g | Altezza = {h:4.2f} cm | \u03b8 = {t:.4f} ± {et:.4f} °")

print(f"\nFit Alu: a = ({a_alu:.4e} ± {err_a_alu:.4e}) °/g, b = ({b_alu:.4e} ± {err_b_alu:.4e}) °")

print("\nAcciaio:")
for m, h, t, et in zip(masse, hauteur_acier, theta_acier, err_theta_acier):
    print(f"Massa = {m:7.2f} g | Altezza = {h:4.2f} cm | \u03b8 = {t:.4f} ± {et:.4f} °")

print(f"\nFit Acier: a = ({a_acier:.4e} ± {err_a_acier:.4e}) °/g, b = ({b_acier:.4e} ± {err_b_acier:.4e}) °")


