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

 #numpy.savetxt('./Messdaten/braggE.txt', np.column_stack([theta, E]))
