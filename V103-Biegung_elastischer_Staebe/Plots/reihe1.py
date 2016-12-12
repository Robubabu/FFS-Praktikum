import matplotlib.pyplot as plt
import numpy as np
import uncertainties.unumpy as unp
from scipy.optimize import curve_fit

x,y0,y1 = np.genfromtxt('../Werte/V103-Reihe1.txt', unpack = True)
F = 0.3792
E = 8470
I = 6.17e-9
L =0.575
#d = F/(2*E*I)(L*x^2 - x^3/3)/1000 #in mm

def f(t, a, b):
    return a * t^2 - b*t^3
parameters, pcov = curve_fit(f, x, y1-y0)
print(parameters, np.sqrt(np.diag(pcov)), sep='\n')

plt.plot(x,y0, 'ko', label = 'Unbelastet')
plt.plot(x,y1, 'ro', label = 'Belastet')
plt.plot(x,y1-y0, 'go', label = 'Differenz')
plt.plot(x, f(x, *parameters), 'g--', label = 'fit')
#plt.plot(x, d, 'y-', label = 'Theoriewert')



plt.xlabel(r'$X \:/\: cm$')
plt.ylabel(r'$y \:/\: mm$')
plt.legend(loc='best')

plt.savefig('Reihe1.pdf')
