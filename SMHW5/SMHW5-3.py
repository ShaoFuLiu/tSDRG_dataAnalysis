# Correlation 
### Plot Correlation

import os
import math
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt 
from scipy.optimize import curve_fit

def coth(x): #python didnt support coth
    return math.cosh(x) / math.sinh(x)
def gamma2(l,K): #gamma value for n = 2
    return math.acosh(math.cosh(2*K)*coth(2*K)-math.cos(l*math.pi/2))
def gamma4(l,K): #gamma value for n = 4
    return math.acosh(math.cosh(2*K)*coth(2*K)-math.cos(l*math.pi/4))

gamma_0 = []
gamma_1 = []
gamma_2 = []
gamma_3 = []
Lambda0_n2 = []
Lambda1_n2 = []
corr2 = []

gamma4_0 = []
gamma4_1 = []
gamma4_2 = []
gamma4_3 = []
gamma4_4 = []
gamma4_5 = []
gamma4_6 = []
gamma4_7 = []
Lambda0_n4 = []
Lambda1_n4 = []
corr4 = []

# 100 linearly spaced numbers
diff = 0.001
Tc = 0.4266
K = [Tc, Tc+diff]

# the function  
for i in range(len(K)):
    gamma_0.append(2*K[i]+math.log(math.tanh(K[i])))
    gamma_1.append(gamma2(1,K[i]))
    gamma_2.append(gamma2(2,K[i]))
    gamma_3.append(gamma2(3,K[i]))
    c = (2*math.sinh(2*K[i]))
    Lambda0_n2.append(math.pow(c,1)*math.exp(0.5*(gamma_1[i]+gamma_3[i])))
    Lambda1_n2.append(math.pow(c,1)*math.exp(0.5*(gamma_0[i]+gamma_2[i])))
    corr2.append(1/(math.log(Lambda0_n2[i]/Lambda1_n2[i])*2))
print('slope of n = 2 at Kc is : ')
print((corr2[1]-corr2[0])/(K[1]-K[0])) 

for i in range(len(K)):
    gamma4_0.append(2*K[i]+math.log(math.tanh(K[i])))
    gamma4_1.append(gamma4(1,K[i]))
    gamma4_2.append(gamma4(2,K[i]))
    gamma4_3.append(gamma4(3,K[i]))
    gamma4_4.append(gamma4(4,K[i]))
    gamma4_5.append(gamma4(5,K[i]))
    gamma4_6.append(gamma4(6,K[i]))
    gamma4_7.append(gamma4(7,K[i]))
    c = (2*math.sinh(2*K[i]))
    Lambda0_n4.append(math.pow(c,2)*math.exp(0.5*(gamma4_1[i]+gamma4_3[i]+gamma4_5[i]+gamma4_7[i])))
    Lambda1_n4.append(math.pow(c,2)*math.exp(0.5*(gamma4_0[i]+gamma4_2[i]+gamma4_4[i]+gamma4_6[i])))
    corr4.append(1/(math.log(Lambda0_n4[i]/Lambda1_n4[i])*4)) 
print('slope of n = 4 at Kc is : ')
print((corr4[1]-corr4[0])/(K[1]-K[0])) 

S2 = (corr2[1]-corr2[0])/(K[1]-K[0])
S4 = (corr4[1]-corr4[0])/(K[1]-K[0])
vinv = math.log(S4/S2)/math.log(2)
print('v = ' + str(1/vinv) + ' ;at diff = 0.001')
"""
# plot the function 
plt.plot(K, corr2, "b--", label = 'n = 2')
plt.plot(K, corr4, "r--", label = 'n = 4')
plt.xlabel('K', fontsize=14)
plt.ylabel(r'$\zeta(K)/n$', fontsize=14)
plt.xlim(0.3,0.6)
plt.ylim(0.001, 2)
#plt.xscale('log')
#plt.yscale('log')
plt.title(r'n = 2 and 4, $\zeta(K)/n$ vs K', fontsize=12)
plt.legend(loc = 'best')
plt.savefig('SMHW5-3.pdf', format='pdf', dpi=4000)
plt.show()"""