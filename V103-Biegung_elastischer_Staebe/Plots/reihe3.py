import matplotlib.pyplot as plt
import numpy as np
import uncertainties.unumpy as unp
from scipy.optimize import curve_fit

x,y0,y1 = np.genfromtxt('../Werte/V103-Reihe3.txt', unpack = True)

x1 = np.array([3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 30])
x2 = np.array([30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 52, 54])

F = 4.7225*9.81
E = 1e8
I = 4.9e-10
L =0.575
d1 = F/(48*E*I)*(3*L**2*(x1/100)- 4*(x1/100)**3) #in mm
d2 = F/(48*E*I)*(4*(x2/100)**3-12*L*(x2/100)**2+ 9*(L**2)*(x2/100) - L**3) #in mm

plt.plot(x,y0, 'ko', label = 'Unbelastet')
plt.plot(x,y1, 'ro', label = 'Belastet')
plt.plot(x,y1-y0, 'go', label = 'Differenz')
plt.plot(x1, d1, 'y-', label = 'Theoriewert')
plt.plot(x2, d2, 'y-')

plt.grid()

plt.xlabel(r'$X \:/\: cm$')
plt.ylabel(r'$y \:/\: mm$')
plt.legend(loc='best')

plt.savefig('Reihe3.pdf')

x,y0,y1 = np.genfromtxt('../Werte/V103-Reihe3-1.txt', unpack = True)

E1 = F/(48*(y1-y0)*I)*(3*L**2*(x/100)- 4*(x/100)**3)

np.savetxt('V103-E31-tab.txt',np.column_stack([x,E1]), delimiter=' & ',newline= r'\\'+'\n' )
np.savetxt('V103-E31.txt',np.column_stack([x,E1]))

print('mean: ', np.mean(E1))
print('std: ', np.std(E1))


x,y0,y1 = np.genfromtxt('../Werte/V103-Reihe3-2.txt', unpack = True)
E2 = F/(48*(y1-y0)*I)*(4*(x/100)**3-12*L*(x/100)**2+ 9*(L**2)*(x/100) - L**3)


np.savetxt('V103-E32-tab.txt',np.column_stack([x,E2]), delimiter=' & ',newline= r'\\'+'\n' )
np.savetxt('V103-E32.txt',np.column_stack([x,E2]))

print('mean: ', np.mean(E2))
print('std: ', np.std(E2))
