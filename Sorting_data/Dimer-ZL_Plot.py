# Dimerization & String Order Parameter 
### Plot
import os
import math
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt 
from scipy.optimize import curve_fit

spin = 0.5
BC = 'PBC'
P = 10
Ls = [32]
Jdis = ['Jdis05']
Dimer = ['Dim01','Dim02','Dim03','Dim04','Dim05','Dim06','Dim07','Dim08','Dim09','Dim10']
N = 10  
init_seed = 1

arr = []
for j in range(N):
    n = str(init_seed+1)
    arr.append(n)

for i in range(len(Ls)):
    L = Ls[i]
    dfstr = pd.DataFrame(columns = ['Dimerization', 'O^z'])
    
    for j in range(len(Jdis)):
        jdis = Jdis[j]
        J = float(Jdis[j][4] + '.' + Jdis[j][5])

        myfile = '/home/liusf/test/Sorting_data/metadata/ZL/'+ jdis + '/Dimer-ZL/'+ BC +'_L'+ str(L) +'_P' + str(P) + '_m30_dim-zl_AV'+ str(N) +'.csv'
        df = pd.read_csv(myfile)
        plt.plot(df['Dimerization'], df['ZL'], "o-", markersize = 8, label = 'L=%d' %(L))

plt.xlabel(r'$Dimerization$', fontsize=14)
plt.ylabel(r'$Z(L)$', fontsize=12)
#plt.xlim(0.1,1.5)
#plt.ylim(-1, 1)
#plt.xscale('log')
#plt.yscale('log')
plt.title(r'Dimerization vs $Z(L)$(average %d), spin = %s, $\delta$ = %s, $\chi$ = 30' % (int(N), spin, J), fontsize=12)
plt.legend(loc = 'best',fontsize=12)
plt.savefig( BC + '_' + jdis + '_P'+ str(P) +'_m30_N' + str(N) +'_ZL-Dimerization.pdf', format='pdf', dpi=4000)
plt.show()