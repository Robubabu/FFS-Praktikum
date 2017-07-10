import matplotlib.pyplot as plt
import numpy as np
import uncertainties.unumpy as unp
from scipy.optimize import curve_fit
from uncertainties import correlated_values, correlation_matrix
from uncertainties import ufloat
from uncertainties.unumpy import (nominal_values as noms, std_devs as stds)

def mittel(x):              #the real mean()-ing of life
    return ufloat(np.mean(x),np.std(x,ddof=1)/np.sqrt(len(x)))


U, I = np.genfromtxt('./Reihe1.txt', unpack = True)
np.savetxt('Reihe1_tab.txt', np.column_stack([U,I]), delimiter = ' & ',newline= r'\\'+'\n' )
plt.plot(U, I, 'k.')
plt.ylabel(r'$I/mA$')
plt.xlabel(r'$U/V$')
plt.xlim(-1,200)
plt.ylim(-0.001,0.013)
plt.grid()
plt.savefig('Plot1.pdf')
plt.clf()

U, I = np.genfromtxt('./Reihe2.txt', unpack = True)
np.savetxt('Reihe2_tab.txt', np.column_stack([U,I]), delimiter = ' & ',newline= r'\\'+'\n' )
plt.plot(U, I, 'k.')
plt.ylabel(r'$I/mA$')
plt.xlabel(r'$U/V$')
plt.ylim(-0.001,0.025)
plt.grid()
plt.savefig('Plot2.pdf')
plt.clf()

U, I = np.genfromtxt('./Reihe3.txt', unpack = True)
np.savetxt('Reihe3_tab.txt', np.column_stack([U,I]), delimiter = ' & ',newline= r'\\'+'\n' )
plt.plot(U, I, 'k.')
plt.ylabel(r'$I/mA$')
plt.xlabel(r'$U/V$')
plt.xlim(-1,251)
plt.grid()
plt.savefig('Plot3.pdf')
plt.clf()

U, I = np.genfromtxt('./Reihe4.txt', unpack = True)
np.savetxt('Reihe4_tab.txt', np.column_stack([U,I]), delimiter = ' & ',newline= r'\\'+'\n' )
plt.plot(U, I, 'k.')
plt.ylabel(r'$I/mA$')
plt.xlabel(r'$U/V$')
plt.xlim(-1, 101)
plt.ylim(-0.001,0.16)
plt.grid()
plt.savefig('Plot4.pdf')
plt.clf()

U, I = np.genfromtxt('./Reihe5.txt', unpack = True)
np.savetxt('Reihe5_tab.txt', np.column_stack([U,I]), delimiter = ' & ',newline= r'\\'+'\n' )
plt.plot(U, I, 'k.')
plt.ylabel(r'$I/mA$')
plt.xlabel(r'$U/V$')
plt.xlim(-1,251)
plt.grid()
plt.savefig('Plot5.pdf')
plt.clf()

U = np.log(U)
I = np.log(I)

def g(x,a,b):
    return a*x+b

params, cov = curve_fit(g,U[0:6], I[0:6])
error = np.sqrt(np.diag(cov))
print('P: ', params, ' +/- ', error)

plt.plot(U[0:6], g(U[0:6], *params), 'k-', label = 'Ausgleichsgerade')
plt.plot(U, I, 'k.', label = 'Messwerte')
plt.ylabel(r'$ln(I/mA)$')
plt.xlabel(r'$ln(U/V)$')
plt.grid()
plt.legend(loc = 'best')
plt.savefig('langmuir.pdf')
plt.clf()


U, I = np.genfromtxt('Reihe6.txt', unpack = True)
U = U
I = I*1e6
np.savetxt('Reihe6_tab.txt', np.column_stack([U,I]), delimiter = ' & ',newline= r'\\'+'\n' )
params, cov = curve_fit(g,U[0:9], np.log(I[0:9]))
error = np.sqrt(np.diag(cov))
a = ufloat(params[0],error[0])
k = 8.6e-5
e = 1.6e-19
T = 1/(k*a)
print('P-Anlauf: ', params, error)
print('T5: ',U, T)

print('Anlauf: ', params, '+/-', error)
plt.plot(U, np.log(I), 'k.', label = 'Messwerte')
plt.plot(U[0:9], g(U[0:9], *params), 'k-', label = 'Ausgleichsgerade')
plt.ylabel(r'$ln(I/nA)$')
plt.xlabel(r'$U/V$')
plt.legend(loc = 'best')
plt.grid()
plt.savefig('Plot6.pdf')
plt.clf()

f = (0.35)
n = 0.28
s = 5.7e-12
I = np.array([1.8,1.9,2.0,2.1, 2.2])
U = np.array([3.5,4,4.5,4.5, 5])
N = 1
h = 4.14e-15
m = 9.1e-31
print('N: ', N)
T = ((I*U-N)/(f*n*s))**0.25
print('T: ', T)
P = k*T*np.log(I*h**3/(4*np.pi*e*m*k**2*T**2))
print('Phi: ', P)
print('mittel: ', mittel(P))
