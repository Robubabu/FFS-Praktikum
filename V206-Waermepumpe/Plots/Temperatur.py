import matplotlib.pyplot as plt
import numpy as np
import uncertainties.unumpy as unp
from scipy.optimize import curve_fit
from uncertainties import correlated_values, correlation_matrix
from uncertainties import ufloat
from uncertainties.unumpy import (nominal_values as noms, std_devs as stds)

t, T1, T2, pa, pb, P = np.genfromtxt('../Werte/Werte.txt', unpack = True)
tp = t[0:15]
tm = t[15:20]
T2p = T2[0:15]
T2m = T2[15:20]

def h(t, A, a, B, C):
    return (A*t**a)/(1+B*t**a)+ C

param_bounds=([-np.inf,1,-np.inf, -np.inf],[np.inf,2,np.inf, np.inf])


paramsH, covH = curve_fit(h, t, T1, bounds = param_bounds)

print('h(T1) : ',paramsH, np.sqrt(np.diag(covH)), sep='\n')

plt.plot(t, T1, 'rx', label = r'$T_1$')
plt.plot(tp, T2p, 'bx', label = r'$T_2$')
plt.plot(tm, T2m, 'kx', label = r'$T_2<0$')

plt.plot(t, h(t, *paramsH), 'r-.', label = r'$fit(T_1)$')


paramsH, covH = curve_fit(h, tp, T2p, bounds = param_bounds)

print('h(T2) : ',paramsH, np.sqrt(np.diag(covH)), sep='\n')

plt.plot(tp, h(tp, *paramsH), 'b-.', label = r'$fit(T_2)$')

plt.grid()

plt.xlabel(r'$t \:/\: min$')
plt.ylabel(r'$T \:/\: C$')
plt.legend(loc='best')
plt.savefig('Temperaturverlauf.pdf')
