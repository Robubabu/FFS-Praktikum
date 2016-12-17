import matplotlib.pyplot as plt
import numpy as np
import uncertainties.unumpy as unp
from scipy.optimize import curve_fit
from uncertainties import correlated_values, correlation_matrix
from uncertainties import ufloat
from uncertainties.unumpy import (nominal_values as noms, std_devs as stds)
v1 , v2 , v3 , v4 , v5 , v6 , v7 , v8 , v9 , v0 = np.genfromtxt('dvor.txt' ,unpack = True)
r1 , r2, r3, r4, r5, r6, r7, r8, r9, r0 =np.genfromtxt('drueck.txt', unpack = True)
ngv , sgv , ngr , sgr = np.genfromtxt('GeschwVorRueck.txt' , unpack=True)
gv = unp.uarray(ngv, sgv)
gr = unp.uarray(ngr, sgr)
f = np.genfromtxt('b.txt' , unpack = True)  #f ist \nu_0
l,m = np.genfromtxt('Mittelwellenlaenge.txt', unpack=True)
lm = ufloat(l,m)        #fehlerbehaftete Wellenlänge lambda
c = f*lm                #errechnete Schallgeschw
V = np.array([v1,v2,v3,v4,v5,v6,v7,v8,v9,v0])
R = np.array([r1,r2,r3,r4,r5,r6,r7,r8,r9,r0])
v = np.array
r = np.array

for i in V:
    v = np.append(v,np.mean(i))
v = v[1:]
for j in R:
    r = np.append(r, np.mean(j))
r=r[1:]
def f2(f,v,c):
     return f*(1 + (v/c))
def f5(f,v,c):
    return f*(1/(1-(v/c)))
dfv = v - f
dfr = r - f
plt.errorbar(noms(gv), dfv, xerr=stds(gv), fmt='rx', label='Frequenzänderung zum Sender hin ')
plt.errorbar(noms(gr), dfr, xerr=stds(gr), fmt='gx', label = 'Frequenzänderung vom Sender weg')
# plt.xlabel(r'$v \:/\: ms^{-1}$')
# plt.ylabel(r'$\Delta \nu \:/\: Hz $')
# plt.xlim(0, 0.6)
plt.legend(loc='best')
plt.show()
# # plt.subplot(1, 2, 2)
# plt.plot(x, y, label='Kurve')
# plt.xlabel(r'$\alpha \:/\: \si{\ohm}$')
# plt.ylabel(r'$y \:/\: \si{\micro\joule}$')
# plt.legend(loc='best')
#
# # in matplotlibrc leider (noch) nicht möglich
# plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
# plt.savefig('build/plot.pdf')
