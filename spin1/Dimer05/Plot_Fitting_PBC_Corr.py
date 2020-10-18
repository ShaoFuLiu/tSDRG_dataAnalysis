## Bulk Correlation for OBC/PBC 
## average raw data

import os
import math
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt 
from scipy.optimize import curve_fit

BC = 'PBC'
Ls = [32, 64, 128]
Jdis = 'Jdis10'
Dim = 0.5
J = 1.0
N = 100

def func(x, a, b): ## 定義 fitting 公式 (ax^b)
    return a*x**b

dftail = pd.DataFrame(columns = ['x2-x1', 'corr'])

for i in range(len(Ls)):
    L = int(Ls[i]/2)
    direc = '/home/liusf/test/spin1/Dimer05/'+ Jdis
    path = direc +'/'+ BC +'_L'+ str(Ls[i]) +'_P10_m30_corr1_N'+ str(N) + '_final' +'.csv'
    df = pd.read_csv(path)
    
    tail = {'x2-x1':df['x2-x1'][L-1] ,'corr': df['corr'][L-1]} ## 取最後一個值,存入dftail
    dftail.loc[i] = tail
    #print(dftail)
    
    plt.plot(df['x2-x1'], df['corr'], ".", markersize = 10, label = 'L=%d' %(Ls[i])) ## oringinal data curve   
    popt, pcov = curve_fit(func, df['x2-x1'], df['corr']) ## fitting
    #print(popt)
    a = popt[0]
    b = popt[1]
    yp = []
    for i in range(L):
        yp.append(func(df['x2-x1'][i], a ,b))
    
    if(L == 16):
        plt.plot(df['x2-x1'], yp, "b--", label = 'L=32, $A/r^%1.4f$' %(abs(b))) ## fitting data curve
    elif (L == 32):
        plt.plot(df['x2-x1'], yp, "r--", label = 'L=64, $A/r^%1.4f$' %(abs(b))) ## fitting data curve
    elif (L == 64):
        plt.plot(df['x2-x1'], yp, "g--", label = 'L=128, $A/r^%1.4f$' %(abs(b))) ## fitting data curve

popt1, pcov1 = curve_fit(func, dftail['x2-x1'], dftail['corr']) ## fitting 最後一個值 curve
c = popt1[0]
d = popt1[1]
yp = []
for i in range(len(Ls)):
    yp.append(func(dftail['x2-x1'][i], c ,d))
plt.plot(dftail['x2-x1'], yp, "k--", label = '$A/r^%1.4f$' %(abs(d))) ## fitting data curve

plt.xlabel('r = |i - j|', fontsize=14)
plt.ylabel(r'$C_b(r)$', fontsize=14)
#plt.xlim(3,32)
#plt.ylim(0.001, 1)
#plt.xscale('log')
#plt.yscale('log')
plt.legend(loc = 'best', fontsize=12)
plt.title(r'Bulk correlation(average %d) , $\delta$ = %s, Dimer = %s, $\chi$ = 30' % (int(N), str(J), str(Dim)), fontsize=12)
plt.savefig('Fitting_'+ BC +'_D05_P10_' + Jdis + '_m30_N' + str(N) +'.pdf', format='pdf', dpi=4000)
plt.show()