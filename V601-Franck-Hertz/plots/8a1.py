import matplotlib.pyplot as plt
import numpy as np
import uncertainties.unumpy as unp
from scipy.optimize import curve_fit
from uncertainties import correlated_values, correlation_matrix
from uncertainties import ufloat
from uncertainties.unumpy import (nominal_values as noms, std_devs as stds)

a,p = np.genfromtxt('8a1-Werte.txt' , unpack = True)
sx = np.genfromtxt('8a1-Skalarx.txt', unpack = True)
def mittel(x):              #the real mean()-ing of life
    return ufloat(np.mean(x),np.std(x,ddof=1)/np.sqrt(len(x)))

sx = mittel(sx)
print('Mittlere x Skalen Abstand:' , sx)
sy = 4.6 /12.3 # nano A duch cm
f = sy/sx*10**-9 # Skalenfaktor A / V
print(f)
a = a*f
p = p/sx
#plt.subplot(1, 2, 1)
plt.plot(noms(p), noms(a), 'rx' ,label='Differentielle Energieverteilung')
plt.axvline(x=10,)
plt.xlabel(r'$U_A / V$')
plt.ylabel(r'$ \frac{\Delta I_A}{\Delta U_A} / \frac{A}{V}$')
plt.legend(loc='best')
plt.show()
# plt.savefig('build/plot2.pdf')
