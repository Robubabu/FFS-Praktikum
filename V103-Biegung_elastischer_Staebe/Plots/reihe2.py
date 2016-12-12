import matplotlib.pyplot as plt
import numpy as np
import uncertainties.unumpy as unp
from scipy.optimize import curve_fit

x,y0,y1 = np.genfromtxt('../Werte/V103-Reihe2.txt', unpack = True)

plt.plot(x,y0, 'ko', label = 'Unbelastet')
plt.plot(x,y1, 'ro', label = 'Belastet')
plt.plot(x,y1-y0, 'go', label = 'Differenz')

plt.grid()

plt.xlabel(r'$X \:/\: cm$')
plt.ylabel(r'$y \:/\: mm$')
plt.legend(loc='best')

plt.savefig('Reihe2.pdf')
