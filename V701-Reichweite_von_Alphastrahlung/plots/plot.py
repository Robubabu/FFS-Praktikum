
import matplotlib.pyplot as plt
import numpy as np
import uncertainties.unumpy as unp
import scipy
from scipy.optimize import curve_fit
from uncertainties import correlated_values, correlation_matrix
from uncertainties import ufloat
from uncertainties.unumpy import (nominal_values as noms, std_devs as stds)



#plt.subplot(1, 2, 1)


Imps=np.genfromtxt('../Messwerte/Statistik.txt', unpack=True)
Imps=Imps/10
plt.hist(Imps, normed = 1, bins = 10, color='orange', alpha=0.5)
n, bins, patches = plt.hist(Imps,normed= 1, bins = 10)

#for i in I:
#    if(i%4==0):
#        x4[i//4]=Imps[i]
#    elif i%3 == 0:
#        x3[i//4] == Imps[i]
#    elif i%2 == 0:
#        x2[i//4] == Imps[i]
#    else:
#        x1[i]==Imps[i]
#
#Tabelle
#np.savetxt('tab.txt',np.column_stack([x1,x2,x3,x4]), delimiter=' & ',newline= r'\\'+'\n' )

m = np.mean(Imps)
print('m: ',m)
print('bins: ', bins)
print('n: ', n)

def g(k,s):
    return 1/(s*np.sqrt(2*np.pi))*np.exp(-0.5*(k-m)**2/s**2)

def p(k,l):
    return l**k/scipy.misc.factorial(k)*np.exp(-l)


r = range(len(n))
bims= np.array(r)    #halo i bims, 1 echter balken

for i in r:
    bims[i] = 0.5*(bins[i]+bins[i+1])

print('halo i bims, 1 echter balken: ',bims)

paramsG, covG = curve_fit(g, bims, n)
errorsG = np.sqrt(np.diag(covG))
print('halo i bims, 1 gauß: ', *paramsG, '+/-', *errorsG)

y = np.linspace(480,600)
plt.plot(y,g(y,*paramsG),'k--', label='Gauß seine Glocke')


plt.xlabel('Impacts/s')
plt.ylabel('Wahrscheinlichkeit')
plt.legend()
plt.savefig('Statistik.pdf')
plt.clf()


Imps = (Imps-490)
plt.hist(Imps, normed = 1, bins = 20, color='orange')
n, bins, patches = plt.hist(Imps,normed = 1, bins = 20)
r = range(len(n))
bims= np.array(r)
for i in r:
    bims[i] = 0.5*(bins[i]+bins[i+1])


print('poissonBims: ', bims, n)
paramsP,covP = curve_fit(p,bims, n)
errorP = np.sqrt(np.diag(covP))
print('halo i bims, i fisch: ', paramsP, '+/-', errorP)
y = np.linspace(0,90)
plt.plot(y,p(y,paramsP), 'k-', label = 'Poisson Verteilung')

plt.xlabel('(Impacts-490)/s')
plt.ylabel('Wahrscheinlichkeit')
plt.legend()
plt.savefig('Poisson.pdf')
plt.clf()


########################################################################
#####################################################################
#########################################################################

def f(x,a,b):
    return a*x+b

p1,Channel1, Imps1 = np.genfromtxt('../Messwerte/Energie1.txt', unpack = True)
p2,Channel2, Imps2 = np.genfromtxt('../Messwerte/Energie2.txt', unpack = True)

Imps1 = Imps1/120
Imps2 = Imps2/120

E1 = 4*Channel1/Channel1[0] #in MeV
p1 =p1/1047 #effektiver Weg
##############################################################################
#############################################################################
#ENERGIEVERTEILUNG
##############################################################################
###########################################################################


E2 = 4*Channel2/Channel2[0] #in MeV
p2 = p2/1047 #effektiver Weg

p1Area = np.concatenate((p1[0:13], p1[14:19]))
E1Area = np.concatenate((E1[0:13], E1[14:19]))

parE1, covE1 = curve_fit(f,p1Area,E1Area)
parE2, covE2 = curve_fit(f,p2[0:12],E2[0:12])
Error1 = np.sqrt(np.diag(covE1))
Error2 = np.sqrt(np.diag(covE2))
print('Energie Messung 1: ', parE1, ' +/- ', Error1)
print('Energie Messung 2: ', parE2, ' +/- ', Error2)

plt.plot(p1Area, f(p1Area,*parE1), 'k-', label = 'Fit 1')
plt.plot(p2[0:12], f(p2[0:12],*parE2), 'k--', label = 'Fit 2')

plt.plot(p1, E1, 'kx', label = 'Erste Messung')
plt.plot(p2, E2, 'k.', label = 'Zweite Messung')
plt.plot(p1[13], E1[13], 'ro', label = 'Verworfener Wert')
plt.xlim(-0.02,1)
plt.ylim(2.0, 4.1)
plt.xlabel(r'$p/p_0$')
plt.ylabel('E/MeV')
plt.grid()
plt.legend()
plt.savefig('Energie.pdf')
plt.clf()

##############################################################################
#############################################################################
#IMPACTS
##############################################################################
###########################################################################


plt.plot(p1, Imps1, 'kx', label = 'Erste Messung')
plt.plot(p1[11],Imps1[11],'ro', label = 'verworfener Wert')
plt.plot(p1[23],Imps1[23],'ro')
plt.plot(p2, Imps2, 'k.', label = 'Zweite Messung')
plt.plot(p1[4],Imps2[4],'ro')


########################################
#Festlegung der Fit-berreiche
##########################################
pArea1 = p1[0:10]
pArea2 = np.concatenate((p2[0:4],p2[5:9]))

ImpArea1 = Imps1[0:10]
ImpArea2 = np.concatenate((Imps2[0:4],Imps2[5:9]))

mean1=np.mean(ImpArea1)
mean2=np.mean(ImpArea2)

error1 = 1/np.sqrt(len(ImpArea1))*np.std(ImpArea1)
error2 = 1/np.sqrt(len(ImpArea2))*np.std(ImpArea2)

print('Messung 1: ', mean1, ' +/- ', error1)
print('Messung 2: ', mean2, ' +/- ', error2)

m1 = ufloat(mean1, error1)
m2 = ufloat(mean2, error2)

plt.plot([pArea1[9],pArea1[9]],[500,600], 'k-.', label = 'Grenze des Plateaus')
plt.plot([pArea2[7],pArea2[7]],[300,400], 'k-.')

#pArea1 = np.concatenate((p1[10:11],p1[12:18]))
pArea2 = p2[10:19]

#ImpArea1 =  np.concatenate((Imps1[10:11],Imps1[12:18]))
ImpArea2 = Imps2[10:19]

#parImps1,covImps1 = curve_fit(f,pArea1,ImpArea1)
parImps2,covImps2 = curve_fit(f,pArea2,ImpArea2)

#Error1 = np.sqrt(np.diag(covImps1))
Error2 = np.sqrt(np.diag(covImps2))
#print('Zweite Gerade Messung 1: ', parImps1, ' +/- ', Error1)
print('Zweite Gerade Messung 2: ', parImps2, ' +/- ', Error2)

#plt.plot(pArea1, f(pArea1,*parImps1), 'k-')
plt.plot(pArea2, f(pArea2,*parImps2), 'k--')


pArea1 = p1[18:23]
#pArea2 = p2[10:19]

ImpArea1 = Imps1[18:23]
#ImpArea2 = Imps2[10:19]

parImps1,covImps1 = curve_fit(f,pArea1,ImpArea1)
#parImps2,covImps2 = curve_fit(f,pArea2,ImpArea2)

Error1 = np.sqrt(np.diag(covImps1))
#Error2 = np.sqrt(np.diag(covImps2))
print('Dritte Gerade Messung 1: ', parImps1, ' +/- ', Error1)
#print('Drittee Gerade Messung 2: ', parImps2, ' +/- ', Error2)

plt.plot(pArea1, f(pArea1,*parImps1), 'k-')
#plt.plot(pArea2, f(pArea2,*parImps2), 'k--')

errorpar1 = unp.uarray(parImps1,Error1)
errorpar2 = unp.uarray(parImps2,Error2)

R_1 = 0.023/errorpar1[0]*(m1/2-errorpar1[1])
R_2 = 0.029/errorpar2[0]*(m2/2-errorpar2[1])
print('ParImp1', parImps1)
print('R_1', R_1)
print('R_2', R_2)

plt.xlim(-0.02,1)
plt.ylim(-10, 610)
plt.xlabel(r'$p/p_0$')
plt.ylabel('Impacts/s')
plt.grid()
plt.legend(loc = 'lower left')
plt.savefig('Rate.pdf')
plt.clf()
