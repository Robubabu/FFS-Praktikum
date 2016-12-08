import matplotlib.pyplot as plt
import numpy as np

phi,nu =np.genfromtxt('5dwerte.txt', unpack = True)
phi*=1e-6

plt.plot( nu,phi , 'rx', label='Frequenz und Phase')
plt.xlabel(r'$\nu \:/\: Hz$')
plt.xscale('log')
plt.ylabel(r'$ \phi\:/\:s $')
plt.legend(loc='best')
plt.show()
# in matplotlibrc leider (noch) nicht möglich
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
#plt.savefig('5dplot.pdf')
