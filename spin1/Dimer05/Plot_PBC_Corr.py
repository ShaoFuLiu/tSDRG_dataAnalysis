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
J = 1.0
Dim = 0.5
N = 100

for i in range(len(Ls)):
    L = int(Ls[i]/2)
    dfM = pd.DataFrame(columns = ['x2-x1', 'corr'])
    direc = '/home/liusf/test/spin1/Dimer05/'+ Jdis
    path = direc +'/'+ BC +'_L'+ str(Ls[i]) +'_P10_m30_corr1_N'+ str(N) + '_final' +'.csv'
    
    if (os.path.exists(direc) == False):
        os.mkdir(direc)
    
    myfile = '/home/liusf/test/spin1/Dimer05/'+ Jdis +'/'+ BC +'_L'+ str(Ls[i]) +'_P10_m30_corr1_N'+ str(N) +'.csv'
    df = pd.read_csv(myfile)

    for i in range(L):
        r = i+1
        dfsr = df.loc[df['x2-x1'] == r]
        mean = {'x2-x1':r ,'corr': dfsr['corr'].mean()}
        dfM.loc[i] = mean
    
    plt.plot(dfM['x2-x1'] ,dfM['corr'],".", markersize = 8, label = "L=%d" %(L*2))
    dfM.to_csv(path,index=0)

plt.xlabel('r = |i - j|', fontsize=14)
plt.ylabel(r'$C_b(r)$', fontsize=14)
#plt.xlim(3,32)
#plt.ylim(0.001, 1)
#plt.xscale('log')
#plt.yscale('log')
plt.title(r'Bulk correlation(average %d) , $\delta$ = %s, Dimer = %s, $\chi$ = 30' % (int(N), str(J), str(Dim)), fontsize=12)
plt.legend(loc = 'best')
plt.savefig(BC +'_D05_P10_' + Jdis + '_m30_N' + str(N) +'.pdf', format='pdf', dpi=4000)
plt.show()