import matplotlib.pyplot as plt
import numpy as np
import uncertainties.unumpy as unp
from scipy.optimize import curve_fit
from uncertainties import correlated_values, correlation_matrix
from uncertainties import ufloat
from uncertainties.unumpy import (nominal_values as noms, std_devs as stds)

#the real mean()-ing of life
def mittel(x):
    return ufloat(np.mean(x),np.std(x,ddof=1)/np.sqrt(len(x)))
c1 = ufloat(2720,10)
c2 = ufloat(2717, 31)
c = np.mean([c1,c2])
print('Mittlere Schallgeschwindgkeit in Acryl:',c)
p, d = np.genfromtxt('SA2_Data.txt', unpack = True)
d*=10**(-6)
z = c/2 * (d[1]- d[0]) #Dicke des Zylinders
p1 = c/2 *(d[2]-d[1]) #Dicke der ersten Platte
print('Dicke der ersten Platte:',p1)
p2= c/2 * (d[3]-d[2])
print('Dicke der zweiten Platte:',p2)
