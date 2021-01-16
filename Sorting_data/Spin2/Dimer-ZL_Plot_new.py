# Dimerization & twist Order Parameter 
### Plot
import os
import math
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt 
from scipy.optimize import curve_fit

spin = 2.0
BC = 'PBC'
P = 10
Ls = [64]
#Jdis = ['Jdis000','Jdis050','Jdis100','Jdis150','Jdis200','Jdis250']
Jdis = ['Jdis000','Jdis200','Jdis250','Jdis260','Jdis270','Jdis280','Jdis290','Jdis300']
chis = [40]
datanum = 500
init_seed = 1

for i in range(len(Ls)):
    L = Ls[i]
    dfstr = pd.DataFrame(columns = ['Dimerization', 'O^z'])
    for m in range(len(chis)):
        
        for j in range(len(Jdis)):
            jdis = Jdis[j]
            J = float(Jdis[j][4] + '.' + Jdis[j][5] + Jdis[j][6])
            if(jdis == 'Jdis000'):
                N = 1
                M = 100
            elif(jdis != 'Jdis000'):
                N = datanum
                M = chis[m]

            myfile = '/home/liusf/test/Sorting_data/Spin2/metadata/ZL/'+ jdis + '/Dimer-ZL/'+ BC +'_L'+ str(L) +'_P' + str(P) + '_m' + str(M) + '_dim-zl_AV'+ str(N) +'.csv'
            df = pd.read_csv(myfile)
            plt.plot(df['Dimerization'], df['ZL'], "o-", markersize = 4, label = 'L=%d, R=%.2f, $\chi$= %d, AVG=%d' %(L, J, M, N))
            plt.errorbar(df['Dimerization'], df['ZL'], yerr=df['error'], linestyle='None', capsize=3, capthick=1, label=None) 

plt.xlabel(r'$Dimerization$', fontsize=14)
plt.ylabel(r'$Z(L)$', fontsize=14)
plt.xlim(0,0.6)
plt.ylim(-0.05, 0.05)
#plt.xscale('log')
#plt.yscale('log')
plt.title(r'Dimerization vs $Z(L)$, spin = %s' % (spin), fontsize=12)
plt.legend(loc = 'best',fontsize=8)
plt.grid(linestyle='-', linewidth=1)
plt.savefig( 'Spin2_' + BC + '_P'+ str(P) +'_ZL-Dimerization.pdf', format='pdf', dpi=4000)
plt.show()