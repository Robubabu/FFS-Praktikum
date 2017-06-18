import matplotlib.pyplot as plt
import numpy as np
import uncertainties.unumpy as unp
from scipy.optimize import curve_fit
from uncertainties import correlated_values, correlation_matrix
from uncertainties import ufloat
from uncertainties.unumpy import (nominal_values as noms, std_devs as stds)
x = np.linspace(1.5, 5)
def mittel(x):              #the real mean()-ing of life
    return ufloat(np.mean(x),np.std(x,ddof=1)/np.sqrt(len(x)))

def fit(x,a,b):
    return a*x +b
def relf(l,m): #relativer Fehler in Prozent
    return (np.absolute(l - m)/np.absolute(l))*100

#Abbe Gegenstands weite Position des LSys Position des Schirms Bildgröße alles cm
xG,xLS,xS,B = np.genfromtxt('abbe.txt', unpack = True)
#Abs der Linsen 6cm xLS ist die Position der zum Schirm gewanten Linse
a = 6
#Gegenstandsgröße G = 3cm
G = 3
#Erstelle Mittelpunktsposition des Linsensystems
mLS = xLS + a/2
#Berechnene gestrichene Größen und V
gs = xG-mLS
bs = mLS - xS
V = B/G
#Umrechnen in Meter
gs*=10**-2
bs*=10**-2

#Fit für g strich
# y = gs
#x = (1+ (1/V))
xg = (1+ (1/V))
gparams , gcov = curve_fit(fit , xg,gs )
gparams = correlated_values(gparams, gcov)
gf,gh = gparams
print('Brennweite von g` :',gf)
print('h von g´ :', gh)
#Fit für b strich
#y = bs
#x = (1+V)
xb = 1 + V
bparams , bcov = curve_fit(fit , xb ,bs )
bparams = correlated_values(bparams, bcov)
bf,bh = bparams
print('Brennweite von b` :',bf)
print('h von b´ :', bh)

#Relative Fehler
print('Abweichung von der Brennweiten :', (gf - bf) )
print('Abweichung der y-Abschnt. :', (gh-bh))




#Tabelle
# np.savetxt('abbetab.txt',np.column_stack([xG,mLS,xS,B,gs,bs,xg,xb]), delimiter=' & ',newline= r'\\'+'\n' )

#plt.subplot(1, 2, 1)
# plt.plot(gs, xg,'rx', label='Messwerte g´ gegen (1+(1/V))')
# plt.plot(noms(fit(x,gf,gh)),x,label='Ausgleichgerade')
# plt.xlabel(r'$(1+ \frac{1}{V})$')
# plt.ylabel(r'$g\' / m$')
# plt.legend(loc='best')
# # plt.show()
# plt.savefig('gsplot.pdf')
# plt.clf()
# # #plt.subplot(1, 2, 2)
# y = np.linspace(1, 2)
# plt.plot(bs, xb,'rx', label='Messwerte b´ gegen (1+V)')
# plt.plot(noms(fit(y,bf,bh)),y,label='Ausgleichgerade')
# plt.xlabel(r'$(1+ V)$')
# plt.ylabel(r'$b\' / m$')
# plt.legend(loc='best')
# # plt.show()
# plt.savefig('bsplot.pdf')
