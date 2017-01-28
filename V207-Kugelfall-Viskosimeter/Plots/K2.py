import matplotlib.pyplot as plt
import numpy as np
import uncertainties.unumpy as unp
from scipy.optimize import curve_fit
from uncertainties import correlated_values, correlation_matrix
from uncertainties import ufloat
from uncertainties.unumpy import (nominal_values as noms, std_devs as stds)
tk1 = np.genfromtxt('M1K1.txt', unpack = True)  #zeit von kugel 1 klein
tk2 = np.genfromtxt('M1K2.txt', unpack = True)  #"""""""" Kugel 2 groß
s = 0.1 #strecke
t1 = ufloat(np.mean(tk1), np.std(tk1 , ddof=1) / np.sqrt(len(tk1)))
t2 = ufloat(np.mean(tk2), np.std(tk2 , ddof=1) / np.sqrt(len(tk2)))
v1 = s / t1 #Geschw von K1
v2 = s / t2 #Geschw von K2
dk1 = np.genfromtxt('Eig-Kugel1.txt', unpack = True ) #kleine kugel
dk2 = np.genfromtxt('Eig-Kugel2.txt', unpack = True)    #große kugel
dk1/=1000
dk2/=1000
d1 = ufloat(np.mean(dk1), np.std(dk1 , ddof=1) / np.sqrt(len(dk1)))
d2 = ufloat(np.mean(dk2), np.std(dk2 , ddof=1) / np.sqrt(len(dk2)))
g1 = 4.45/1000
g2 = 4.95/1000
K1 = 0.07640*(1000/100**3)
def rerr(x ,y):
    return np.absolute(x-y)/y
def rho(g,d):
    return g/((4/3)*np.pi*(d/2)**3)
def nu(K,rho1, rho2 ,t):         #rho1 ist dichte der kugel 1 rho2 ist von wasser
    return K*(rho1 - rho2)*t
nu1 = nu(K1, rho(g1,d1) ,1000,t1)  # Viskosität mit einer wasser dichte von 1000 kg/ m**3
nu2 = nu(1,rho(g2,d2), 1000 , t2)
K2 = nu1 /nu2
r1 = rho(g1,d1)
r2 = rho(g2,d2)
rey1= (1000 * v1 * (d1/2))*1000/nu1
rey2 = (1000* v2 * (d2/2))*1000/nu(K2,rho(g2,d2),1000,t2)
print(rerr(nu1 , 1))
print("Fallgeschw. Kugel1:",v1)
print("Fallgeschw. Kugel2:", v2)
print("Reynoldszahl für Kugel 1:",rey1)
print("Reynoldszahl für Kugel 2:", rey2)
# print("Viskosität für die kleine Kugel 1:", nu1)
# print ("Apparatekonstante K1:", K1)
# print ("Apparatekonstante K2:", K2)
# print("Mittel des Durchmessers Kugel 1:" ,d1)
# print("Mittel des Durchmessers Kugel 2:",d2)
# print ("Dichte Kugel 1 klein:", r1)
# print("Dichte Kugel 2 groß:", r1)
# print("Mittel der Fallzeit Kugel 1:", t1)
# print("Mittel der Fallzeit Kugel 2:", t2)
