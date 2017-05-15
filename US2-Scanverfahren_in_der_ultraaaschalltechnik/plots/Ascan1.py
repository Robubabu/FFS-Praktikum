import matplotlib.pyplot as plt
import numpy as np
import uncertainties.unumpy as unp
from scipy.optimize import curve_fit
from uncertainties import correlated_values, correlation_matrix
from uncertainties import ufloat
from uncertainties.unumpy import (nominal_values as noms, std_devs as stds)


def mittel(x):              #the real mean()-ing of life
    return ufloat(np.mean(x),np.std(x,ddof=1)/np.sqrt(len(x)))

def refl(m,l):
    return np.absolute(m-l)/np.absolute(l) * 100

fb, tb = np.genfromtxt('Ascan_Block_B.txt', unpack = True) #enthält fehlstelle 10
fr , tr = np.genfromtxt('Ascan_Block_R.txt', unpack = True)    # die nicht
D , L = np.genfromtxt('Block.txt', unpack = True)
c = 2730 #meter pro sec
fb2, tb2 = np.genfromtxt('Ascan2_Block_B.txt', unpack = True)
fr2 , tr2 = np.genfromtxt('Ascan2_Block_R.txt', unpack = True)
bfb, btb1 , btb2 = np.genfromtxt('Bscan_Block_B.txt', unpack = True)
b4fb , b4tr1 , b4tr2 = np.genfromtxt('Bscan_Block_R4.txt', unpack = True)


#Umrechnen
D*=10**-2
tb*=10**-6
tr*=10**-6
tb2*=10**-6
tr2*=10**-6
btb1*= 10**-6
btb2*=10**-6
b4tr1*=10**-6
b4tr2*=10**-6
#Bestimmung des Fehlers für 1 Mhz Sonde
dtb = tb[-2] - (2*D/c)
dtr = tr[-1] - (2*D/c)
dt= np.array([dtb,dtr])
dt = mittel(dt)
print('Laufzeitkorrektur1:', dt)
#Bestimmung des Fehlers 2.0 für 4MHz Sonde
dtb2 = tb2[-1] - (2*D/c)
dtr2 = tr2[-1] - (2*D/c)
dt2 = np.array([dtb2,dtr2])
dt2 = mittel(dt2)
print('Laufzeitkorrektur2:',dt2)
#Bestimmung der Größe der Fehlstellen
def fg(tr,tb):
    return D - c/2 * (tr+tb -2*dt)
F=fg(tb[0:-2],tr[0:-1])
#Bestimmung der Größe der Fehlstellen 1,2
def fg2(tr,tb):
    return D - c/2 * (tr+tb -2*dt2)
F2 = fg2(tb2[0:-1], tr2[0:-1])
# Bestimmung Fehlstellen 11 bis 3 Bscan 1MhzSonde
BF1 = fg(btb1[0:-2],btb2[0:-2])
# BF1 = (c/2 )*(btb2[0:-2] - btb1[0:-2])
BF1 = np.absolute(BF1)
#Bestimmung Fehlstellen 1 und 2 BScan 4Mhz Sonde
DF2 = fg2(b4tr1[-2:], b4tr2[-2:])
# DF2 = (c/2) * (b4tr2[-2:] -b4tr1[-2:])
DF2 = np.absolute(DF2)
#relative Abweichung
B = np.append(BF1[2:], BF1[0])
B = np.append(B,DF2)
A = np.append(F[:-2],F2)
RF = refl(A,B)

#Tabelle
# np.savetxt('ABBtab.txt',np.column_stack([fb,tb]), delimiter=' & ',newline= r'\\'+'\n' )
# np.savetxt('ABRtab.txt',np.column_stack([fr,tr]), delimiter=' & ',newline= r'\\'+'\n' )
# np.savetxt('F1tab.txt',np.column_stack([fr[0:-1],tb[0:-2],tr[0:-1],noms(F)]), delimiter=' & ',newline= r'\\'+'\n' )
# np.savetxt('A2tab.txt',np.column_stack([fr2,tb2,tr2]), delimiter=' & ',newline= r'\\'+'\n' )
# np.savetxt('F2tab.txt',np.column_stack([fr2[0:-1],noms(F2),stds(F2)]), delimiter=' & ',newline= r'\\'+'\n' )
# np.savetxt('BF1tab.txt',np.column_stack([bfb[0:-2],btb1[0:-2],btb2[0:-2],noms(BF1),stds(BF1)]), delimiter=' & ',newline= r'\\'+'\n' )
# np.savetxt('BF2tab.txt',np.column_stack([b4fb[-2:],b4tr1[-2:], b4tr2[-2:],noms(DF2), stds(DF2)]), delimiter=' & ',newline= r'\\'+'\n' )











#
