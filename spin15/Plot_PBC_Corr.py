## Bulk Correlation for OBC/PBC ##
## average raw data ##import os

import os
import math
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt 
from scipy.optimize import curve_fit

BC = 'PBC'
Ls = [32, 64]
Jdis = 'Jdis10'
N = 100

for i in range(len(Ls)):
    dfM = pd.DataFrame(columns = ['x2-x1', 'corr'])
    direc = '/home/liusf/test/spin15/'+ Jdis
    path = direc +'/'+ BC +'_L'+ str(Ls[i]) +'_P10_m30_corr1_N'+ str(N) + '_final' +'.csv'
    
    L = int(Ls[i]/2)
    myfile = '/home/liusf/test/spin15/'+ Jdis +'/'+ BC +'_L'+ str(Ls[i]) +'_P10_m30_corr1_N'+ str(N) +'.csv'
    df = pd.read_csv(myfile)
    
    if (os.path.exists(direc) == False):
        os.mkdir(direc)
    
    for i in range(L):
        r = i+1
        dfsr = df.loc[df['x2-x1'] == r]
        mean = {'x2-x1':r ,'corr': dfsr['corr'].mean()}
        dfM.loc[i] = mean
    
    plt.plot(dfM['x2-x1'] ,dfM['corr'],"o-", markersize = 8, label = 'L = %d' %(L*2))
    dfM.to_csv(path,index=0)

plt.xlabel('r = |i - j|', fontsize=14)
plt.ylabel(r'$C_b(r)$', fontsize=14)
#plt.xlim(3,32)
#plt.ylim(0.001, 1)
#plt.xscale('log')
#plt.yscale('log')
plt.title(r'Bulk correlation(average %d) , %s, $\chi$ = 30' % (int(N), Jdis), fontsize=12)
plt.legend(loc = 'best')
plt.savefig( BC +'_P10_' + Jdis + '_m30_N' + str(N) +'_BulkCorr.pdf', format='pdf', dpi=4000)
plt.show()