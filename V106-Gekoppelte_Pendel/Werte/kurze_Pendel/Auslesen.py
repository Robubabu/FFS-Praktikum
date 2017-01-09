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

mean = np.mean(tl)
std = np.std(tl)
print('Tl: ', mean, ' +/- ', std)

mean = np.mean(tr)
std = np.std(tr)
print('Tr: ', mean, ' +/- ', std)


mean = np.mean(t1)
std = np.std(t1)
print('T+: ', mean, ' +/- ', std)

mean = np.mean(t2)
std = np.std(t2)
print('T-: ', mean, ' +/- ', std)

mean = np.mean(t3)
std = np.std(t3)
print('Ts: ', mean, ' +/- ', std)

mean = np.mean(t4)
std = np.std(t4)
print('Ts5: ', mean, ' +/- ', std)
