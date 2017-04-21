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
a_u = a
p_u = p
sx = mittel(sx)
print('Mittlere x Skalen Abstand:' , sx)
sy = 4.6 /12.3 # nano A duch cm
print('y-Achsen Referenzwert:', sy)
f = sy/sx*10**-9 # Skalenfaktor A / V
print('Umrechnungsfaktor:', f)
a = a*f
p = p/sx
m = p[10:13]
M = np.mean(m)
print(M)
#plt.subplot(1, 2, 1)
np.savetxt('steigung.txt',np.column_stack([a_u,p_u,noms(a),stds(a),noms(p),stds(p)]), delimiter=' & ',newline= r'\\'+'\n' )
plt.plot(noms(p), noms(a), 'rx' ,label='Differentielle Energieverteilung')
plt.axvline(x=noms(M))
plt.xlabel(r'$U_A / V$')
plt.ylabel(r'$ \frac{\Delta I_A}{\Delta U_A} / \frac{A}{V}$')
plt.legend(loc='best')
# plt.show()
plt.savefig('8a1plot.pdf')
