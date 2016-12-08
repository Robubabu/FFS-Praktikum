import matplotlib.pyplot as plt
import numpy as np
import uncertainties.unumpy as unp
from scipy.optimize import curve_fit
from uncertainties import correlated_values, correlation_matrix
from uncertainties import ufloat



Uio,tio = np.genfromtxt('5awerteoben.txt', unpack= True)
Uiu,tiu = np.genfromtxt('5awerteunten.txt', unpack = True)
Uio/=1000
Uiu/= 1000
tiu/=1000000
tio/=1000000
U = np.append(Uio, Uiu)
t = np.append(tio ,tiu)
Uer= unp.uarray(U,5e-5)
ter= unp.uarray(t,1e-7)
#UUo = np.log((np.absolute(U[0 : -3])))

def f1(x , a ,b):
        return a*np.exp(-2*np.pi*x*b)


oparam , ocvar = curve_fit(f1, tio , Uio) #oben

uparam , ucvar = curve_fit(f1, tiu[3 : -1] , Uiu[3:-1]) #unten

oparams = correlated_values(oparam, ocvar)
uparams = correlated_values(uparam, ucvar)

print('Obere e Funktion Parameter A0 und myh:',uparams)
print('Obere e Funktion Parameter A0 und myh:',oparams)
umyh = uparams[1]
omyh = oparams[1]

myh= (umyh +  omyh)/2
print('Mittelwert aus mhy der oberen und unteren Einhuellenden:',myh)
R = ufloat(48.1, 0.1)
L = ufloat(10.11 ,0.03 )/1000
print('Tex = ',(1/(2*np.pi*myh)))
print('Reff=',(4*L*np.pi*myh))
print('Delta T =',((1/(2*np.pi*myh))-((2*L)/R)))
print('Delta R = ',((4*L*np.pi*myh)-R) )

plt.plot(t[0 : -3], UUo,'rx', label='Messwerte')
plt.plot(tio , f1(tio,oparam[0],oparam[1] ), 'g--', label = 'Obere Einhüllende')
plt.plot(tiu , f1(tiu,uparam[0] ,uparam[1] ), 'b--', label = 'Untere Einhüllende')
plt.xlabel(r'$t /s$')
plt.ylabel(r'$ U /V $')
plt.legend(loc='best')
#plt.savefig('build/5aplot.pdf')
#plt.show()
# # in matplotlibrc leider (noch) nicht möglich
# plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('5aplot.pdf')
# plt.show()
