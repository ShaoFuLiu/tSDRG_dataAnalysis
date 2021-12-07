# Bulk Correlation 
### Plot Correlation and fitting

import os
import math
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt 
from scipy.optimize import curve_fit

def func(x, a, b): ## 定義 fitting 公式 (ax^b)
    return a*x**b

BC = 'PBC'
Ls = [32, 64]
Jdis = 'Jdis01'
J = Jdis[4] + '.' + Jdis[5]
Dimer = 'Dim01'
D = Dimer[3] + '.' + Dimer[4]
P = 10
N = 100  

dftail = pd.DataFrame(columns = ['x2-x1', 'corr'])
for i in range(len(Ls)):
    L = int(Ls[i]/2)
    direc = './metadata/Corr/'+ Dimer
    myfile = direc +'/'+ BC +'_L'+ str(Ls[i]) +'_P' + str(P) + '_m30_corr_AV'+ str(N) +'.csv'
    df = pd.read_csv(myfile)
    plt.plot(df['x2-x1'] ,df['corr'],".", markersize = 10, label = 'L=%d' %(Ls[i]))
    
    popt, pcov = curve_fit(func, df['x2-x1'], df['corr']) ## fitting data
    print(popt)
    a = popt[0]
    b = popt[1]
    yp = []
    for j in range(L):
        yp.append(func(df['x2-x1'][j], a ,b))
    
    plt.plot(df['x2-x1'], yp, "--", label = 'L = %s, $A/r^ %1.4f$' %(Ls[i], abs(b))) ## fitting data curve

    tail = {'x2-x1':df['x2-x1'][L-1] ,'corr': df['corr'][L-1]} ## 尾端值
    dftail.loc[i] = tail

popt1, pcov1 = curve_fit(func, dftail['x2-x1'], dftail['corr']) ## fitting 尾端值 
c = popt1[0]
d = popt1[1]
yp = []
for k in range(len(Ls)):
    yp.append(func(dftail['x2-x1'][k], c ,d))
plt.plot(dftail['x2-x1'], yp, "k--", label = '$A/r^%1.4f$' %(abs(d))) ## fitting 尾端值 curve

plt.xlabel('r = |i - j|', fontsize=14)
plt.ylabel(r'$C_b(r)$', fontsize=14)
#plt.xlim(3,32)
#plt.ylim(0.001, 1)
plt.xscale('log')
plt.yscale('log')
plt.title(r'Bulk correlation(average %d) , $\delta$ = %s, Dimer = %s, $\chi$ = 30' % (int(N), J, D), fontsize=12)
plt.legend(loc = 'best')
plt.savefig( BC +'_P'+ str(P) +'_' + Jdis + '_' + Dimer + '_m30_Corr_AV' + str(N) +'.pdf', format='pdf', dpi=4000)
plt.show()