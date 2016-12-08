import matplotlib.pyplot as plt
import numpy as np
import uncertainties.unumpy as unp
from scipy.optimize import curve_fit
from uncertainties import correlated_values, correlation_matrix
from uncertainties import ufloat

Uss,Ueff,f = np.genfromtxt('5cwerte.txt', unpack = True )
U = 65e-3
Ueff/=1000
Ueff/=U
f*=1e-6
plt.subplot(1 ,2 ,1)
plt.plot(f, Ueff,'rx')
plt.xlabel(r'$ \nu /Hz$')
plt.ylabel(r'$ Uc/U$')
plt.grid()
plt.xscale('log')
#plt.legend(loc='best')

plt.subplot(1, 2 , 2)
plt.plot(f, Ueff,'bx')
plt.xlabel(r'$\nu /Hz$')
plt.xlim(10**-2 , 10**-1)
plt.grid()
plt.ylabel(r'$ Uc/U$')
#plt.legend(loc='best')
#qexp abgelesen ist (30173,3 ; 0,00955402) R = 100.7+/-2.1
L = ufloat(10.11 , 0.03)/1000
R = ufloat(100.7, 2.1)
C = ufloat( 2.098 , 0.006)*1e-9
q = (unp.sqrt(1/(C*L))/(R/L))
nu= (unp.sqrt(1/(C*L))/(R/(L*2*np.pi)))
qex= 2.34375
print('q theoretisch=' ,q )
print('q experimental = ' ,qex)
nuexp= 0.0343407
print('\nu experimentel=', nuexp)
print('\nu theoretisch =', nu)

print('Rap=',(unp.sqrt((4*L)/C)))
print('\nu res =', ((1/np.pi)*unp.sqrt((1/(L*C)-(R**2)/(2*L**2)))))
print('\nu plus =',(1/(2*np.pi)*(unp.sqrt((R**2/(4*L**2)+(1/(L*C))))+(R/(2*L)))))
print('\nu minus =',(1/(2*np.pi)*(unp.sqrt((R**2/(4*L**2)+(1/(L*C))))-(R/(2*L)))))



plt.show()

# # in matplotlibrc leider (noch) nicht möglich
# plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
#plt.savefig('5cplot.pdf')
