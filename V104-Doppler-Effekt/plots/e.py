import matplotlib.pyplot as plt
import numpy as np
import uncertainties.unumpy as unp
from scipy.optimize import curve_fit
from uncertainties import correlated_values, correlation_matrix
from uncertainties import ufloat
from uncertainties.unumpy import (nominal_values as noms, std_devs as stds)
v1 , v2 , v3 , v4 , v5 , v6 , v7 , v8 , v9 , v0 = np.genfromtxt('evor.txt' ,unpack = True)
r1 , r2, r3, r4, r5, r6, r7, r8, r9, r0 =np.genfromtxt('erueck.txt', unpack = True)
ngv , sgv , ngr , sgr = np.genfromtxt('GeschwVorRueck.txt' , unpack=True)
f = np.genfromtxt('b.txt' , unpack = True)  #f ist \nu_0
gv = unp.uarray(ngv, sgv)
gr = unp.uarray(ngr, sgr)
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
np.savetxt('evorxy.txt', np.column_stack([noms(gv),v]))
vx , vy = np.genfromtxt('evorxy.txt', unpack = True)
np.savetxt('erueckxy.txt', np.column_stack([noms(gr),r]))
rx , ry = np.genfromtxt('erueckxy.txt', unpack = True)


vparams ,vcov = curve_fit(fit,vx, vy)
rparams , rcov = curve_fit(fit, rx , ry)
vparams = correlated_values(vparams, vcov)
rparams = correlated_values(rparams , rcov)
va = vparams
ra = rparams
x = np.linspace(0,0.6, num = 50)
print(va)
print(ra)
print(f/va)
print(f/ra)


plt.subplot(1, 2, 1)
plt.errorbar(noms(gr), r , xerr=stds(gr), fmt='gx', label= r'$\Delta \nu$ ')
plt.plot(-x , fit(-x, noms(ra)), label= 'Fit')
plt.xlabel(r'$ v \:/\: ms^{-1}$')
plt.ylabel(r'$ \Delta \nu \:/\: Hz$')
plt.xlim(-0.6,0)
plt.grid()
plt.legend(loc='best')


plt.subplot(1, 2, 2)
plt.errorbar(noms(gv), v, xerr=stds(gv), fmt='rx', label=r'$\Delta \nu$ ')
plt.plot(x , fit(x,noms(va)), label = 'Fit')
plt.xlabel(r'$ v \:/\: ms^{-1}$')
plt.ylabel(r'$ \Delta \nu \:/\: Hz$')
plt.xlim(0,0.6)
plt.grid()
plt.legend(loc='best')

# plt.show()

plt.savefig('eplot.pdf')
