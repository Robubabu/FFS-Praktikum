import matplotlib.pyplot as plt
import numpy as np
import uncertainties.unumpy as unp
from scipy.optimize import curve_fit
from uncertainties import correlated_values, correlation_matrix
from uncertainties import ufloat
from uncertainties.unumpy import (nominal_values as noms, std_devs as stds)
v1 , v2 , v3 , v4 , v5 , v6 , v7 , v8 , v9 , v0 = np.genfromtxt('dvor.txt' ,unpack = True)
r1 , r2, r3, r4, r5, r6, r7, r8, r9, r0 =np.genfromtxt('drueck.txt', unpack = True)
f = np.genfromtxt('b.txt' , unpack = True)  #f ist \nu_0
y= np.genfromtxt('GeschwMittelproGang.txt', unpack = True)
l,m = np.genfromtxt('Mittelwellenlaenge.txt', unpack=True)
lm = ufloat(l,m)
f*=1e-1
c = f*lm                #errechnete Schallgeschw
v1=np.append(v1, r1)
v2=np.append(v2 ,r2)
v3=np.append(v3,r3)
v4=np.append(v4,r4)
v5=np.append(v5,r5)
v6=np.append(v6,r6)*0.1             #ab 6tem Gang wurde in 1/10s gemessen
v7=np.append(v7,r7)*0.1
v8=np.append(v8,r8)*0.1
v9 =np.append(v9, r9)*0.1
v0 =np.append(v0 , r0)*0.1
F = np.array([v1,v2,v3,v4,v5,v6,v7,v8,v9,v0])
fq = np.array
for fq in F:
    fq = np.append(fq,np.mean(fq))
fq=fq[1:]


def f2(f,v,c):
     return f*(1 + (v/c))
def f5(f,v,c):
    return f*(1/(1-(v/c)))

df=f-fq



plt.errorbar(y, noms(df),yerr=stds(df),fmt='rx', label='Frequenz d. bewegten Empfängers')
plt.plot(y,)
plt.xlabel(r'$v \:/\: ms^{-1}$')
plt.ylabel(r'$\Delta \nu \:/\: Hz $')
plt.xlim(0, 0.6)
plt.legend(loc='best')
plt.show()
# plt.subplot(1, 2, 2)
# plt.plot(x, y, label='Kurve')
# plt.xlabel(r'$\alpha \:/\: \si{\ohm}$')
# plt.ylabel(r'$y \:/\: \si{\micro\joule}$')
# plt.legend(loc='best')
#
# # in matplotlibrc leider (noch) nicht möglich
# plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
# plt.savefig('build/plot.pdf')
