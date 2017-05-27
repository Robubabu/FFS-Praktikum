import matplotlib.pyplot as plt
import numpy as np
import uncertainties.unumpy as unp
from scipy.optimize import curve_fit
from uncertainties import correlated_values, correlation_matrix
from uncertainties import ufloat
from uncertainties.unumpy import (nominal_values as noms, std_devs as stds)
def mittel(x):              #the real mean()-ing of life
    return ufloat(np.mean(x),np.std(x,ddof=1)/np.sqrt(len(x)))
z,N = np.genfromtxt('VTd.txt', unpack = True)
n = unp.uarray(N, np.sqrt(N))
n1 = n[0]
n12 = n[1]
n2 = n[2]
t = (n1 + n2 - n12)/(2*n1*n2)
print('Totzeit t=', t*10**6)
