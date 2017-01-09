import matplotlib.pyplot as plt
import numpy as np
import uncertainties.unumpy as unp
from scipy.optimize import curve_fit

x,y0,y1 = np.genfromtxt('../Werte/V103-Reihe3.txt', unpack = True)
x = x/100
y0 = y0/1000
y1 = y1/1000

x1 = np.array([3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 30])
x2 = np.array([30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 52, 54])
x1 = x1/100
x2 = x2/100

F = 4.7225*9.81
E = 9.7e10
I = 4.9e-10
L =0.575
d1 = F/(48*E*I)*(3*L**2*(x1)- 4*(x1)**3)#in mm
d2 = F/(48*E*I)*(4*(x2)**3-12*L*(x2)**2+ 9*(L**2)*(x2) - L**3) #in mm

plt.plot(x,y0, 'ko', label = 'Unbelastet')
plt.plot(x,y1, 'ro', label = 'Belastet')
plt.plot(x,y1-y0, 'go', label = 'Differenz')
plt.plot(x1, d1, 'y-', label = 'Theoriewert')
plt.plot(x2, d2, 'y-')

x,y0,y1 = np.genfromtxt('../Werte/V103-Reihe3-1.txt', unpack = True)

E1 = F/(48*(y1-y0)*I)*(3*L**2*(x/100)- 4*(x/100)**3)

np.savetxt('V103-E31-tab.txt',np.column_stack([x,E1]), delimiter=' & ',newline= r'\\'+'\n' )
np.savetxt('V103-E31.txt',np.column_stack([x,E1]))

def f(t, a, b):
    return a * t - b*t**3
params1, pcov = curve_fit(f, x, y1-y0)
print(params1, np.sqrt(np.diag(pcov)), sep='\n')


print('mean: ', np.mean(E1))
print('std: ', np.std(E1))
#plt.plot(x, f(x, *params1), 'g--', label = 'fit x<27')

x,y0,y1 = np.genfromtxt('../Werte/V103-Reihe3-2.txt', unpack = True)
E2 = F/(48*(y1-y0)*I)*(4*(x/100)**3-12*L*(x/100)**2+ 9*(L**2)*(x/100) - L**3)

def g(t, a, b, c, d):
    return a * t**3 - b*t**2 - c*t - d
params2, pcov = curve_fit(f, x, y1-y0)
print(params2, np.sqrt(np.diag(pcov)), sep='\n')

np.savetxt('V103-E32-tab.txt',np.column_stack([x,E2]), delimiter=' & ',newline= r'\\'+'\n' )
np.savetxt('V103-E32.txt',np.column_stack([x,E2]))

print('mean: ', np.mean(E2))
print('std: ', np.std(E2))
#plt.plot(x, g(x, *params2), 'g.-', label = 'fit x>27')


plt.grid()

plt.xlabel(r'$x \:/\: m$')
plt.ylabel(r'$y \:/\: m$')
plt.legend(loc='best')
plt.savefig('Reihe3.pdf')
