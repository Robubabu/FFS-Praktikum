import matplotlib.pyplot as plt
import numpy as np
import uncertainties.unumpy as unp
from scipy.optimize import curve_fit
from uncertainties import correlated_values, correlation_matrix
from uncertainties import ufloat
from uncertainties.unumpy import (nominal_values as noms, std_devs as stds)
import scipy.constants as const
x = np.linspace(0, 0.23, 1000)
B = 6.17*10**-3 #Cunningham Korrektur Torr * cm
B*=(101325/760)*10**-2 #Umrechnen in Pa*m
p = const.value('standard atmosphere')
rho = 886 #kg / m**3
d = ufloat(7.6250,0.0051)*10**-3
def mittel(x):              #the real mean()-ing of life
    return ufloat(np.mean(x),np.std(x,ddof=1)/np.sqrt(len(x)))
def g(x,a,b):
    return a*x+b
def rkorr(n,v):
    return unp.sqrt(((B/(2*p))**2)+((9*n*v)/(2*const.g*rho)))-(B/(2*p))
def q(r,E):
    return ((4*np.pi/3)*rho*const.g*(r**3))/E

R, t, U = np.genfromtxt('millikan.txt', unpack = True)
# R thermo wiederstand in Mega Ohm
#t Zeit in s
# U SPannung in V
s = 0.5 #millimeter Kästchenlänge
s*= 10**-3 # in Metern
Tt , Rt = np.genfromtxt('ThermoWid.txt', unpack = True)
#Rt tabellen thermo wiederstand
#Tt tabellen Temperatur in C
T = np.array([]) # ist temperatur array
for r in R:
    for i,j in enumerate(Rt):
        if j<=r :
            T = np.append(T,Tt[i])
            break
E = np.absolute(U / d )# EFeld  im Kondensator berechnen
v = s/t # v null  Geschindigkeit ohne Feld

nT = np.array([16,17,18])
nn = np.array([1.805,1.81,1.814])
#Fit
nparams , ncov = curve_fit(g , nT ,nn )
nparams = correlated_values(nparams, ncov)
na,nb = nparams
n = np.array(g(T,na,nb)) #viskositäts array
n*=10**-5
Q = q(rkorr(n,v),E)
er = np.sort(rkorr(n,v))
Q = np.sort(Q)
# Niveaus Bestimmen
q0 = np.array([])
q1 = np.array([])
q2 = np.array([])
for q in Q:
    if q < 5e-20:
        q0 = np.append(q0,q)
    if q > 1.5e-19 and q < 2e-19:
        q1 = np.append(q1,q)
    if q > 3.5e-19 and q < 4e-19:
        q2 = np.append(q1,q)
q0 = np.mean(q0)
q1 = np.mean(q1)
q2 = np.mean(q2)
print('mittelwert von q1:',q1)
print('Mittelwert von q2:',q2)
print('Berechnete Elementarladung:',(q1 + (1/2)*q2)/2)
#Tabelle
# np.savetxt('millitab.txt',np.column_stack([(noms(v)),noms(T),noms(n)*10**5,noms(rkorr(n,v)),stds(rkorr(n,v)),noms(E)]), delimiter=' & ',newline= r'\\'+'\n' )
# #plt.subplot(1, 2, 1)
plt.plot(noms(er), noms(Q),'ro', label='Ladung')
# plt.axhline(y=4.5e-20 , color='g' , linestyle='--', label='Niveau 0')
plt.axhline(y=1.8e-19 , color='g' , linestyle='--', label='Niveau 1')
plt.axhline(y=3.8e-19 , color='b' , linestyle='--', label='Niveau 2')
plt.xlabel(r'$r / m$')
plt.ylabel(r'$Q / C$')
plt.grid()
plt.legend(loc='best')
# plt.show()
plt.savefig('milliplot.pdf')
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
