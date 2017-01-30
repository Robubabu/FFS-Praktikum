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
pa = pa * 100000
pb = pb * 100000
t4 = ufloat(-1.6, 0.8)
t8 = ufloat(-1.8, 0.9)
t12 = ufloat(-1.4, 0.6)
t15 = ufloat(-1, 0.5)

k =1.14
r = 5.51

L=ufloat(147,2)

dm4 = 1/L*(3*4.2+0.66)*t4
dm8 = 1/L*(3*4.2+0.66)*t8
dm12 = 1/L*(3*4.2+0.66)*t12
dm15 = 1/L*(3*4.2+0.66)*t15

print('dm(4)=', dm4)
print('dm(8)=', dm8)
print('dm(12)=', dm12)
print('dm(15)=', dm15)

pA = pa[4]
pB= pb[4]
N4 = 1/(k-1)*((pB/pA)*(pA/pB)**(1/k)-1)*5*T2[4]/(r*19.9)*(dm4*60)

pA = pa[8]
pB= pb[8]
N8 = 1/(k-1)*(pB/pA*(pA/pB)**(1/k)-1)*5*T2[8]/(r*19.9)*dm8*60

pA = pa[12]
pB= pb[12]
N12 = 1/(k-1)*(pB/pA*(pA/pB)**(1/k)-1)*5*T2[12]/(r*19.9)*dm12*60

pA = pa[15]
pB= pb[15]
N15 = 1/(k-1)*(pB/pA*(pA/pB)**(1/k)-1)*5*T2[15]/(r*19.9)*dm15*60

print('N4:', N4)

print('N8:', N8)

print('N12:', N12)

print('N15:', N15)
