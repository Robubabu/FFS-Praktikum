import matplotlib.pyplot as plt
import numpy as np
import uncertainties.unumpy as unp
from scipy.optimize import curve_fit
from uncertainties import correlated_values, correlation_matrix
from uncertainties import ufloat
from uncertainties.unumpy import (nominal_values as noms, std_devs as stds)

Uio,tio = np.genfromtxt('5awerteoben.txt', unpack = True)
Uiu, tiu = np.genfromtxt('5awerteunten.txt', unpack = True )
Uio*=1e-3
Uiu*=1e-3
tio*=1e-6
tiu*=1e-6
U= np.append(Uio , Uiu)
t= np.append(tio ,tiu)

def fit(x , a , b):
    return a*x + b

oparam, ocav = curve_fit(fit , np.log(tio) , np.log(Uio))
uparam, ucav = curve_fit(fit, np.log(np.absolute(tiu[3:-3])) , np.log(np.absolute(Uiu[3:-3]) ))
oparam = correlated_values(oparam, ocav)
uparam = correlated_values(uparam, ucav)
oa = oparam[0]
ob = oparam[1]
ua = -uparam[0]
ub = -uparam[1]

print('Wert oa und ob:',oa,ob)
print('Wert ua und ub:', ua ,ub)
R = ufloat(48.1 , 0.1)
L = ufloat(10.11 , 0.03)/1000
x = np.linspace(0, 1e-3)

# plt.errorbar(noms(t) , noms(U) , xerr=stds(t),yerr=stds(U), fmt='rx' )
# plt.plot(x,fit(x , oa ,ob) , label='Kurve')
# plt.plot(x, fit(x ,ua, ub), label='Kurve')
# plt.xlabel(r'$\alpha \:/\: \si{\ohm}$')
# plt.ylabel(r'$y \:/\: \si{\micro\joule}$')

# plt.legend(loc='best')
#
# plt.subplot(1, 2, 2)
# plt.plot(x, y, label='Kurve')
# plt.xlabel(r'$\alpha \:/\: \si{\ohm}$')
# plt.ylabel(r'$y \:/\: \si{\micro\joule}$')
# plt.legend(loc='best')
#
# # in matplotlibrc leider (noch) nicht möglich
# plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
# plt.savefig('build/plot.pdf')
plt.show()
