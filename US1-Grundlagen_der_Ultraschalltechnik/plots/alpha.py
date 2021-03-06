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
z1 , a1 ,a2, g = np.genfromtxt('IE2_Data.txt', unpack = True)
z2,h,t = np.genfromtxt('IE_Data.txt', unpack = True)
h*=10**-6
def gain(a,g):
    return a/10**((g/20)) #gain von der amplitude abrechnen
def fit(x,b,a):
    return b*x +a # Y =  bx  -> y = exp(b*x)
def relf(l,m):
    return (np.absolute(l-m)/l) *100
def fit2(x,y,z):
    return z*np.exp(x*y)
#gain abrechnen
ar = gain(a2,g) #TGC
print(ar)
ar = gain(ar,15)    #gain1 15
a1 = gain(a1,15)
ar = gain(ar,10)    #output 10
a1 = gain(a1,10)
print(ar)
print(a1)
x = 2*h[0:5] # x ist 2h wegen Impuls Echo
qI = ar/a1 # ist gleich von I(x)/I0
lqI = 20*np.log10(qI)

# Fit
params , cov = curve_fit(fit , x ,lqI )
params = correlated_values(params, cov)
#Fit 2
params2 , cov2 = curve_fit(fit2 , x ,noms(ar) )
params2 = correlated_values(params2, cov)
for p in params2:
    print(p)
print((-20*np.log(noms(-params2[0]))) / np.log(10))
print(params)
g =(-20*params[0]) / np.log(10)
print(g)
c = np.linspace(0,0.00025 , 1000)
print(relf(270,g))
print(relf(570,g))
#Tabelen
# np.savetxt('alphatab.txt',np.column_stack([x,lqI,a1,a2,g]), delimiter=' & ',newline= r'\\'+'\n' )

# #Plot
# plt.subplot(1, 2, 1)
plt.plot(x, ar,'rx', label='Messwerte')
plt.plot(c,fit2(c,noms(params2[0]),noms(params2[1])), label= 'Ausgleichsgerade')
plt.ylabel(r'$ln\left(\frac{I(x)}{I_0}\right)$')
plt.xlabel(r'$x /m$')
plt.legend(loc='best')
plt.show()
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
# plt.savefig('alphaplot.pdf')
