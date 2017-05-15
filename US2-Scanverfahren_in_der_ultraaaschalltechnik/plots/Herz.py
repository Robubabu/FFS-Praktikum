import matplotlib.pyplot as plt
import numpy as np
import uncertainties.unumpy as unp
from scipy.optimize import curve_fit
from uncertainties import correlated_values, correlation_matrix
from uncertainties import ufloat
from uncertainties.unumpy import (nominal_values as noms, std_devs as stds)
x = np.linspace(0, 10, 1000)
def mittel(x):              #the real mean()-ing of life
    return ufloat(np.mean(x),np.std(x,ddof=1)/np.sqrt(len(x)))
t , d = np.genfromtxt('Ascan_Herz.txt', unpack = True)
R=(46*10**-3)/2  #Radius
print(R)
#Umrechnen
d*=10**-6

#Peakdetakt
tp=np.array([1.3,3.5,5.6,8])
tm = np.array([3.5,5.6,8])
f = tm -tp[0:-1]
f = mittel(f)
print('Herzfrequenz:',f)
#Bestimmung des Volumens
h = (2730/2) *((37.7 - 11.8)*10**-6) #höhe des Paraboluids
print('Höhe des Paraboluids:',h)
V = (3.1415/2 )*h* R**2  #Volumen des Paraboluids
print('Volumen des Paraboloids:', V)
# np.savetxt('tab.txt',np.column_stack([x,y]), delimiter=' & ',newline= r'\\'+'\n' )

#plt.subplot(1, 2, 1)
# plt.plot(t , -d,'r--', label='Herzschlag')
# plt.xlabel(r'$t / s$')
# plt.ylabel(r'$ negative \; Laufzeit\; des\; Ultraschalls\; (-d) /s$')
# plt.legend(loc='best')
# plt.yticks([])
# # plt.show()
# plt.savefig('Herzplot.pdf')
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
