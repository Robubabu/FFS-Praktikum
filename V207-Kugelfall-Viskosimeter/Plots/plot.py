import matplotlib.pyplot as plt
import numpy as np
import uncertainties.unumpy as unp
from scipy.optimize import curve_fit
from uncertainties import correlated_values, correlation_matrix
from uncertainties import ufloat
from uncertainties.unumpy import (nominal_values as noms, std_devs as stds)
from K2 import K1 , K2 , r1 ,r2, nu , d2 ,rerr
def mittel(x):              #the real mean()-ing of life
    return ufloat(np.mean(x),np.std(x,ddof=1)/np.sqrt(len(x)))

T , t1,t2 = np.genfromtxt('M2K1.txt', unpack =True)
T+= 273.15 #in Kelvin um rechnen
x = 1/T
tn = np.array([])
terr = np.array([])
for i,j in enumerate(t1):
    a = [j, t2[i]]
    b = mittel(a)
    tn = np.append(tn,noms(b))
    terr = np.append(terr,stds(b))
t= unp.uarray(tn, terr)
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
#reynold bei 70 grad
print(1000 * 0.1 * d2 / eta(x[9],B,A)*t[9])
# np.savetxt('tab.txt',np.column_stack([T,t1,t2,tn,terr, noms(n),stds(n)]), delimiter=' & ',newline= r'\\'+'\n' )
# np.savetxt('plottab.txt',np.column_stack([x,noms(y), stds(y)]), delimiter=' & ',newline= r'\\'+'\n' )
#relativer Fehler
c = -6.944 #literaturwert von log(A)
d = 2036.8 #literatur wert zu B
print('relativer Fehler von A: ', rerr(unp.log(A), c))
print('relativer Fehler von B:', rerr(B,d))

plt.errorbar(x ,noms(y),yerr= stds(y), fmt='rx',label= 'Messwerte')
plt.plot(x, leta(x,noms(B),noms(A)),'b--',label='Ausgleichgrade')
plt.xlabel(r'$ \frac{1}{T} \:/\: K^{-1}$')
plt.ylabel(r'$ln(\eta \:/\: mPas)$')
plt.grid()
plt.legend(loc='best')
# plt.savefig('plot.pdf')
# plt.show()
