import matplotlib.pyplot as plt
import numpy as np
import uncertainties.unumpy as unp
from scipy.optimize import curve_fit

x,y0,y1 = np.genfromtxt('../Werte/V103-Reihe2.txt', unpack = True)

F = 0.7675*9.81
E =9.7e10
I = 8.3e-10
L =0.6
d = F/(2*E*I)*(L*(x/100)**2 - (x/100)**3/3) *1000#in mm

def f(t, a, b):
    return a * t**2 - b*t**3
parameters, pcov = curve_fit(f, x, y1-y0)
print(parameters, np.sqrt(np.diag(pcov)), sep='\n')

plt.plot(x,y0, 'ko', label = 'Unbelastet')
plt.plot(x,y1, 'ro', label = 'Belastet')
plt.plot(x,y1-y0, 'go', label = 'Differenz')
plt.plot(x, d, 'y-', label = 'Theoriewert')
plt.plot(x, f(x, *parameters), 'g--', label = 'fit')

plt.grid()

plt.xlabel(r'$X \:/\: cm$')
plt.ylabel(r'$y \:/\: mm$')
plt.legend(loc='best')

plt.savefig('Reihe2.pdf')


E = F/(2*(y1-y0)*I)*(L*(x/100)**2-(x/100)**3/3)

np.savetxt('V103-E2-tab.txt',np.column_stack([x,E]), delimiter=' & ',newline= r'\\'+'\n' )
np.savetxt('V103-E2.txt',np.column_stack([x,E]))

print('mean: ', np.mean(E))
print('std: ', np.std(E))
