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
def relf(l,m):
    return (np.absolute(l-m)/m)*100
cl = 2730 #meter pro secunde lit. Schallgeschw in Acryl
c1 = ufloat(2720,10)
c2 = ufloat(2717, 31)
cm = ufloat(2718,16)
print('relf der Impuls Echo Schallgeschw:', relf(cl,c1))
print('relf der Durchschall Schallgeschw:', relf(cl,c2))
print('relf der mittleren Schallgeschw:',relf(cl,cm))

p1l = 0.006
p1 = ufloat(0.005437,0.000033)
print('relf der ersten Platte:', relf(p1l,p1))

p2l = 0.01
p2 = ufloat(0.00816,0.00005)
print('relf der zweiten Platte:',relf(p2l,p2))
