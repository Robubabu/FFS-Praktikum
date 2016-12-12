import matplotlib.pyplot as plt
import numpy as np
import uncertainties.unumpy as unp
from scipy.optimize import curve_fit
from uncertainties import correlated_values, correlation_matrix
from uncertainties import ufloat
from uncertainties.unumpy import (nominal_values as noms, std_devs as stds)
#Einlesen
Uio,tio = np.genfromtxt('5awerteoben.txt', unpack = True)
Uiu, tiu = np.genfromtxt('5awerteunten.txt', unpack = True )
#Einheiten
Uio*=1e-3
Uiu*=1e-3
tio*=1e-6
tiu*=1e-6
#Zusammenfuegen und log der y Werte
Uio= np.log(Uio)
Uiu = Uiu[0:-3]
Uiu = np.absolute(Uiu)
Uiu = np.log(Uiu)
Uiu*=(-1)
tiu = tiu[0:-3]
U= np.append(Uio , Uiu)
t= np.append(tio ,tiu)

#Fit

def fit(x , a , b):
    return a*2*np.pi*x + b
oparams, ocav = curve_fit(fit , tio ,Uio )
uparams, ucav = curve_fit(fit , tiu[4:-1], Uiu[4:-1])
oparams = correlated_values(oparams , ocav)
uparams = correlated_values(uparams , ucav)
oa = oparams[0]
ob = oparams[1]
ua = uparams[0]
ub = uparams[1]
print('omhy:',oa)
print('oA0:', unp.exp(ob))
print('umhy:', ua)
print('uA0:', unp.exp(ub))
#Plot
x = np.linspace(0,0.001)
plt.plot(t, U, 'rx' , label= 'Messwerte')
plt.plot(x,fit(x , noms(oa) ,noms(ob)) ,'b--' , label='Fit der oberen Einhüllenden')
plt.plot(x, fit(x ,noms(ua), noms(ub)),'g--', label='Fit der unteren Einhüllenden')
plt.xlabel(r'$ t / s $')
plt.ylabel(r'$ln( U\:/\:V ) $')
plt.legend(loc='best')
#plt.savefig('5aplotreload.pdf')
plt.show()

R = ufloat(48.1 , 0.1)
L = ufloat(10.11 , 0.03)/1000
To =np.absolute((1/(2*np.pi*oa)))
Tu =np.absolute((1/(2*np.pi*ua)))
Ro =np.absolute((4*L*np.pi*oa))
Ru =np.absolute((4*L*np.pi*ua))
print('To=',To)
print('Tu=', Tu)
print('Ro=', Ro)
print('Ru=', Ru)
#InnenWiderstand abziehen
# Ru=Ru-50
# Ro=Ro-50
R= R+50
print('Delta To , Tu , Ro , Ru')
dTo=(To-((2*L)/R))/((2*L)/R)
dTu=(Tu-((2*L)/R))/((2*L)/R)
dRo=(Ro-R)/R
dRu=(Ru-R)/R
print(dTo)
print(dTu)
print(dRo)
print(dRu)




























#
