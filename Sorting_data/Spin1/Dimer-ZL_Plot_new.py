# Dimerization & twist Order Parameter 
### Plot
import os
import math
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt 
from scipy.optimize import curve_fit

spin = 1.0
BC = 'PBC'
P = 10
Ls = [64]
Jdis = ['Jdis000','Jdis020','Jdis040','Jdis060','Jdis080','Jdis100','Jdis105','Jdis110','Jdis150','Jdis200',]
chis = [30]
datanum = 1000
init_seed = 1

for i in range(len(Ls)):
    L = Ls[i]
    dfstr = pd.DataFrame(columns = ['Dimerization', 'O^z'])
    for m in range(len(chis)):
        M = chis[m]
        for j in range(len(Jdis)):
            jdis = Jdis[j]
            J = float(Jdis[j][4] + '.' + Jdis[j][5] + Jdis[j][6])
            if(j == 0):
                N = 1
            elif(j != 0):
                N = datanum

            myfile = '/home/liusf/test/Sorting_data/Spin1/metadata/ZL/'+ jdis + '/Dimer-ZL/'+ BC +'_L'+ str(L) +'_P' + str(P) + '_m' + str(M) + '_dim-zl_AV'+ str(N) +'.csv'
            df = pd.read_csv(myfile)
            plt.plot(df['Dimerization'], df['ZL'], "o-", markersize = 8, label = 'L=%d, R=%.2f, $\chi$= %d, AVG=%d' %(L, J, M, N))
            plt.errorbar(df['Dimerization'], df['ZL'], yerr=df['error'], linestyle='None', capsize=3, capthick=1, label=None) 

plt.xlabel(r'$Dimerization$', fontsize=14)
plt.ylabel(r'$Z(L)$', fontsize=12)
#plt.xlim(0.1,1.5)
#plt.ylim(-1, 1)
#plt.xscale('log')
#plt.yscale('log')
plt.title(r'Dimerization vs $Z(L)$, spin = %s, $\delta$ = %s' % (spin, J), fontsize=12)
plt.legend(loc = 'best',fontsize=12)
plt.grid(color='b', linestyle='-', linewidth=1)
plt.savefig( 'Spin1_' + BC + '_P'+ str(P) +'_ZL-Dimerization.pdf', format='pdf', dpi=4000)
plt.show()