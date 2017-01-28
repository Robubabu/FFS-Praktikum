import matplotlib.pyplot as plt
import numpy as np
import uncertainties.unumpy as unp
from scipy.optimize import curve_fit
from uncertainties import correlated_values, correlation_matrix
from uncertainties import ufloat
from uncertainties.unumpy import (nominal_values as noms, std_devs as stds)
from K2 import K1 , K2 , r1 ,r2, nu
T , t = np.genfromtxt('M2K1.txt', unpack =True)
T+= 273.15 #in Kelvin um rechnen
x = 1/T
n = nu(K2, r2 , 1000, t)
y = unp.log(n)
# cy = np.array(noms(y))
def leta(x,B,A):
    return  (B*x)+np.log(A)

params, cov = curve_fit(leta, x[0:10] ,noms(y[0:10]) )
params = correlated_values(params,cov)
for p in params:
    print(p)
B , A = params
def eta(x,B,A):
    return unp.exp(B*x)*A
e = eta(x[0:10],B,A)
e=ufloat(np.mean(noms(e)), np.std(noms(e) , ddof=1) / unp.sqrt(len(e)))
print(e)


plt.errorbar(x ,noms(y),yerr= stds(y), fmt='rx',label= 'Messwerte')
plt.plot(x, leta(x,noms(B),noms(A)),'b--',label='Ausgleichgrade')
plt.xlabel(r'$ \frac{1}{T} \:/\: K^{-1}$')
plt.ylabel(r'$ln(\eta \:/\: mPas)$')
plt.grid()
plt.legend(loc='best')
# plt.savefig('plot.pdf')
plt.show()
