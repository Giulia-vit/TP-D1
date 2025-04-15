import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Dati
theta_list_alu = np.array([0.51, 0.63702227, 0.73623574, 0.79751465, 0.84511832,
                           0.86834064, 0.93, 0.96954242, 0.99289668, 1.19509805])
distance_alu = np.array([16, 21, 23, 25.5, 29.5, 34.5, 38.5, 40, 42.5, 46.5])
theta_err_alu = np.full_like(theta_list_alu, 0.05)  # esempio: errore costante

theta_list_acier = np.array([2.41404295, 2.61281925, 2.9, 3.07904049, 3.3294904,
                             3.85, 4.1, 4.3, 4.5, 4.9, 5.39])
distance_acier = np.array([17.5, 22, 25.5, 29.5, 34.2, 36.5, 38.6, 40.6, 42.3, 44.5, 46.6])
theta_err_acier = np.full_like(theta_list_acier, 0.05)  # esempio: errore costante

def linear_func(x, a, b):
    return a * x + b

params_acier, _ = curve_fit(linear_func, distance_acier, theta_list_acier)
fit_theta_acier = linear_func(distance_acier, *params_acier)

params_alu, _ = curve_fit(linear_func, distance_alu, theta_list_alu)
fit_theta_alu = linear_func(distance_alu, *params_alu)

plt.errorbar(distance_acier, theta_list_acier, yerr=theta_err_acier, fmt='o', color='steelblue', label='Acier', capsize=4)
plt.plot(distance_acier, fit_theta_acier, '--', color='steelblue', label=f'Fit Acier: y = {params_acier[0]:.2f}x + {params_acier[1]:.2f}')

plt.errorbar(distance_alu, theta_list_alu, yerr=theta_err_alu, fmt='s', color='orange', label='Aluminium', capsize=4)
plt.plot(distance_alu, fit_theta_alu, '--', color='orange', label=f'Fit Alu: y = {params_alu[0]:.2f}x + {params_alu[1]:.2f}')


plt.xlabel(" $l$ [cm]", fontsize = 14)
plt.ylabel(r"$\theta$ [deg]", fontsize = 14)
plt.legend(loc='upper left',  fontsize=11)
plt.ylim(0, 5)
plt.grid(True)
plt.tight_layout()
plt.show()
