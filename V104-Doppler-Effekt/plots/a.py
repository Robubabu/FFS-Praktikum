import matplotlib.pyplot as plt
import numpy as np
import uncertainties.unumpy as unp
from scipy.optimize import curve_fit
from uncertainties import correlated_values, correlation_matrix
from uncertainties import ufloat
from uncertainties.unumpy import (nominal_values as noms, std_devs as stds)

v1 , v2 , v3 , v4 , v5 , v6 , v7 , v8 , v9 , v0 = np.genfromtxt('avor.txt' ,unpack = True)
r1 , r2, r3, r4, r5, r6, r7, r8, r9, r0 =np.genfromtxt('arueck.txt', unpack = True)
s = ufloat(0.43,0.0002)    #Strecke 43 cm mit 0,2 mm Fehler :/

V = np.array([v1,v2,v3,v4,v5,v6,v7,v8,v9,v0])
R = np.array([r1,r2,r3,r4,r5,r6,r7,r8,r9,r0])
gv = unp.uarray       #Geschw. vorwärts
gr = unp.uarray       #Geschw. rückwärts
for v in V:
    v*=1e-2
    gv = np.append(gv,np.mean(v))
gv=gv[1:]
gv = s/gv

for r in R:
    r*=1e-2
    gr = np.append(gr, np.mean(r))
gr = gr[1:]
gr = s/gr
x = np.linspace(1,10, num=10)
np.savetxt('GangGeschwVorRueck4Tab.txt',
np.column_stack([x,noms(gv), stds(gv),-noms(gr),-stds(gr)]),
header='Gang/MittelGeschwVor/FehlerVor/MittelGeschwRueck/FehlerRueck/inMeterproSek')


#
# x= np.linspace(1,10,num=10)
# np.savetxt('GeschwMittelproGang.txt',y,header='#inMeterproSekund')
#
# Plot der Geschw. im arith. Mittel
# plt.plot(x , y,'rx', label='arith. Mittel der gemessenen Geschwindigkeiten')
# plt.xlabel(r'$ Gäng\;der\; Versuchsapparatur$')
# plt.ylabel(r'$ v\:/\:ms^{-1}$')
# plt.xlim(0,11)
# plt.legend(loc='best')
# print((c/np.mean(v0)))
# plt.show()
# plt.savefig('build/plot.pdf')
