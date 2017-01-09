import matplotlib.pyplot as plt
import numpy as np
import uncertainties.unumpy as unp
from scipy.optimize import curve_fit

x,y0,y1 = np.genfromtxt('../Werte/V103-Reihe1.txt', unpack = True)
x = x/100
y0 = y0/1000
y1 = y1/1000
F = 0.2389*9.81
E = 9.7e10
I = 4.9e-10
L =0.575
d = F/(2*E*I)*(L*(x)**2 - (x)**3/3) #in mm

def f(t, a, b):
    return a * t**2 - b*t**3
parameters, pcov = curve_fit(f, x, y1-y0)
print(parameters, np.sqrt(np.diag(pcov)), sep='\n')

#plt.plot(x,y0, 'ko', label = 'Unbelastet')
#plt.plot(x,y1, 'ro', label = 'Belastet')
#plt.plot(x,y1-y0, 'go', label = 'Differenz')
#plt.plot(x, f(x, *parameters), 'g--', label = 'fit')
#plt.plot(x, d, 'y-', label = 'Theoriewert')

z = L * (x)**2 -(x)**3/3

def g(t, a, b):
    return a * t + b
parameters, pcov = curve_fit(g, z, (y1-y0))
print(parameters, np.sqrt(np.diag(pcov)), sep='\n')

plt.plot(z,y0, 'kx', label = 'Unbelastet')
plt.plot(z,y1, 'rx', label = 'Belastet')
plt.plot(z,y1-y0, 'gx', label = 'Differenz')
plt.plot(z, g(z, *parameters), 'g--', label = 'fit')
plt.plot(z, d, 'y-', label = 'Theoriewert')

a = unp.uarray(parameters[0], parameters[1])
E =F/(2*a*I)

print('E: ', E)

plt.grid()

plt.xlabel(r'$X \:/\: m^3$')
plt.ylabel(r'$y \:/\: m$')
plt.legend(loc='best')

plt.savefig('Reihe1.pdf')

E = F/(2*((y1-y0))*I)*(L*(x)**2-(x)**3/3)

#np.savetxt('V103-E1-tab.txt',np.column_stack([x,E]), delimiter=' & ',newline= r'\\'+'\n' )
#np.savetxt('V103-E1.txt',np.column_stack([x,E]))

print('mean: ', np.mean(E))
print('std: ', np.std(E))
