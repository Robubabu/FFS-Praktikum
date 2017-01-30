import matplotlib.pyplot as plt
import numpy as np
import uncertainties.unumpy as unp
from scipy.optimize import curve_fit
from uncertainties import correlated_values, correlation_matrix
from uncertainties import ufloat
from uncertainties.unumpy import (nominal_values as noms, std_devs as stds)

t, T1, T2, pa, pb, P = np.genfromtxt('../Werte/Werte.txt', unpack = True)
T1 = T1+273.15
T2 = T2+273.15
tp = t[0:15]
tm = t[15:20]
T2p = T2[0:15]
T2m = T2[15:20]

R = ufloat(8.31451,0.00007)

def f(x, a, b):
    return a*x + b
params, cov = curve_fit(f, 1/T1, np.log(pb))
print(params, np.sqrt(np.diag(cov)))
plt.plot(1/T1, np.log(pb), 'kx', label = r'$p_B$')
plt.plot(1/T1, f(1/T1,*params), 'g-', label = 'fit')

print('L = ', a*R)

plt.grid()

plt.xlabel(r'$1/T_1 \:/\: K^{-1}$')
plt.ylabel(r'$ln(p/bar)$')
plt.legend(loc='best')
plt.savefig('Druck.pdf')
