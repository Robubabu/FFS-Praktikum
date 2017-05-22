
import matplotlib.pyplot as plt
import numpy as np
import uncertainties.unumpy as unp
from scipy.optimize import curve_fit
from uncertainties import correlated_values, correlation_matrix
from uncertainties import ufloat
from uncertainties.unumpy import (nominal_values as noms, std_devs as stds)


#Tabelle
# np.savetxt('tab.txt',np.column_stack([x,y]), delimiter=' & ',newline= r'\\'+'\n' )
#plt.subplot(1, 2, 1)


Imps=np.genfromtxt('../Messwerte/Statistik.txt')
Imps=Imps/10
plt.hist(Imps, normed = 1, bins = 10, facecolor='green', alpha=0.5)
n, bins, patches = plt.hist(Imps,normed= 1, bins = 10)

m = np.mean(Imps)
print('m: ',m)
print('bins: ', bins)
print('n: ', n)

def g(k,s):
    return 1/(s*np.sqrt(2*np.pi))*np.exp(-0.5*(k-m)**2/s**2)

def p(k,l,A):
    return A*l**k/np.math.factorial(k)*np.exp(-l)


r = range(len(n))
bims= np.array(r)    #halo i bims, 1 echter balken

for i in r:
    bims[i] = 0.5*(bins[i]+bins[i+1])

print('halo i bims, 1 echter balken: ',bims)

paramsG, covG = curve_fit(g, bims, n)
errorsG = np.sqrt(np.diag(covG))
print('halo i bims, 1 gauß: ', paramsG, '+/-', errorsG)


y = np.linspace(480,600)
plt.plot(y,g(y,*paramsG),'k--', label='Gauß seine Glocke')

#paramsP, covP = curve_fit(p,bims,n)
#plt.plot(y,p(y,*paramsP),'b--', label='Poisson seine Fairteilung')

plt.xlabel('Impacts/s')
plt.ylabel('Wahrscheinlichkeit')
plt.legend()
plt.savefig('Statistik.pdf')
plt.clf()
