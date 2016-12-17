import matplotlib.pyplot as plt
import numpy as np
import uncertainties.unumpy as unp
from scipy.optimize import curve_fit
from uncertainties import correlated_values, correlation_matrix
from uncertainties import ufloat
from uncertainties.unumpy import (nominal_values as noms, std_devs as stds)

berg , tal = np.genfromtxt('c2.txt' , unpack= True) # in mm
f = np.genfromtxt('b.txt', unpack = True)   #in 1/10s
berg= unp.uarray(berg, 0.2) #fehler von 0.2 mm
tal = unp.uarray(tal, 0.2)
berg*=1e-3
tal*=1e-3
f*=1e-1

lamb = unp.uarray(
noms([berg[-1]-berg[-2], berg[-2]-berg[-3], tal[-1]-tal[-2],tal[-2]-tal[-3]]),
stds([berg[-1]-berg[-2], berg[-2]-berg[-3], tal[-1]-tal[-2],tal[-2]-tal[-3]]))
#lamb = Wellenlänge berg-berg
lm = np.mean(lamb)  #arithmetisches Mittel der Wellenlänge
# print(np.mean(lamb))
np.savetxt('Mittelwellenlaenge.txt',np.column_stack([noms(lm),stds(lm)]),header='#inMeter #fehler')
