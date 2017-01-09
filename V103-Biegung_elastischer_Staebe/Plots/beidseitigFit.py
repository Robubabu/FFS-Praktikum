import matplotlib.pyplot as plt
import numpy as np
import uncertainties.unumpy as unp
from scipy.optimize import curve_fit
from uncertainties import ufloat

x,y0,y1 = np.genfromtxt('../Werte/V103-Reihe3-1.txt', unpack = True)
x = x/100
y0 = y0/1000
y1 = y1/1000

F = 4.7225*9.81
E = 9.7e10
I = 4.9e-10
L =0.575
d = F/(48*E*I)*(3*L**2*(x)- 4*(x)**3)#in mm

z = 3*L**2*x-4*x**3

def f(t, a, b):
    return a*t + b
parameters, pcov = curve_fit(f, z, (y1-y0))
print(parameters, np.sqrt(np.diag(pcov)), sep='\n')

a = ufloat(0.01958625, 7.36393738e-4)

E =F/(48*I*a)

print('E: ', E)

plt.plot(z,y0, 'kx', label = 'Unbelastet')
plt.plot(z,y1, 'rx', label = 'Belastet')
plt.plot(z,y1-y0, 'gx', label = 'Differenz')
plt.plot(z, f(z, *parameters), 'g--', label = 'fit')
plt.plot(z, d, 'y-', label = 'Theoriewert')


plt.grid()

plt.xlabel(r'$3L^3x-4x^3 \:/\: m^3$')
plt.ylabel(r'$y \:/\: m$')
plt.legend(loc='best')
plt.savefig('beidseitigFit.pdf')
