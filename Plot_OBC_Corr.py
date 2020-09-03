## OBC plot ##
## fitting plot ##import os

import os
import math
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt 
from scipy.optimize import curve_fit

BC = 'OBC'
Ls = [32, 48, 64, 96, 128, 256]
Jdis = 'Jdis10'
N = 200  #arr = ['1','2','3','4','5'...]
init_seed = 1
dftail = pd.DataFrame(columns = ['x2-x1', 'corr'])

def func(x, a, b): ## 定義 fitting 公式 (ax^b)
    return a*x**b

for i in range(len(Ls)):
    #dfM = pd.DataFrame(columns = ['x2-x1', 'corr'])
    myfile = '/home/liusf/test/'+ Jdis +'/'+ BC +'_L'+ str(Ls[i]) +'_P10_m30_corr1_N'+ str(N) +'.csv'
    df = pd.read_csv(myfile)
    plt.plot(df['x2-x1'] ,df['corr'],"o-", markersize = 10, label = 'L = %d' %(Ls[i])) ## 原始data點
    tail = {'x2-x1':df['x2-x1'][0] ,'corr': df['corr'][0]} ## 取最後一個值
    dftail.loc[i] = tail

popt1, pcov1 = curve_fit(func, dftail['x2-x1'], dftail['corr']) ## fitting 最後一個值 curve
c = popt1[0]
d = popt1[1]
yp = []
for i in range(len(Ls)):
    yp.append(func(dftail['x2-x1'][i], c ,d))
plt.plot(dftail['x2-x1'], yp, "k--", label = '$A/r^%1.4f$' %(abs(d))) ## fitting data curve

plt.xlabel('r = L', fontsize=14)
plt.ylabel(r'$C_1(L)$', fontsize=14)
plt.xlim(30,260)
plt.ylim(0.01, 1)
plt.xscale('log')
plt.yscale('log')
plt.title(r'OBC correlation(average %d) , %s, $\chi$ = 30' % (int(N), Jdis), fontsize=12)
plt.legend(loc = 'best')
plt.savefig( BC +'_Corr_P10_' + Jdis + '_m30_N' + str(N) +'.pdf', format='pdf', dpi=4000)
plt.show()