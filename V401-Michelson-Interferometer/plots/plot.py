import matplotlib.pyplot as plt
import numpy as np
import uncertainties.unumpy as unp
from scipy.optimize import curve_fit
from uncertainties import correlated_values, correlation_matrix
from uncertainties import ufloat
from uncertainties.unumpy import (nominal_values as noms, std_devs as stds)
x = np.linspace(0, 10, 1000)
def mittel(x):              #the real mean()-ing of life
    return ufloat(np.mean(x),np.std(x,ddof=1)/unp.sqrt(len(x)))

#Fit
#params , cov = curve_fit(f , x ,y )
#params = correlated_values(params, cov)
#for p in params:
#    print(p)


#Tabelle
# np.savetxt('tab.txt',np.column_stack([x,y]), delimiter=' & ',newline= r'\\'+'\n' )
#plt.subplot(1, 2, 1)

####################################################################
#########           WAVELENGTH        ##############################
####################################################################

startCount, endCount, startX, endX = np.genfromtxt('lambda.txt', unpack = True)
x = endX - startX
x = x*10**6 #x in nm
j = np.linspace(0,len(x)-1, len(x))
for i in j:
    if(x[i]<0):
        x[i] = -1*x[i]
count = endCount - startCount


length = 2*x/(count)/5.017 #lever
print('wavelength: ', length)

middleLength = mittel(length)
print('middleLength: ', middleLength)


np.savetxt('lambda_tab.txt',np.column_stack([count, x, length]), delimiter=' & ',newline= r'\\'+'\n' )

#########################################################################
##################### BREAKING BAD ######################################
#########################################################################


startCountAir, endCountAir = np.genfromtxt('Luft.txt', unpack = True)
countAir = endCountAir - startCountAir
pAir = 0.8
pGas, startCountGas, endCountGas = np.genfromtxt('Gas.txt', unpack = True)
countGas = endCountGas-startCountGas

dnAir = countAir * middleLength / (2*50*10**6)
dnGas = countGas * middleLength / (2*50*10**6)

dnAir0 = dnAir * 298.15/273.15*1.0132/pAir
dnGas0 = dnGas * 298.15/273.15*1.0132/pGas

np.savetxt('N_tab.txt',np.column_stack([countAir,  noms(dnAir), stds(dnAir), pGas, countGas, noms(dnGas), stds(dnGas)]), delimiter=' & ',newline= r'\\'+'\n' )
print(len(countAir), len(dnAir), len(pGas), len(countGas), len(dnGas))
print('Delta N Air: ' , mittel(noms(dnAir0)))
print('Delta N Gas: ' , mittel(noms(dnGas0)))
#plt.plot(x, y, label='Kurve')
#plt.xlabel(r'$\alpha \:/\: \si{\ohm}$')
#plt.ylabel(r'$y \:/\: \si{\micro\joule}$')
#plt.legend(loc='best')
#plt.savefig('build/Wavelength.pdf')
#plt.clf()

####################################################################
####################################################################
####################################################################
