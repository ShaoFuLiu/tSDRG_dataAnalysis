# Dimerization & String Order Parameter
### Plot
import os
import math
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

spin = int(1)
BC = 'PBC'
P = 10
M = 30
Ls = [16,32,48,64,128]
Jdis = ['Jdis090','Jdis095','Jdis100','Jdis105','Jdis110','Jdis115','Jdis120']
Dimer = ["Dim000"]
Ns = [7000,7000,6000,4000,1000]
init_seed = 1

for l in range(len(Ls)):
    L = Ls[l]
    N = Ns[l]
    dfstr = pd.DataFrame(columns = ['Jdis', 'O^z'])

    for d in range(len(Dimer)):
        dimer = Dimer[d]
        D = float(Dimer[d][3] + '.' + Dimer[d][4])

        myfile = '/home/liusf/tSDRG_DataAnalysis/Sorting_data/Spin'+ str(spin) +'/metadata/ZL/'+ dimer + '/Jdis-ZL/'+ BC +'_L'+ str(L) +'_P' + str(P) + '_m'+ str(M) +'_jdis-zl_AV'+ str(N) +'.csv'
        df = pd.read_csv(myfile)
        plt.plot(df['Jdis'], df['ZL'], "o-", markersize = 8, label = 'L=%d, AVG(%d)' %(L, N))
        if (N != 1):
            plt.errorbar(df['Jdis'], df['ZL'], yerr=df['error'], linestyle='None', capsize=3, capthick=1, label=None)

plt.xlabel(r'$R$', fontsize=14)
plt.ylabel(r'$Z(L)$', fontsize=12)
plt.xlim(0.95,1.15)
plt.ylim(-0.4, -0.2)
#plt.xscale('log')
#plt.yscale('log')
plt.title(r'spin = %s, $\dimer$ = %s, $\chi$ = %d' % (spin, D, M), fontsize=12)
plt.legend(loc = 'best',fontsize=12)
plt.savefig( 'Spin'+ str(spin) +'_' + BC + '_P'+ str(P) +'_m'+ str(M) +'_ZL-Jdis.pdf', format='pdf', dpi=4000)
plt.show()