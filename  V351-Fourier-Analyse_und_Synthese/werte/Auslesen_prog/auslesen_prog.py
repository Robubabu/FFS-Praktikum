import numpy as np

nn10,kn10 = np.genfromtxt('bnwerrteNadelk10.txt', unpack = True)
nn100,kn100 = np.genfromtxt('bnwerteNadelk100.txt', unpack = True)
nd,kd = np.genfromtxt('bnwerteDreieck.txt', unpack = True)
nr,kr = np.genfromtxt('bnwerteRechteck.txt', unpack = True)
np.savetxt('nadel10tab.txt',np.column_stack([nn10,kn10]), delimiter=' & ',newline= r'\\'+'\n' )
np.savetxt('nadel100tab.txt',np.column_stack([nn100,kn100]), delimiter=' & ',newline= r'\\'+'\n' )
np.savetxt('dreiecktab.txt',np.column_stack([nd,kd]), delimiter=' & ',newline= r'\\'+'\n' )
np.savetxt('rechtecktab.txt',np.column_stack([nr,kr]), delimiter=' & ',newline= r'\\'+'\n' )
