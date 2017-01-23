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

def f(t, A, B, C):
    return A*t**2 + B*t + C

def g(t, A, a, B):
    return A/(1+B*t**a)

def h(t, A, a, B, C):
    return (A*t**a)/(1+B*t**a)+ C

def i(t, A, a, B, C):
    return (A*t**a)/(1+B*t**2)+ C

paramsF, covF = curve_fit(f, t, T1)
paramsG, covG = curve_fit(g, t, T1)
paramsH, covH = curve_fit(h, t, T1)

print('h(T1) : ',paramsH, np.sqrt(np.diag(covH)), sep='\n')

plt.plot(t, T1, 'rx', label = r'$T_1$')
plt.plot(tp, T2p, 'bx', label = r'$T_2$')
plt.plot(tm, T2m, 'kx', label = r'$T_2<0$')

plt.plot(t, h(t, *paramsH), 'r-.', label = r'$fit(T_1)$')

paramsF, covF = curve_fit(f, t, T2)
paramsG, covG = curve_fit(g, t, T2)
paramsH, covH = curve_fit(h, tp, T2p)
paramsI, covI = curve_fit(i, t, T2)
#print('f(T2): ',paramsF, np.sqrt(np.diag(covF)), sep='\n')
#print('g(T2): ',paramsG, np.sqrt(np.diag(covG)), sep='\n')
print('h(T2) : ',paramsH, np.sqrt(np.diag(covH)), sep='\n')
#print('i(T2) : ',paramsI, np.sqrt(np.diag(covI)), sep='\n')

#plt.plot(t, f(t, *paramsF), 'y-', label = r'$f(T_2)$')
#plt.plot(t, g(t, *paramsG), 'k-', label = r'$g(T_2)$')
plt.plot(tp, h(tp, *paramsH), 'b-.', label = r'$fit(T_2)$')
#plt.plot(t, i(t, *paramsH), 'g-.', label = r'$i(T_2)$')



plt.grid()

plt.xlabel(r'$t \:/\: min$')
plt.ylabel(r'$T \:/\: C$')
plt.legend(loc='best')
plt.savefig('Temperaturverlauf.pdf')
