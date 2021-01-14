#  Correlation 
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
def gamma8(l,K): #gamma value for n = 8
    return math.acosh(math.cosh(2*K)*coth(2*K)-math.cos(l*math.pi/8))

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

gamma8_0 = []
gamma8_1 = []
gamma8_2 = []
gamma8_3 = []
gamma8_4 = []
gamma8_5 = []
gamma8_6 = []
gamma8_7 = []
gamma8_8 = []
gamma8_9 = []
gamma8_10 = []
gamma8_11 = []
gamma8_12 = []
gamma8_13 = []
gamma8_14 = []
gamma8_15 = []
Lambda0_n8 = []
Lambda1_n8 = []
corr8 = []

# 100 linearly spaced numbers
#K = np.linspace(0.01,1,100)
diff = 0.00001
Tc = 0.438
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

for i in range(len(K)):
    gamma8_0.append(2*K[i]+math.log(math.tanh(K[i])))
    gamma8_1.append(gamma8(1,K[i]))
    gamma8_2.append(gamma8(2,K[i]))
    gamma8_3.append(gamma8(3,K[i]))
    gamma8_4.append(gamma8(4,K[i]))
    gamma8_5.append(gamma8(5,K[i]))
    gamma8_6.append(gamma8(6,K[i]))
    gamma8_7.append(gamma8(7,K[i]))
    gamma8_8.append(gamma8(8,K[i]))
    gamma8_9.append(gamma8(9,K[i]))
    gamma8_10.append(gamma8(10,K[i]))
    gamma8_11.append(gamma8(11,K[i]))
    gamma8_12.append(gamma8(12,K[i]))
    gamma8_13.append(gamma8(13,K[i]))
    gamma8_14.append(gamma8(14,K[i]))
    gamma8_15.append(gamma8(15,K[i]))
    c = (2*math.sinh(2*K[i]))
    Lambda0_n8.append(math.pow(c,4)*math.exp(0.5*(gamma8_1[i]+gamma8_3[i]+gamma8_5[i]+gamma8_7[i]+gamma8_9[i]+gamma8_11[i]+gamma8_13[i]+gamma8_15[i])))
    Lambda1_n8.append(math.pow(c,4)*math.exp(0.5*(gamma8_0[i]+gamma8_2[i]+gamma8_4[i]+gamma8_6[i]+gamma8_8[i]+gamma8_10[i]+gamma8_12[i]+gamma8_14[i])))
    corr8.append(1/(math.log(Lambda0_n8[i]/Lambda1_n8[i])*8))
print('slope of n = 8 at Kc is : ')
print((corr8[1]-corr8[0])/(K[1]-K[0]))  

S8 = (corr8[1]-corr8[0])/(K[1]-K[0])
S4 = (corr4[1]-corr4[0])/(K[1]-K[0])
vinv = math.log(S8/S4)/math.log(2)
print('v = ' + str(1/vinv) + ' ;at diff = 0.00001')
"""
# plot the function 
plt.plot(K, corr2, "b--", label = 'n = 2')
plt.plot(K, corr4, "r--", label = 'n = 4')
plt.plot(K, corr8, "g--", label = 'n = 8')
plt.xlabel('K', fontsize=14)
plt.ylabel(r'$\zeta(K)/n$', fontsize=14)
plt.xlim(0.4,0.48)
plt.ylim(0.5, 2)
#plt.xscale('log')
#plt.yscale('log')
plt.title(r'n = 2,4 and 8, $\zeta(K)/n$ vs K', fontsize=12)
plt.legend(loc = 'best')
plt.savefig('SMHW5-4.pdf', format='pdf', dpi=4000)
plt.show()"""