import matplotlib.pyplot as plt
import numpy as np
import uncertainties.unumpy as unp
from scipy.optimize import curve_fit
from uncertainties import correlated_values, correlation_matrix
from uncertainties import ufloat
from uncertainties.unumpy import (nominal_values as noms, std_devs as stds)
# werte von T1 T2   messing
tm , anm , afm = np.genfromtxt('wT1T2.txt', unpack = True)  #periode 80s
pm = 8520
cm = 385
fm = 1/80
# were von T5T6 Aluminium
ta , ana , afa = np.genfromtxt('wT5T6.txt', unpack = True)  # periode 80s
pa = 2800
ca = 830
fa = 1/80
#werte von T7T8 eldelstahl
te , ane , afe = np.genfromtxt('wT7T8.txt', unpack = True) # periode 200s
pe = 8000
ce = 400
fe = 1/200
# delta x 0,03 m Abstand zwischen den Termoelementen
x = 0.03

def kappa(p,c , t , an ,af ):
    return (p*c*x**2)/(2*t*np.log(an/af))
km = np.mean(kappa(pm , cm , tm , anm , afm))
ka = np.mean(kappa(pa , ca , ta , ana , afa))
ke = np.mean(kappa(pe,ce , te, ane , afe)[1:])  # [1:] weil erster wert funkt nicht :(
print("Kappa von Messing:", km)
print("Kappa von Aluminium:", ka)
print("Kappa von Edelstahl:", ke)

def lam(k , f , p, c):
    return (1/f)*np.sqrt((4*np.pi * k * f)/(p*c))
print("Lambda für Messing:" ,lam(km , fm ,pm , cm))
print("Lambda für Aluminium:", lam(ka , fa, pa ,ca))
print("Lambda für Edelstahl:", lam(ke , fe ,pe ,ce))
wfm = 120
wfa = 236
wfe = 58

def rlerr(x ,y):
     return (np.absolute(x - y)/y)*100

print("relativer Fehler von kappa für Messing in %:",  rlerr(km , wfm))
print("relativer Fehler von kappa fürAluminium in %:", rlerr(ka , wfa))
print("relativer Fehler von kappa für Edelstahl in %:", rlerr(ke , wfe))
