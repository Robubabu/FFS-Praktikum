import matplotlib.pyplot as plt
import numpy as np
import uncertainties.unumpy as unp
from scipy.optimize import curve_fit
from uncertainties import correlated_values, correlation_matrix
from uncertainties import ufloat
from uncertainties.unumpy import (nominal_values as noms, std_devs as stds)

x = np.linspace(0,18,20)

def mittel(x):              #the real mean()-ing of life
    return ufloat(np.mean(x),np.std(x,ddof=1)/np.sqrt(len(x)))
def ULGL(g,b): # Umgekehrt Linsengleichung gibt direkt f (Brennweite) aus
    return (1/((1/b) + (1/g)))
def relf(l,m): #relativer Fehler in Prozent
    return (np.absolute(l - m)/np.absolute(l))*100

#Messwerte 100mm Linse
xG1,xL1,xS1 = np.genfromtxt('gbLinse100mm.txt', unpack = True)
#Messwerte 100mm Linse mit Bildgröße
xG2,xL2,xS2,B = np.genfromtxt('gbLinse100mmB.txt', unpack = True)
#Messwerte Wasserlinse
xG3,xL3,xS3 = np.genfromtxt('gbWasserlinse.txt', unpack = True)
#Gegenstandsgröße:
G = 3 #centimeter
#Brennweiter der 100mm Linse
f = 100

#Umrechnen von cm auf m
xG1*=10e-3
xG2*=10e-3
xG3*=10e-3
xL1*=10e-3
xL2*=10e-3
xL3*=10e-3
xS1*=10e-3
xS2*=10e-3
xS3*=10e-3
B*=10e-3
G*=10e-3
f*= 10e-4

#Berechnung der Gegenstands- und Bildweiten
g1 = xG1 - xL1
b1 = xL1 - xS1
g2 = xG2 - xL2
b2 = xL2 - xS2
g3 = xG3 - xL3
b3 = xL3 - xS3
#Berechnung der Brennweite
f1 = ULGL(g1,b1)
f2 = ULGL(g2,b2)
f3 = ULGL(g3,b3)
#Mittel der Brennweiten
mf1 = mittel(f1)
mf2 = mittel(f2)
mf3 = mittel(f3)
print('Mittlere Brennweite der 100mm Linse:', mf1)
print('Mittlere Brennweite der Wasserlinse:', mf3)
#Berechnung des Abbildungsmaßstabes mit b und g (und G und B)
V = B/G
V2 = b2 / g2
#Mittel des Abbildungsmaßstabes über g&b und über B&G
mV = mittel(V)
mV2 = mittel(V2)
print('Mittelwert des Abbildungsmaßstabes über G und B:', mV)
print('Mittelwert des Abbildungsmaßstabes über g und b:',mV2)
#Relativer Fehler des mittleren Abbildungsmaßstabes und mittlerer Brennweiten
print('Relativer Fehler des mittleren Abbildungsmaßstabes:', relf(mV,mV2))
print('Relativer Fehler der mittleren Brennweite f1:', relf(f,mf1))
#Tabelle
np.savetxt('Lgbtab.txt',np.column_stack([xG1,xL1,xS1,g1,b1,f1]), delimiter=' & ',newline= r'\\'+'\n' )
np.savetxt('Wgbtab.txt',np.column_stack([xG3,xL3,xS3,g3,b3,f3]), delimiter=' & ',newline= r'\\'+'\n' )
np.savetxt('BLgbtab.txt',np.column_stack([xG2,xL2,xS2,g2,b2,B]), delimiter=' & ',newline= r'\\'+'\n' )

#Plotarrays
#Jedes Array sollte wie folgt aufgebaut sein: [(g1,0) ; (0,b1)]
X = np.array([])
Y = np.array([])
for g,b in list(zip(g1,b1)): #Möchte zwei arrays haben 1: [b1[0] , 0 , b1[1],0,..] 2: [0 ,g1[0],0, g1[1],0  . . ]
    X = np.append(X,0)
    Y = np.append(Y,b)
    X = np.append(X,g)
    Y = np.append(Y,0)
X3 = np.array([])
Y3 = np.array([])
for g,b in list(zip(g3,b3)): #Nochmal für die Wasserlinse
    X3 = np.append(X,0)
    Y3 = np.append(Y,b)
    X3 = np.append(X,g)
    Y3 = np.append(Y,0)
# print(X)
# print(Y)


# Plots
# N = np.arange(0,19,1)
# #Plot für die100mm Linse
# for n in N:
#     plt.plot(X[n:n+3], Y[n:n+3] ,'g--')
# plt.xlabel(r'$g \quad Gegenstandsweiten / [m]$')
# plt.ylabel(r'$ b \quad Bildweiten / [m]$')
# # plt.show()
# plt.savefig('100mmLinsegbplot.pdf')
# plt.clf()
# #Plot für die Wasserlinse
# for n in N:
#     plt.plot(X3[n:n+3], Y3[n:n+3] ,'b--')
# plt.xlabel(r'$g \quad Gegenstandsweiten / [m]$')
# plt.ylabel(r'$ b \quad Bildweiten/ [m]$')
# # plt.show()
# plt.savefig('Wasserlinsegbplot.pdf')
