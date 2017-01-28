import numpy as np

x,y,z = np.genfromtxt('wT1T2.txt', unpack = True)
np.savetxt('wT1T2tab.txt',np.column_stack([x,y,z]), delimiter=' & ',newline= r'\\'+'\n' )

a,b,c = np.genfromtxt('wT5T6.txt', unpack = True)
np.savetxt('wT5T6tab.txt',np.column_stack([a,b,c]), delimiter=' & ',newline= r'\\'+'\n' )

d,e,f = np.genfromtxt('wT7T8.txt', unpack = True)
np.savetxt('wT7T8tab.txt',np.column_stack([d,e,f]), delimiter=' & ',newline= r'\\'+'\n' )
