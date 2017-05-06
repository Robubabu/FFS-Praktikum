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
def relf(l,m):
    return np.absolute((l-m)/l)*100
ul = 4.9 # lit Wert der Anregungserngie in eV
um = ufloat(4.94 , 0.15) #mess wert in eV

wl = 253 #lit wellenlänge des emittierten lichts in nm
wm = ufloat(251,8) # messwert in nm
il = 10.437
im = ufloat(11.9 , 0.8)

print('rel. Fehler in Prozent der Ionisierungsspannung:', relf(il,im))
print('rel. Fehler in Prozent der Anregungsenergie:', relf(ul,um))
print('rel. Fehler in Prozent der Wellenlänge:', relf(wl,wm))
