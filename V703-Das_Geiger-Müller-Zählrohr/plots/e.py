import matplotlib.pyplot as plt
import numpy as np
import uncertainties.unumpy as unp
from scipy.optimize import curve_fit
from uncertainties import correlated_values, correlation_matrix
from uncertainties import ufloat
from uncertainties.unumpy import (nominal_values as noms, std_devs as stds)
import scipy.constants as const
x = np.linspace(0, 10, 1000)
def mittel(x):              #the real mean()-ing of life
    return ufloat(np.mean(x),np.std(x,ddof=1)/np.sqrt(len(x)))
I, U , N = np.genfromtxt('VTae.txt', unpack = True)
t = 60 #seconds
I = I[1:]
U = U[1:]
N = N[1:]
#Umrechnen
I*=10**-6

Q = I*t/N
Z = Q/const.e
print(Z)
np.savetxt('etab.txt',np.column_stack([I,N,Q,Z*10**(-10)]), delimiter=' & ',newline= r'\\'+'\n' )
