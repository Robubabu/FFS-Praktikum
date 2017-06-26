import matplotlib.pyplot as plt
import numpy as np
import uncertainties.unumpy as unp
import scipy
from scipy.optimize import curve_fit
from uncertainties import correlated_values, correlation_matrix
from uncertainties import ufloat
from uncertainties.unumpy import (nominal_values as noms, std_devs as stds)
#x = np.linspace(0, 10, 1000)
def mittel(x):              #the real mean()-ing of life
    return ufloat(np.mean(x),np.std(x,ddof=1)/np.sqrt(len(x)))

def f(x,a,b):
    return a*x+b

#Fit
#params , cov = curve_fit(f , x ,y )
#params = correlated_values(params, cov)
#for p in params:
#    print(p)

u, i= np.genfromtxt('./fine.txt', unpack = True)
u =-u
#Tabelle
np.savetxt('fine_tab.txt',np.column_stack([u,i]), delimiter=' & ',newline= r'\\'+'\n' )

plt.plot(u, i, 'kx', label='578nm')

plt.xlabel(r'$U / V$')
plt.ylabel(r'$\sqrt{I / nA}$')
plt.legend(loc='best')
plt.savefig('fine.pdf')
plt.clf()

u, i= np.genfromtxt('./orange.txt', unpack = True)
u = -u

params, cov = curve_fit(f,u[22:32], np.sqrt(i[22:32]))
error = np.sqrt(np.diag(cov))

x = np.linspace(-0.5,0)
print('orange: ', params, error)

plt.clf()
plt.plot(u, np.sqrt(i), 'k.', label='578nm')
plt.plot(x, f(x,*params), 'k--', label = 'fit')
plt.xlabel(r'$U / V$')
plt.ylabel(r'$\sqrt{I / nA}$')
plt.legend(loc='best')
plt.savefig('orange.pdf')



u, i= np.genfromtxt('./gruen.txt', unpack = True)
u = -u
#Tabelle
np.savetxt('gruen_tab.txt',np.column_stack([u,i]), delimiter=' & ',newline= r'\\'+'\n' )

params, cov = curve_fit(f,u[22:32], np.sqrt(i[22:32]))
error = np.sqrt(np.diag(cov))

x = np.linspace(-0.5,0)
print('Gruen: ', params, error)

plt.clf()
plt.plot(u, np.sqrt(i), 'kx', label='546nm')
plt.plot(x, f(x,*params), 'k--', label = 'fit')
plt.xlabel(r'$U / V$')
plt.ylabel(r'$\sqrt{I / nA}$')
plt.legend(loc='best')
plt.savefig('gruen.pdf')


u, i= np.genfromtxt('./blau1.txt', unpack = True)
u = -u
#Tabelle
np.savetxt('blau1_tab.txt',np.column_stack([u,i]), delimiter=' & ',newline= r'\\'+'\n' )

params, cov = curve_fit(f,u[22:32], np.sqrt(i[22:32]))
error = np.sqrt(np.diag(cov))

x = np.linspace(-1.0,0)
print('Blau1: ', params, error)

plt.clf()
plt.plot(u, np.sqrt(i), 'kx', label='492nm')
plt.plot(x, f(x,*params), 'k--', label = 'fit')
plt.xlabel(r'$U / V$')
plt.ylabel(r'$\sqrt{I / nA}$')
plt.legend(loc='best')
plt.savefig('blau.pdf')

u, i= np.genfromtxt('./blau2.txt', unpack = True)
u = -u
#Tabelle
np.savetxt('blau2_tab.txt',np.column_stack([u,i]), delimiter=' & ',newline= r'\\'+'\n' )

params, cov = curve_fit(f,u[27:33], np.sqrt(i[27:33]))
error = np.sqrt(np.diag(cov))

x = np.linspace(-1.2,0)
print('Blau2: ', params, error)

plt.clf()
plt.plot(u, np.sqrt(i), 'kx', label='436nm')
plt.plot(x, f(x,*params), 'k--', label = 'fit')
plt.xlabel(r'$U / V$')
plt.ylabel(r'$\sqrt{I / nA}$')
plt.legend(loc='best')



plt.savefig('blau2.pdf')
plt.clf()

c = 3*10**8
ug = unp.uarray([0.45,0.53,1.01,1.18],[0.02,0.02,0.03,0.05])
v = np.array([c/578.0, c/546.0, c/492.0, c/435.0])
v = (1/1000)*v

params,cov = curve_fit(f,v,noms(ug))
error = np.sqrt(np.diag(cov))
print('h: ', params, error)
x = np.linspace(400,700)
plt.errorbar(v, noms(ug), yerr = stds(ug), fmt = 'kx', label = 'Grenzspannungen')
plt.plot(x, f(x,*params),'k--', label = 'fit')
plt.xlabel('f/kHz')
plt.ylabel('U/V')
plt.legend(loc = 'best')
plt.savefig('h.pdf')
