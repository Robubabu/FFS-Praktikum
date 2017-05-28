import matplotlib.pyplot as plt
import numpy as np
import uncertainties.unumpy as unp
from scipy.optimize import curve_fit
from uncertainties import correlated_values, correlation_matrix
from uncertainties import ufloat
from uncertainties.unumpy import (nominal_values as noms, std_devs as stds)
x = np.linspace(0, 10, 1000)
def mittel(x):              #the real mean()-ing of life
    return ufloat(np.mean(x),np.std(x,ddof=1)/np.sqrt(len(x)))
def relf(l,m):
    return (np.absolute(l-m)/l)*100
tZQM = ufloat(3,0.9)
tO = ufloat(232,8)
print('Relativer Fehler von t Oszi zu t Zwei Q M:', relf(tZQM,tO))
