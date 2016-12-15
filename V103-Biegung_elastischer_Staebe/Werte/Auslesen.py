import numpy as np

x,y0, y1 = np.genfromtxt('V103-Reihe1.txt', unpack = True)
np.savetxt('V103-Reihe1-tab.txt',np.column_stack([x,y0, y1, y1-y0]), delimiter=' & ',newline= r'\\'+'\n' )

x,y0, y1 = np.genfromtxt('V103-Reihe2.txt', unpack = True)
np.savetxt('V103-Reihe2-tab.txt',np.column_stack([x,y0, y1, y1-y0]), delimiter=' & ',newline= r'\\'+'\n' )

x,y0, y1 = np.genfromtxt('V103-Reihe3.txt', unpack = True)
np.savetxt('V103-Reihe3-tab.txt',np.column_stack([x,y0, y1, y1-y0]), delimiter=' & ',newline= r'\\'+'\n' )
