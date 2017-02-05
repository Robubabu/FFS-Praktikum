import numpy as np
import uncertainties.unumpy as unp
from uncertainties import ufloat
from uncertainties.unumpy import (nominal_values as noms,
                                  std_devs as stds)

mcu =0.37865 - 0.14005 #Masse Kupfer
mgr = 0.24765 -0.13977 #Masse Graphit
mpb = 0.68437 - 0.14007 #Masse Blei

cw = 4200 #Wärmekapazität Wasser in J/(kg K)

U0 = ufloat(-0.955, 0.001) #T = 273.15K (in mV)
U100 = ufloat(0.667, 0.009) #T = 373.15K (in mV)

a = 100/(U100-U0) #K/mV
b =- a*U0 + 273.15 # T(U0) wird auf 273.15K gesetzt

def T(u):
    return a*u + b


#print(a, b)
#print(T(U0))
#print(T(U100))

my = 0.3
Tx = T(ufloat(-0.557, 0.001))
mx = 0.3
Ty = T(ufloat(0.510, 0.001))
Tm = T(ufloat(-0.103, 0.001))

g = cw*my*(Ty-Tm)/(Tm-Tx) - cw*mx #g ist eigentlich cgmg
print('cgmg = ',g)
#print(Tx)
#print(Ty)
#print(Tm)

mw = 0.6
Upb, Uw, Um = np.genfromtxt('./Blei.txt', unpack = True)
Tpb = T(unp.uarray(Upb, [0.001, 0.001, 0.001]))
Tw = T(unp.uarray(Uw, [0.001, 0.001, 0.001]))
Tm = T(unp.uarray(Um, [0.001, 0.001, 0.001]))

cpb = (cw*mw + g)*(Tm-Tw)/(mpb*(Tpb-Tm))

print('Tpb:', Tpb)
print('Tw:', Tw)
print('Tm:', Tm)
print('-----------------------')
#print('Cpb = ', noms(cpb), '+/-', stds(cpb))

mw = 0.6
Ugr, Uw, Um = np.genfromtxt('./Graphit.txt', unpack = True)
Tgr = T(unp.uarray(Ugr, [0.001, 0.001, 0.001]))
Tw = T(unp.uarray(Uw, [0.001, 0.001, 0.001]))
Tm = T(unp.uarray(Um, [0.001, 0.001, 0.001]))

cgr = (cw*mw + g)*(Tm-Tw)/(mgr*(Tgr-Tm))

print('Tgr:', Tgr)
print('Tw:', Tw)
print('Tm:', Tm)
print('-----------------------')
#print('Cgr = ',noms(cgr), '+/-', stds(cgr))

mw = 0.6
Ucu, Uw, Um = np.genfromtxt('./Kupfer.txt', unpack = True)
Tcu = T(unp.uarray(Ucu, [0.001]))
Tw = T(unp.uarray(Uw, [0.001]))
Tm = T(unp.uarray(Um, [0.001]))


ccu = (cw*mw + g)*(Tm-Tw)/(mcu*(Tcu-Tm))

print('Tcu:', Tcu)
print('Tw:', Tw)
print('Tm:', Tm)
print('-----------------------')
#print('Ccu = ',noms(ccu), '+/-', stds(ccu))
