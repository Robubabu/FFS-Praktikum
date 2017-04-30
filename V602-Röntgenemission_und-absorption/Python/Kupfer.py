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
theta2, imps = np.genfromtxt('../Messdaten/Cu.txt', unpack = True)
theta = theta2/2
h = 4.136*10**(-15) #eVs
c = 2.998*10**8 #m/s'
d = 201.4*10**(-12)
E =h*c/(2*d*np.sin(2*np.pi*theta/360)) #eV
plt.plot(E[68:]/1000, imps[68:], 'rx', label = 'Kupfer')
plt.plot([E[68+23]/1000,E[68+23]/1000],[0,250], 'r--', label = r'$K_\beta$')
plt.plot([E[68+12]/1000,E[68+12]/1000],[0,250], 'r-', label = r'$K_\alpha$')

print('Ka: ', E[68+12]/1000)
print('Kb: ', E[68+23]/1000)

plt.grid()
plt.xlabel(r'$E /\mathrm{keV}$')
plt.ylabel(r'$Imp \,/\, \mathrm{s}$')
plt.legend()
plt.savefig('Kupfer.pdf')
