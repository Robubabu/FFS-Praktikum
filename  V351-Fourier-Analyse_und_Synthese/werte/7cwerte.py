import numpy as np

n = np.arange(1,10)
#b= (1/(n*np.pi))(1-np.cos(n*np.pi))
a= (1/(n*np.pi))
c = (1-np.cos(n*np.pi))
bnrecht = a * c
np.savetxt('bnwerteRechteck.txt',np.column_stack([n , bnrecht]))

bndrei = (-1/(np.pi*n))
np.savetxt('bnwerteDreieck.txt', np.column_stack([n , bndrei]))

k=10
bnnadel = (1/(n*np.pi))*np.sin((n*2*np.pi)/k)
np.savetxt('bnwerrteNadelk10.txt', np.column_stack([n , bnnadel]))
k=100
np.savetxt('bnwerteNadelk100.txt', np.column_stack([n , bnnadel]))
