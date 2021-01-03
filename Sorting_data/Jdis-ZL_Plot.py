# Dimerization & String Order Parameter 
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
Ls = [32,64,128]
Jdis = ['Jdis090','Jdis095','Jdis100','Jdis105','Jdis110','Jdis115','Jdis120']
Dimer = ["Dim000"]
init_seed = 1

for l in range(len(Ls)):
    L = Ls[l]
    if (L == 32 or L == 64):
        N = 1000
    if (L == 128):
        N = 100
    dfstr = pd.DataFrame(columns = ['Jdis', 'O^z'])
    for d in range(len(Dimer)):
        dimer = Dimer[d]
        D = float(Dimer[d][3] + '.' + Dimer[d][4])

        myfile = '/home/liusf/test/Sorting_data/metadata/ZL/'+ dimer + '/Jdis-ZL/'+ BC +'_L'+ str(L) +'_P' + str(P) + '_m30_jdis-zl_AV'+ str(N) +'.csv'
        df = pd.read_csv(myfile)
        plt.plot(df['Jdis'], df['ZL'], "o-", markersize = 8, label = 'L=%d, AVG(%d)' %(L, N))
        if (N != 1):
            plt.errorbar(df['Jdis'], df['ZL'], yerr=df['error'], linestyle='None', capsize=3, capthick=1, label=None)

plt.xlabel(r'$R$', fontsize=14)
plt.ylabel(r'$Z(L)$', fontsize=12)
#plt.xlim(0.1,1.5)
plt.ylim(-0.6, 0.1)
#plt.xscale('log')
#plt.yscale('log')
plt.title(r'R vs $Z(L)$, spin = %s, $\dimer$ = %s, $\chi$ = 30' % (spin, D), fontsize=12)
plt.legend(loc = 'best',fontsize=12)
plt.savefig( 'Spin1_' + BC + '_' + dimer + '_P'+ str(P) +'_m30_ZL-Jdis.pdf', format='pdf', dpi=4000)
plt.show()