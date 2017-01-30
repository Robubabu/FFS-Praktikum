import matplotlib.pyplot as plt
import numpy as np
import uncertainties.unumpy as unp
from scipy.optimize import curve_fit
from uncertainties import correlated_values, correlation_matrix
from uncertainties import ufloat
from uncertainties.unumpy import (nominal_values as noms, std_devs as stds)

A1 = ufloat(0.454, 0.020)
a1 = ufloat(1.73, 0.2)
B1 = ufloat(9.11e-3, 0.28e-3)
C1 = ufloat(20.12, 0.07)

A2 = ufloat(-0.255, 0.095)
a2 = ufloat(2.0, 0.19)
B2 = ufloat(7.75e-3, 2.1e-3)
C2 = ufloat(20.77, 0.35)

t, T1, T2, pa, pb, P = np.genfromtxt('../Werte/Werte.txt', unpack = True)
tp = t[0:15]
tm = t[15:20]
T2p = T2[0:15]
T2m = T2[15:20]

def T(t, A, a, B, C):
    return (a*A*t**(a-1))/(B*t**a+1)**2

print('T1(4)=', T(4,A1, a1, B1, C1))
print('T1(8)=', T(8,A1, a1, B1, C1))
print('T1(12)=', T(12,A1, a1, B1, C1))
print('T1(15)=', T(15,A1, a1, B1, C1))

print('T2(4)=', T(4,A2, a2, B2, C2))
print('T2(8)=', T(8,A2, a2, B2, C2))
print('T2(12)=', T(12,A2, a2, B2, C2))
print('T2(15)=', T(15,A2, a2, B2, C2))
