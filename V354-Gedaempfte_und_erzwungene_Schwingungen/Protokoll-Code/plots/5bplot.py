import matplotlib.pyplot as plt
import numpy as np
import uncertainties.unumpy as unp
from scipy.optimize import curve_fit
from uncertainties import correlated_values, correlation_matrix
from uncertainties import ufloat
from uncertainties.unumpy import (nominal_values as noms, std_devs as stds)

C = ufloat(2.098, 0.006)*1e-9
L = ufloat(10.11 , 0.03)*1e-3
Ra =(unp.sqrt((4*L)/C))
R = 3.3*1e3
print(((Ra-R)/Ra))
