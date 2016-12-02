import matplotlib.pyplot as plt
import numpy as np
import uncertainties.unumpy as unp


#Rechteck
nr,br = np.genfromtxt('br.txt', unpack = True) #berechnete Wwerte
bre = np.genfromtxt('7b1Recheck.txt', unpack =True) # aus erster Messreihe
#Nadelimpuls
nn, bn = np.genfromtxt('bn10.txt', unpack = True) # nadelimpuls mit k = 10
nn1, bn1 = np.genfromtxt('bn100.txt', unpack = True) #nadelimpuls mit k=100
bne = np.genfromtxt('7bNadelimpuls.txt', unpack = True)
#Dreick und Sägezahn
nd , bd = np.genfromtxt('bd.txt' , unpack = True)
bse = np.genfromtxt('7bSaegezahn.txt', unpack = True)
br*=10
bn*=10
bd*=10
bn1*=50
mbd = -bd
#nun Fehler der exp Größen
#Rechteck
re= unp.uarray(bre,(bre*(3/100)))
#Nadelimpuls
ne = unp.uarray(bne,(bne*(3/100)))
#Sägezahn
se = unp.uarray(bse,(bse*(3/100)))

#Rechteckplot
plt.plot(nr, br,'bx', label='Errechnete Amplitude')
plt.errorbar(nr, unp.nominal_values(re), yerr=unp.std_devs(re), fmt='rx', label='Experimentele Amplitude')
plt.xlabel(r'$n$')
plt.ylabel(r'$ A \:/\: V$')
plt.legend(loc='best')
plt.savefig('build/Rechteckplot.pdf')
plt.clf()
#Nadelimpuls
plt.plot(nn,bn,'bx', label='Errechnete Amplitude mit k=10')
plt.plot(nn,bn1, 'gx' , label='Errechnete Amplitude mit k= 100')
plt.errorbar(nr, unp.nominal_values(ne), yerr=unp.std_devs(ne),fmt ='rx', label='Experimentele Amplitude')
plt.xlabel(r'$n$')
plt.ylabel(r'$A\:/\: V$')
plt.legend(loc='best')
plt.savefig('build/Nadelimpulsplot.pdf')
plt.clf()
#Dreick und Sägezahn
plt.plot(nd, bd,'bx', label='Errechnete Amplitude')
plt.errorbar(nr, unp.nominal_values(se), yerr=unp.std_devs(se),fmt='rx', label='Experimentele Amplitude')
plt.plot(nd, mbd ,'gx' , label='Errechnete Amplitude mit anderem Vorzeichen')
plt.xlabel(r'$n$')
plt.ylabel(r'$A \:/\: V$')
plt.legend(loc='best')
plt.savefig('build/Dreieckplot.pdf')
