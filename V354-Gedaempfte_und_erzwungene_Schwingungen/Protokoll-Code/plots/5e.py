import matplotlib.pyplot as plt
import numpy as np

Upp,Ipp,f = np.genfromtxt('5ewerte.txt', unpack = True)
R = Upp/Ipp



plt.plot(f, R,'rx', label='Scheinwiederstand')
plt.xlabel(r'$\nu \:/\: Hz$')
plt.ylabel(r'$ U/I * (1/\Omega)$')
plt.legend(loc='best')

# in matplotlibrc leider (noch) nicht möglich
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('5eplot.pdf')
