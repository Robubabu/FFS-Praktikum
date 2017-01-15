import matplotlib.pyplot as plt
import numpy as np
import uncertainties.unumpy as unp
from scipy.optimize import curve_fit
from uncertainties import correlated_values, correlation_matrix
from uncertainties import ufloat
from uncertainties.unumpy import (nominal_values as noms, std_devs as stds)
#Wärmeleitfähigkeiten
wfm = 120       #Messing
wfa = 236       #Alu
wfe = 58        #Stahl unlegiert
#temperaturen
t , dm , de = np.genfromtxt('dwerte.txt', unpack =True)
# waermestrom rechner nimmt kappa Querfläche und Temp.diff
# Querschnittsfläche
A = 0.012*0.004 #für beide gleich
def wflux(k, T ):
    return -k*A*(T/0.03)
wm = wflux(wfm,dm)
we = wflux(wfe, de)
np.savetxt('waermestromtab.txt', np.column_stack([t , dm , wm, de , we]), \
            delimiter = ' & ', newline ='\\'+' \n')
