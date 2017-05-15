import matplotlib.pyplot as plt
import numpy as np
import uncertainties.unumpy as unp
from scipy.optimize import curve_fit
from uncertainties import correlated_values, correlation_matrix
from uncertainties import ufloat
from uncertainties.unumpy import (nominal_values as noms, std_devs as stds)

#the real mean()-ing of life:
#def mittel(x):
#    return ufloat(np.mean(x),np.std(x,ddof=1)/np.sqrt(len(x)))
theta2, imps = np.genfromtxt('../Messdaten/bragg.txt', unpack = True)
theta = theta2/2
h = 4.136*10**(-15) #eV
c = 2.998*10**8 #m/s'
d = 201.4*10**(-12)
E =2*h*c*d*np.sin(theta) #eV


plt.grid()
plt.plot(theta2, imps, 'bx')
plt.xlabel(r'$\gamma$')
plt.ylabel(r'$Imp \,/\, \mathrm{s}$')
plt.savefig('bragg.pdf')
