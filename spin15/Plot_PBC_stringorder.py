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
#Jdis = ['Jdis08', 'Jdis09', 'Jdis10', 'Jdis11', 'Jdis12']
Jdis = ['Jdis10']
N = 100

for j in range(len(Jdis)):
    delta = Jdis[j]
    #dfstr = pd.DataFrame(columns = ['ln(L)', 'ln(O^z)'])
    dfstr = pd.DataFrame(columns = ['L', 'O^z'])

    for i in range(len(Ls)):
        myfile = '/home/liusf/test/spin15/'+ delta +'/'+ BC +'_L'+ str(Ls[i]) +'_P10_m30_string_N'+ str(N) +'.csv'
        df = pd.read_csv(myfile)
        #mean = {'ln(L)':math.log(Ls[i]) ,'ln(O^z)': math.log(df['corr'].mean())}
        mean = {'L':Ls[i] ,'O^z': df['corr'].mean()}
        dfstr.loc[i] = mean

    plt.plot(dfstr['L'] ,dfstr['O^z'], "o-", markersize = 8, label = delta)
    #plt.plot(dfstr['ln(L)'] ,dfstr['ln(O^z)'])
#plt.xlabel(r'$lnL$', fontsize=14)
#plt.ylabel(r'$lnO^z(L/2)$', fontsize=14)
plt.xlabel(r'$L$', fontsize=14)
plt.ylabel(r'$O^z(L/2)$', fontsize=14)
#plt.xlim(3.3,5.7)
plt.ylim(-1, 1)
#plt.xscale('log')
#plt.yscale('log')
plt.title(r'String order parameter(average %d), $\chi$ = 30, $\delta$ = 1.0' % (int(N)), fontsize=12)
plt.legend(loc = 'best')
plt.savefig( BC +'_P10_m30_string_N' + str(N) +'.pdf', format='pdf', dpi=4000)
plt.show()