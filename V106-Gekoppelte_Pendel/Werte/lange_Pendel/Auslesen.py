import numpy as np
import uncertainties as unp

t1, t2 = np.genfromtxt('gekoppelt.txt', unpack = True)
np.savetxt('gekoppelt-tab.txt',np.column_stack([t1, t2]), delimiter=' & ',newline= r'\\'+'\n' )
t3, t4 = np.genfromtxt('Schwebung.txt', unpack = True)
np.savetxt('Schwebung-tab.txt',np.column_stack([t1, t2]), delimiter=' & ',newline= r'\\'+'\n' )


tl = np.genfromtxt('links.txt')
tr = np.genfromtxt('rechts.txt')

l, r = np.genfromtxt('laenge.txt', unpack = True)

print('l: ', np.mean(l), ' +/- ', np.std(l), 'r: ', np.mean(r), ' +/- ', np.std(r))
l = unp.ufloat(np.mean(l), np.std(l))

mean = np.mean(tl)
std = np.std(tl)
print('Tl: ', mean, ' +/- ', std)
mean = np.mean(tr)
std = np.std(tr)
print('Tr: ', mean, ' +/- ', std)
mean = np.mean(t1)
std = np.std(t1)

print('T+: ', mean, ' +/- ', std)
t1 = unp.ufloat(mean/5, std/5)

mean = np.mean(t2)
std = np.std(t2)
t2 = unp.ufloat(mean/5, std/5)
print('T-: ', mean, ' +/- ', std)
mean = np.mean(t3)
std = np.std(t3)
t3 = unp.ufloat(mean, std)
print('Ts: ', mean, ' +/- ', std)
mean = np.mean(t4)
std = np.std(t4)
t4 = unp.ufloat(mean/5, std/5)
print('Ts5: ', mean, ' +/- ', std)
K = l/2*(2*np.pi/t2)**2 - 9.81/2
print('K=', K)

k = (t1**2-t2**2)/(t1**2+t2**2)
print('k= ', k)
