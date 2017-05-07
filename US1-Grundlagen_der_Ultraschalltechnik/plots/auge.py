import matplotlib.pyplot as plt
import numpy as np
import uncertainties.unumpy as unp
from scipy.optimize import curve_fit
from uncertainties import correlated_values, correlation_matrix
from uncertainties import ufloat
from uncertainties.unumpy import (nominal_values as noms, std_devs as stds)

#the real mean()-ing of life
def mittel(x):
    return ufloat(np.mean(x),np.std(x,ddof=1)/np.sqrt(len(x)))
p , d = np.genfromtxt('auge.txt', unpack = True)
d*=10**-6
c1 = 2500
c2 = 1410
s1 = c2/2 * (d[1]-d[0]) # abs von hornhaut zu linse
s2 = c1/2 * (d[2]-d[1]) #abs linse zu linse ende
s3 = c2/2 * (d[3]-d[2]) #abs linse zu retina
print('Abs Hornhaut zu Linse:', s1)
print('Dicke der Linse:',s2)
print('Abs Linse zu Retina:', s3)
# #Fit
# params , cov = curve_fit(f , x ,y )
# params = correlated_values(params, cov)
# for p in params:
#     print p

x = np.linspace(0, 10, 1000)

#Tabelen
# np.savetxt('tab.txt',np.column_stack([x,y]), delimiter=' & ',newline= r'\\'+'\n' )

# #Plot
# plt.subplot(1, 2, 1)
# plt.plot(x, y, label='Kurve')
# plt.xlabel(r'$\alpha \:/\: \si{\ohm}$')
# plt.ylabel(r'$y \:/\: \si{\micro\joule}$')
# plt.legend(loc='best')
#
# plt.clf()
#
# plt.subplot(1, 2, 2)
# plt.plot(x, y, label='Kurve')
# plt.xlabel(r'$\alpha \:/\: \si{\ohm}$')
# plt.ylabel(r'$y \:/\: \si{\micro\joule}$')
# plt.legend(loc='best')
#
# # in matplotlibrc leider (noch) nicht möglich
# #plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
# plt.savefig('build/plot2.pdf')
