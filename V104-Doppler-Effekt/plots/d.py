import matplotlib.pyplot as plt
import numpy as np
import uncertainties.unumpy as unp
from scipy.optimize import curve_fit
from scipy.stats import linregress
from uncertainties import correlated_values, correlation_matrix
from uncertainties import ufloat
from uncertainties.unumpy import (nominal_values as noms, std_devs as stds)
v1 , v2 , v3 , v4 , v5 , v6 , v7 , v8 , v9 , v0 = np.genfromtxt('dvor.txt' ,unpack = True)
r1 , r2, r3, r4, r5, r6, r7, r8, r9, r0 =np.genfromtxt('drueck.txt', unpack = True)
ngv , sgv , ngr , sgr = np.genfromtxt('GeschwVorRueck.txt' , unpack=True)
gv = unp.uarray(ngv, sgv)
gr = unp.uarray(ngr, sgr)
f = np.genfromtxt('b.txt' , unpack = True)  #f ist \nu_0
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
def fit(x,a):
    return a*x

dfv = v-f
dfr = r-f
x = np.append(gr,gv)
y = np.append(dfr, dfv)
# x = x[[0:5]+[7:15]+[19]]
# y = y[[0:5]+[7:15]+[19]]
# x = x[:-5]
# y = y[:-5]
n = np.array
m = np.array
for i,j in enumerate(y):
    if -40 < j < 40:
        n = np.append(n, x[i])
        m = np.append(m , j)
n = n[1:]
m = m[1:]
np.savetxt('xy.txt', np.column_stack([noms(n) , m]))
l,k = np.genfromtxt('xy.txt', unpack = True)
params , cov = curve_fit(fit, l , k)
params=correlated_values(params, cov)
print('Schallgeschw. c = f/a =', (f/params))
s = np.linspace(-0.6 , 0.6, num = 50)
plt.subplot(211)
plt.errorbar(noms(gv), dfv, xerr=stds(gv), fmt='rx', label='Frequenzänderung zum Sender hin ')
plt.errorbar(noms(gr), dfr, xerr=stds(gr), fmt='gx', label = 'Frequenzänderung vom Sender weg')
# plt.errorbar(s,fit(s,noms(params)), label = 'Fit')
plt.xlabel(r'$v \:/\: ms^{-1}$')
plt.ylabel(r'$\Delta \nu \:/\: Hz $')
plt.xlim(-0.6,0.6)
plt.grid()
plt.legend(loc='best')
plt.subplot(212)
plt.errorbar(noms(gv), dfv, xerr=stds(gv), fmt='rx')
plt.errorbar(noms(gr), dfr, xerr=stds(gr), fmt='gx')
plt.errorbar(s,fit(s,noms(params)), label = 'Fit')
plt.xlabel(r'$v \:/\: ms^{-1}$')
plt.ylabel(r'$\Delta \nu \:/\: Hz $')
plt.legend(loc='best')
plt.xlim(-0.6,0.6)
plt.ylim(-40,40)
plt.grid()
# plt.show()

# plt.xlabel(r'$\alpha \:/\: \si{\ohm}$')
# plt.ylabel(r'$y \:/\: \si{\micro\joule}$')
# plt.legend(loc='best')
#
# # in matplotlibrc leider (noch) nicht möglich
# plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('dplot.pdf')
