import matplotlib.pyplot as plt
import numpy as np
import uncertainties.unumpy as unp
from scipy.optimize import curve_fit
from uncertainties import correlated_values, correlation_matrix
from uncertainties import ufloat
from uncertainties.unumpy import (nominal_values as noms, std_devs as stds)

def mittel(x):              #the real mean()-ing of life
    return ufloat(np.mean(x),np.std(x,ddof=1)/np.sqrt(len(x)))
l = np.linspace(5,21)
#skalenwerte
# 10 volt abs
s1 = np.array([6.2, 6.45])
# 5 volt abs
s2 = np.array([3.55 , 3.35 ,3.25])
#xy Werte in cm
x ,y= np.genfromtxt('8cxy.txt', unpack = True)
# fit gerade
def f(x,a,b):
    return a*x + b

s1 = 10/s1
s2 = 5/s2
s = np.append(s1, s2)
s = mittel(s)
print('Mittlerer Skalen Abstand in Volt pro cm:', s)






params , cov = curve_fit(f , x ,y )
params = correlated_values(params, cov)
for p in params:
    print('a,b :',p)
a = params[0]
b = params[1]
print('Postition des Nulldurchlaufes in cm:', -b/a)
print('Position des Nulldurchlaufes in Volt:', (-b/a)*s)
z = x*s
i =(-b/a)*s
k1 = ufloat(1.11,0.18)
k2 = ufloat(0.94 , 0.12)
k = np.mean([k1,k2])
print('mittleres Kontaktpotential:', k)
print('Ionisierungsspannung:', i-k)
#plt.subplot(1, 2, 1)
plt.plot(x, y,'rx' ,label='Ionisierungsspannung')
plt.plot(l, f(l,noms(a), noms(b)), label= 'Ausgleichsgerade')

np.savetxt('8ctab.txt',np.column_stack([x,y, noms(z), stds(z)]), delimiter=' & ',newline= r'\\'+'\n' )

plt.xlabel(r'$x / cm$')
plt.ylabel(r'$y \:/\: cm$')
plt.xlim(6,20)
plt.legend(loc='best')
# plt.show()
plt.savefig('8cplot.pdf')
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
