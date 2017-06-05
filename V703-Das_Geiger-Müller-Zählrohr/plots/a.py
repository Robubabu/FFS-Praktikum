import matplotlib.pyplot as plt
import numpy as np
import uncertainties.unumpy as unp
from scipy.optimize import curve_fit
from uncertainties import correlated_values, correlation_matrix
from uncertainties import ufloat
from uncertainties.unumpy import (nominal_values as noms, std_devs as stds)
x = np.linspace(0, 1000, 1000)
def mittel(x):              #the real mean()-ing of life
    return ufloat(np.mean(x),np.std(x,ddof=1)/np.sqrt(len(x)))
I, U , N = np.genfromtxt('VTae.txt', unpack = True)
t = 60 #Sekunden Messdauer
A = unp.uarray(N/t, np.sqrt(N/t))

def fit(x,a,b):
    return a*x+b

#Fit
params , cov = curve_fit(fit , U[4:] ,noms(A[4:] ))
params = correlated_values(params, cov)
a = params[0]
b = params[1]
c = unp.arctan(noms(a))

print('Steigung a =',a)
print('Steigung a in Prozent:', c)
print('y-Abschnitt b = ', b)
#Tabelle
# np.savetxt('atab.txt',np.column_stack([U,noms(A), stds(A)]), delimiter=' & ',newline= r'\\'+'\n' )
# plt.subplot(2, 1, 1)
# # plt.plot(U, N,'bx' ,label='Charakteristik')
# plt.errorbar(U, noms(A), yerr=stds(A), fmt='rx', label='Charakteristik')
# plt.plot(x, fit(x,noms(a),noms(b)), label='Ausgleichsgerade (Plateau)')
# plt.grid()
# # plt.xlabel(r'$U \:/\: V$')
# plt.ylabel(r'$N$')
# plt.xlim(400,900)
# plt.ylim(-1000,55000)
# plt.axvline(x=470, ls = '--' , label='Auslösespannung', c='g')
# plt.legend(loc='best')
# plt.savefig('build/plot.pdf')
# plt.clf()
# plt.subplot(2, 1, 2)
plt.errorbar(U[2:], noms(A[2:]), yerr=stds(A[2:]), fmt='rx', label='Charakteristik(Plateau)')
plt.plot(x, fit(x,noms(a),noms(b)), label='Ausgleichsgerade(Plateau)')
plt.xlim(400,900)
# plt.ylim(46500,51500)
plt.axvline(x=490, ls = '--' , label='Auslösespannung', c='g')

plt.grid()
plt.xlabel(r'$U \:/\: V$')
plt.ylabel(r'$\frac{N}{t} \; / Bq$')
plt.legend(loc='best')

# plt.show()
#
# # in matplotlibrc leider (noch) nicht möglich
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('charplot.pdf')
