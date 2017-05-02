import matplotlib.pyplot as plt
import numpy as np
import uncertainties.unumpy as unp
from scipy.optimize import curve_fit
from uncertainties import correlated_values, correlation_matrix
from uncertainties import ufloat
from uncertainties.unumpy import (nominal_values as noms, std_devs as stds)

Z = np.array([30, 32, 35, 38, 40])
E = np.array([9.5,11.0,13.5,16.0,18.0])


def f (x, a, b):
    return a*x +b

params, cov = curve_fit(f,Z**2, E*1000)



plt.plot(Z**2, E, 'kx', label = 'Messwerte')
plt.plot(Z**2, f(Z**2, *params)/1000, 'k-', label = 'Fit')

params = correlated_values(params, cov)

print(params)

plt.grid()
plt.xlabel(r'$Z^2$')
plt.ylabel(r'$E/\mathrm{keV}$')
plt.legend()
plt.savefig('Mosley.pdf')
