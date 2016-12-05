# import matplotlib.pyplot as plt
# import numpy as np
# import uncertainties.unumpy as unp
# from scipy.optimize import curve_fit
# from uncertainties import correlated_values, correlation_matrix
# #Rechteck
# nr,br = np.genfromtxt('br.txt', unpack = True) #berechnete Wwerte
# bre = np.genfromtxt('7b1Recheck.txt', unpack =True) # aus erster Messreihe
# #Nadelimpuls
# nn, bn = np.genfromtxt('bn10.txt', unpack = True) # nadelimpuls mit k = 10
# nn1, bn1 = np.genfromtxt('bn100.txt', unpack = True) #nadelimpuls mit k=100
# bne = np.genfromtxt('7bNadelimpuls.txt', unpack = True) #aus messreihe
# #Dreick und Sägezahn
# nd , bd = np.genfromtxt('bd.txt' , unpack = True)
# bse = np.genfromtxt('7bSaegezahn.txt', unpack = True)#aus messreihe
# br*=10
# bn*=10
# bd*=10
# bn1*=50
# mbd = -bd
#
# #Fit
# def f(x , a ,b):
#     return a*(1/(x**b))
#
#
# rparams, rcov = curve_fit(f ,nr , bre )
# dparams, dcov = curve_fit(f, nd , bse)
# nparams, ncov = curve_fit(f ,nn , bne )
# rparams = correlated_values(rparams, rcov)
# dparams = correlated_values(dparams, dcov)
# nparams = correlated_values(nparams, ncov)
# #print(rparams[0],rparams[1],dparams[0],dparams[1],nparams[0],nparams[1])
# #nun Fehler der exp Größen
# #Rechteck
# re= unp.uarray(bre,(bre*(3/100)))
# #Nadelimpuls
# ne = unp.uarray(bne,(bne*(3/100)))
# #Sägezahn
# se = unp.uarray(bse,(bse*(3/100)))
#
# x = np.linspace(1,9)
#
# #Rechteckplot
# plt.plot(nr, br,'bx', label='Errechnete Amplitude')
# plt.errorbar(nr, unp.nominal_values(re), yerr=unp.std_devs(re), fmt='rx', label='Experimentele Amplitude')
# plt.plot(x, unp.nominal_values(f(x , rparams[0] , rparams[1])), 'g--', label='Fit')
# plt.xlabel(r'$n$')
# plt.ylabel(r'$ A \:/\: V$')
# plt.yscale('log')
# plt.xlim(0,10)
# plt.legend(loc='best')
# plt.savefig('build/Rechteckplot.pdf')
# plt.clf()
# #Nadelimpuls
# plt.plot(nn,bn,'bx', label='Errechnete Amplitude mit k=10')
# plt.plot(nn,bn1, 'gx' , label='Errechnete Amplitude mit k= 100')
# plt.errorbar(nr, unp.nominal_values(ne), yerr=unp.std_devs(ne),fmt ='rx', label='Experimentele Amplitude')
# plt.plot(x, unp.nominal_values(f(x , nparams[0] , nparams[1])), 'm--', label='Fit')
# plt.xlabel(r'$n$')
# plt.ylabel(r'$A\:/\: V$')
# plt.xlim(0,10)
# plt.legend(loc='best')
# plt.savefig('build/Nadelimpulsplot.pdf')
# plt.clf()
# #Dreick und Sägezahn
# #plt.plot(nd, bd,'bx', label='Errechnete Amplitude')
# plt.errorbar(nr, unp.nominal_values(se), yerr=unp.std_devs(se),fmt='rx', label='Experimentele Amplitude')
# plt.plot(nd, mbd ,'gx' , label='Errechnete Amplitude mit anderem Vorzeichen')
# plt.plot(x, unp.nominal_values(f(x , dparams[0] , dparams[1])), 'm--', label='Fit')
# plt.xlabel(r'$n$')
# plt.ylabel(r'$A \:/\: V$')
# # plt.ylim(-5 , 6)
# # plt.xlim(0,11)
# plt.yscale('log')
# plt.legend(loc='best')
# plt.savefig('build/Dreieckplot.pdf')
