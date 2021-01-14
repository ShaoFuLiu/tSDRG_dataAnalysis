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

n = 4 
gamma_0 = []
gamma_1 = []
gamma_2 = []
gamma_3 = []
gamma_4 = []
gamma_5 = []
gamma_6 = []
gamma_7 = []
Lambda0_n2 = []
Lambda1_n2 = []
Lambda0_n4 = []
Lambda1_n4 = []
corr = []

# 100 linearly spaced numbers
K = np.linspace(0.01,1,100)



# the function  
if(n == 4):
    for i in range(len(K)):
        print(i)
        gamma_0.append(2*K[i]+math.log(math.tanh(K[i])))
        gamma_1.append(gamma4(1,K[i]))
        gamma_2.append(gamma4(2,K[i]))
        gamma_3.append(gamma4(3,K[i]))
        gamma_4.append(gamma4(4,K[i]))
        gamma_5.append(gamma4(5,K[i]))
        gamma_6.append(gamma4(6,K[i]))
        gamma_7.append(gamma4(7,K[i]))
        c = (2*math.sinh(2*K[i]))
        Lambda0_n4.append(math.pow(c,n/2)*math.exp(0.5*(gamma_1[i]+gamma_3[i]+gamma_5[i]+gamma_7[i])))
        Lambda1_n4.append(math.pow(c,n/2)*math.exp(0.5*(gamma_0[i]+gamma_2[i]+gamma_4[i]+gamma_6[i])))
if(n == 2):
    for i in range(len(K)):
        gamma_0.append(2*K[i]+math.log(math.tanh(K[i])))
        gamma_1.append(gamma2(1,K[i]))
        gamma_2.append(gamma2(2,K[i]))
        gamma_3.append(gamma2(3,K[i]))
        c = (2*math.sinh(2*K[i]))
        Lambda0_n2.append(math.pow(c,n/2)*math.exp(0.5*(gamma_1[i]+gamma_3[i])))
        Lambda1_n2.append(math.pow(c,n/2)*math.exp(0.5*(gamma_0[i]+gamma_2[i])))

# plot the function 
if(n == 2): 
    plt.plot(K, Lambda0_n2, "b-", label = '$\lambda0$')
    plt.plot(K, Lambda1_n2, "r--", label = '$\lambda1$')
if(n == 4):
    plt.plot(K, Lambda0_n4, "b-", label = '$\lambda0$')
    plt.plot(K, Lambda1_n4, "r--", label = '$\lambda1$')
plt.xlabel('K', fontsize=14)
plt.ylabel(r'$\lambda(K)$', fontsize=14)
plt.xlim(0,1)
#plt.ylim(0.001, 1)
#plt.xscale('log')
#plt.yscale('log')
plt.title(r'n = %d, $\lambda(K)$ vs K' %(n), fontsize=12)
plt.legend(loc = 'best')
plt.savefig('SMHW5.pdf', format='pdf', dpi=4000)
plt.show()