import numpy as np
import uncertainties as unp

w1t = 2*np.pi/unp.ufloat(1.53215, 0.00035)

w1s = 2*np.pi/unp.ufloat(9.828, 0.071)
w15s = 2*np.pi/unp.ufloat(10.2536, 0.0832)
T11 = unp.ufloat(1.446, 0.011)
T12 = unp.ufloat(1.284,0.012)
l1 = unp.ufloat(0.5833, 0.00027)
l1l = unp.ufloat(0.58233, 0.00027)
l1r = unp.ufloat(0.58433, 0.00027)
w1p = 2*np.pi/T11
w1m = 2*np.pi/T12

w2t = 2*np.pi/unp.ufloat(1.747, 0.023)

w2s = 2*np.pi/unp.ufloat(15.571, 0.195)
w25s = 2*np.pi/unp.ufloat(15.7474, 0.593)
T21 = unp.ufloat(1.746, 0.007)
T22 = unp.ufloat(1.559, 0.009)
l2 = unp.ufloat(0.758, 0.02)
w2p = 2*np.pi/T21
w2m = 2*np.pi/T22

T1l = 2*np.pi*(l1l/9.81)**(0.5)
T1r = 2*np.pi*(l1r/9.81)**(0.5)
T2 = 2*np.pi*(l2/9.81)**(0.5)

k1 = (T11**2 - T12**2)/(T11**2 + T12**2)
k2 = (T21**2 - T22**2)/(T21**2 + T22**2)

K1 = (4*np.pi**2*l1)/(2*T12**2)-9.81/2
K2 = (4*np.pi**2*l2)/(2*T22**2)-9.81/2

w1mt = (w1p**2*(1+k1)/(1-k1))**(1/2)
w2mt = (w2p**2*(1+k2)/(1-k2))**(1/2)

w1st = w1mt - w1t
w2st = w2mt - w2t
#t1m = 2 * np.pi*(l1/(9.81+2*K1))**(1/2)
#t2m = 2* np.pi * (l2/(9.81+2*K2))**(1/2)
print('T1l: ', T1l)
print('T1r: ', T1r)
print('T2: ', T2)
print('k1: ', k1)
print('k2: ', k2)
print('K1: ', K1)
print('K2: ', K2)
print('w1mt: ', w1mt)
print('w2mt: ', w2mt)
print('ws1e: ', w1p - w1m)
print('ws2e: ', w2p - w2m)
print('w1s: ', w1s)
print('w15s: ', w15s)
print('w2s: ', w2s)
print('w25s: ', w25s)
print('w1st: ', w1st)
print('w1t: ', w1t)
print('w2t: ', w2t)
print('w2st: ', w2st)
