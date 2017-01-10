import matplotlib.pyplot as plt
import numpy as np
import uncertainties.unumpy as unp
from uncertainties import ufloat
l,m = np.genfromtxt('Mittelwellenlaenge.txt', unpack = True)
lm = ufloat(l,m)
d,p = np.genfromtxt('dpropfak.txt', unpack =True)
dp = ufloat(d,p)
v,a,r,b = np.genfromtxt('epropfak.txt', unpack = True)
va = ufloat(v,a)
rb = ufloat(r,b)
print(lm , va , rb )
    
