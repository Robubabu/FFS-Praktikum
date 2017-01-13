import matplotlib.pyplot as plt
import numpy as np
import uncertainties.unumpy as unp
from uncertainties import ufloat
from uncertainties.unumpy import (nominal_values as noms, std_devs as stds)
l,m = np.genfromtxt('Mittelwellenlaenge.txt', unpack = True)
lm = ufloat(l,m)
lm = 1/lm      # varianz ist 4
d,p = np.genfromtxt('dpropfak.txt', unpack =True)
dp = ufloat(d,p)        # varianz ist 13
v,a,r,b = np.genfromtxt('epropfak.txt', unpack = True)
va = ufloat(v,a)            #varianz ist 10
rb = ufloat(r,b)
rb*=-1           # varianz ist 10
def ttest(x , xerr,y ,yerr , vx ,vy):
    return ((x-y)/(np.sqrt(((xerr**2) / vx)+ ((yerr**2) / vy))))
def dftest(xerr , yerr , vx ,vy):
    return (((xerr**2 / vx)+ (yerr**2 / vy))**2 / ((((xerr**2 / vx)**2) /(vx-1)) +(((yerr**2 / vy)**2) /(vy-1))))
# lambda mit d
print('Test mit lambda und d:')
print('t:' , ttest(noms(lm),stds(lm), noms(dp), stds(dp), 4 , 13))
print('Freiheitsgerade df:', dftest(stds(lm) , stds(dp) , 4, 13))
# lambda mit c vor
print('Test mit lambda und d:')
print('t:' , ttest(noms(lm),stds(lm), noms(va), stds(va), 4 , 10))
print('Freiheitsgerade df:', dftest(stds(lm) , stds(va) , 4, 10))
# lambda mit c rueck
print('Test mit lambda und d:')
print('t:' , ttest(noms(lm),stds(lm), noms(rb), stds(rb), 4 , 10))
print('Freiheitsgerade df:', dftest(stds(lm) , stds(rb) , 4, 10))
