# String Order Parameter 
### Plot Delta vs Oz

import os
import math
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt 
from scipy.optimize import curve_fit

BC = 'PBC'
Ls = [32, 64]
Jdis = ['Jdis01','Jdis05','Jdis10']
Dimer = 'Dim01'
D = Dimer[3] + '.' + Dimer[4]
P = 10  # prob distribution type
N = 100 # total data number 

for i in range(len(Ls)):
    dfstr = pd.DataFrame(columns = ['delta', 'O^z'])
    
    for j in range(len(Jdis)):
        J = Jdis[j][4] + '.' + Jdis[j][5]
        delta = float(J)

        direc = './metadata/SOP/' + Jdis[j] + '/' + Dimer
        myfile = direc +'/'+ BC +'_L'+ str(Ls[i]) +'_P' + str(P) + '_m30_sop_AV'+ str(N) +'.csv'
        df = pd.read_csv(myfile)
        mean = {'delta':delta ,'O^z':df['corr'].mean()}
        dfstr.loc[j] = mean 
    
    plt.plot(dfstr['delta'] ,dfstr['O^z'],"o-", markersize = 8, label = 'L=%d' %(Ls[i]))

plt.xlabel(r'$\delta$', fontsize=14)
plt.ylabel(r'$O^z(r=L/2)$', fontsize=14)
#plt.xlim(0.1,1.5)
#plt.ylim(0, 0.4)
#plt.xscale('log')
#plt.yscale('log')
plt.title(r'$\delta$ vs $O^z(r=L/2)$(average %d), Dimer = %s, $\chi$ = 30' % (int(N), D), fontsize=12)
plt.legend(loc = 'best',fontsize=12)
plt.savefig( BC +'_P'+ str(P) + '_' + Dimer + '_m30_Delta-Oz_AV' + str(N) +'.pdf', format='pdf', dpi=4000)
plt.show()