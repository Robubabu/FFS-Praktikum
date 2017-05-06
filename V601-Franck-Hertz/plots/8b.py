import matplotlib.pyplot as plt
import numpy as np
import uncertainties.unumpy as unp
from scipy.optimize import curve_fit
from uncertainties import correlated_values, correlation_matrix
from uncertainties import ufloat
from uncertainties.unumpy import (nominal_values as noms, std_devs as stds)
import scipy.constants as const
def mittel(x):              #the real mean()-ing of life
    return ufloat(np.mean(x),np.std(x,ddof=1)/np.sqrt(len(x)))
A = 2.3 # position erster Anregung in cm
s = np.genfromtxt('8b-Skalar.txt',  unpack = True) #10volt pro cm
a = np.genfromtxt('8b-Abs.txt', unpack = True) # abstände in cm
K = ufloat(1.11, 0.18)
m1= 2.3  #cm Abs von 0 bis zum ersten Maximum
ms = mittel(s)
ma = mittel(a)

print('Mittlerer Skalenabs:', ms)
print('Mittlerer Abs. in cm:', ma)
f = 10/ms       # Umrechnungsfaktor Volt pro cm
print(f)
av = ma*f
k = (m1*f) - av
print('Abs. des ersten MAximums von 0 in V:', m1*f)
print('Kontaktpotential der FHK in Volt:',k)
print('Mittlerer Abs. in V:',av)
Av = A*f - k
print('Beschleunigungsspannung der ersten Anregung in Volt:', Av)
Av*= const.e
print('Beschleunigungsenrgie in eV:', Av)
print('Wellenlänge des emittierten Lichts:' , const.c /(Av/const.h))
# np.savetxt('8btab1.txt',np.column_stack(s), delimiter=' & ',newline= r'\\'+'\n' )
# np.savetxt('steigung.txt',np.column_stack(a), delimiter=' & ',newline= r'\\'+'\n' )
