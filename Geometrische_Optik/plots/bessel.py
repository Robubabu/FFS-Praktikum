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

def f(d,o): #Bessel Brennweite Fkt.
    return ((o**2) - d**2)/4*o

def relf(l,m): #relativer Fehler in Prozent 
    return (np.absolute(l-m)/np.absolute(l))
#Bessel normales Licht
xG1,aL1,bL1,xS1 = np.genfromtxt('besselLinse100mmnormal.txt',unpack = True)
#Bessel blaues Licht
xG2,aL2,bL2,xS2 = np.genfromtxt('besselLinse100mmblau.txt',unpack = True)
#Bessel rotes Licht
xG3,aL3,bL3,xS3 = np.genfromtxt('besselLinse100mmrot.txt',unpack = True)
# Brennweite der verwendeten Linse
fl = 100 # milimeter
#e und d für die jeweiligen Lichter n,b,r berechnen
en = xG1 - xS1
dn = bL1 - aL1
eb = xG2 - xS2
db = aL2 - bL2
er = xG3 - xS3
dr = bL3 - aL3
#Umrechnen
en*= 10e-3
dn*= 10e-3
eb*= 10e-3
db*= 10e-3
er*= 10e-3
dr*= 10e-3
fl*= 10e-4
print(10e-4)
# Brennweiten Brechnen
fn = f(dn,en)
fb = f(db,eb)
fr = f(dr,er)
print(fn)
print(fb)
print(fr)

#Mittelwert der berechneten Brennweiten
mfn = mittel(fn)
mfb = mittel(fb)
mfr = mittel(fr)
# Relative Fehler des Mittelwerts der Berechneten Brennweiten
print('Relativer Fehler vom Mittelwert von f für normales Licht:', relf(fl,mfn))
print('Relativer Fehler vom Mittelwert von f für blaues Licht:',relf(fl,mfb))
print('Relativer Fehler vom Mittelwert von f für rotes Licht:', relf(fl,mfr))

# #Fit
# params , cov = curve_fit(f , x ,y )
# params = correlated_values(params, cov)
# for p in params:
#     print(p)
#
#Tabelle
# np.savetxt('tab.txt',np.column_stack([x,y]), delimiter=' & ',newline= r'\\'+'\n' )

# #plt.subplot(1, 2, 1)
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
