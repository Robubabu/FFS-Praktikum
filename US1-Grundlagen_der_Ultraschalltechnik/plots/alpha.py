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
    return a*10**(-(g/20)) #gain von der amplitude abrechnen
def fit(x,b):
    return b*x # Y =  bx  -> y = exp(b*x)

ar = gain(a2,g)
x = 2*h[0:5] # x ist 2h wegen Impuls Echo
qI = ar/a1 # ist gleich von I(x)/I0
lqI = np.log(qI)

# Fit
params , cov = curve_fit(fit , x ,lqI )
params = correlated_values(params, cov)
print(params)

c = np.linspace(0,0.00025 , 1000)

#Tabelen
np.savetxt('alphatab.txt',np.column_stack([x,lqI,a1,a2,g]), delimiter=' & ',newline= r'\\'+'\n' )

# #Plot
# plt.subplot(1, 2, 1)
plt.plot(x, lqI,'rx', label='Messwerte')
plt.plot(c,fit(c,noms(params)), label= 'Ausgleichsgerade')
plt.ylabel(r'$ln\left(\frac{I(x)}{I_0}\right)$')
plt.xlabel(r'$x /m$')
plt.legend(loc='best')
# plt.show()
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
plt.savefig('alphaplot.pdf')
