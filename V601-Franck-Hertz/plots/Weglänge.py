import matplotlib.pyplot as plt
import numpy as np
import uncertainties.unumpy as unp
from scipy.optimize import curve_fit
from uncertainties import correlated_values, correlation_matrix
from uncertainties import ufloat
from uncertainties.unumpy import (nominal_values as noms, std_devs as stds)
import scipy.constants as const
def mittel(x):              #the real mean()-ing of life
    return ufloat(np.mean(x),np.std(x,ddof=1)/np.sqrt(len(x)))
def psaet(T):
    return 5.5*10**7* np.exp(-6876/T)
def wegw(p):
    return 0.0029 / p
# T in Celsius
a_1 = 23.2
a_2 = 159
b = 198
c = 103
fk = const.zero_Celsius #null Celsius in Kelvin
#umrechnen in kelvin
a_1 = a_1 + fk
a_2+= fk
b+= fk
c+=fk
T = np.array([a_1, a_2 , b ,c])
p = psaet(T)
w = wegw(p)
f = 1/w
np.savetxt('weglaenge.txt',np.column_stack([T,p,w,f]), delimiter=' & ',newline= r'\\'+'\n' )

#plt.subplot(1, 2, 1)
# plt.plot(x, y, label='Kurve')
# plt.xlabel(r'$\alpha \:/\: \si{\ohm}$')
# plt.ylabel(r'$y \:/\: \si{\micro\joule}$')
# plt.legend(loc='best')
# plt.savefig('build/plot.pdf')
# plt.clf()
# #plt.subplot(1, 2, 2)
# plt.plot(x, y, label='Kurve')
# plt.xlabel(r'$\alpha \:/\: \si{\ohm}$')
# plt.ylabel(r'$y \:/\: \si{\micro\joule}$')
# plt.legend(loc='best')
#
# # in matplotlibrc leider (noch) nicht möglich
# #plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
# plt.savefig('build/plot2.pdf')
