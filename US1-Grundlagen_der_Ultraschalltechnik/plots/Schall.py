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
z1 , l , t = np.genfromtxt('IE_Data.txt', unpack = True) #zylinder länge durchlaufzeit Impuls Echo
z2, t2 = np.genfromtxt('DS_Data.txt', unpack = True) # zylinder durchlaufzeit Durchstrahlung
l*= 10**(-3)
t*= 10**(-6)
h =  l[0:5]
t2*= 10**(-6)
def tschall(l,c,dt):
    return 2*l/c + dt
def dschall(h,c,dt):
    return h/c + dt
#Fit
params , cov = curve_fit(tschall , l ,t)
params = correlated_values(params, cov)
c = params[0]
dt = params[1]
params2 , cov2 = curve_fit(dschall , h ,t2)
params2 = correlated_values(params2, cov2)
c2 = params2[0]
dt2 = params2[1]
print('Schallgeschw. ImpulsEcho:', c)
print('Schallgeschw. Durchschall:',c2)
print('IE Fehler:', dt)
print('DS Fehler:', dt2)

# x = np.linspace(0, 0.13, 1000)
# # #Tabelen
# np.savetxt('IEtab.txt',np.column_stack([l,t]), delimiter=' & ',newline= r'\\'+'\n' )
# np.savetxt('DStab.txt',np.column_stack([h,t2]), delimiter=' & ',newline= r'\\'+'\n' )
#
# # # #Plot
# # # plt.subplot(1, 2, 1)
# plt.plot(l, t*10**5,'rx', label='Messwerte')
# plt.plot(x, noms(tschall(x,c,dt))*10**5, label= 'Ausgleichsgerade')
# plt.xlabel(r'$ h / m$')
# plt.ylabel(r'$ t \cdot 10^5 / s$')
# plt.xlim(0,0.13)
# plt.legend(loc='best')
# plt.savefig('IE_plot.pdf')
# # plt.show()
# #
# plt.clf()
# #
# # plt.subplot(1, 2, 2)
# plt.plot(h, t2* 10**5,'rx' , label='Messwerte')
# plt.plot(x,noms(dschall(x,c2,dt2))*10**5, label='Ausgleichsgerade')
# plt.xlabel(r'$h\:/\: m$')
# plt.ylabel(r'$ t \cdot 10^5 \:/\: s$')
# plt.xlim(0,0.13)
# plt.legend(loc='best')
# # plt.show()
# # # in matplotlibrc leider (noch) nicht möglich
# # plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
# plt.savefig('DS_plot.pdf')
