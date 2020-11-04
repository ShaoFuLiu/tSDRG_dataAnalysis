import os
import math
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt 
from scipy.optimize import curve_fit


spin = 0.5
BC = 'PBC'
Ls = [32]
Jdis = 'Jdis05'
J = float(Jdis[4] + '.' + Jdis[5])
Dimer = ['Dim01','Dim02','Dim03','Dim04','Dim05','Dim06','Dim07','Dim08','Dim09','Dim10']
N = 10  
init_seed = 1

arr = []
for j in range(N):
    n = str(1+j)
    arr.append(n)

for i in range(len(Ls)):
    L = Ls[i]
    dfstr = pd.DataFrame(columns = ['Dimerization', 'ZL'])
    
    for d in range(len(Dimer)):
        Dim = Dimer[d]
        D = float(Dimer[d][3] + '.' + Dimer[d][4])
        
        for k in range(len(arr)):
            num = arr[k] 
            myfile = '/home/liusf/tSDRG/testfunction/data2/'+ BC +'/'+ Jdis + '/'+ Dim + '/L'+ str(L) +'_P10_m30_'+ num + '/ZL.csv'
            df = pd.read_csv(myfile)  
            if(k == 0):
                dftc = df['ZL']
            dfc = df['ZL']

            if(k != 0):
                dftc += dfc

        dfavc = dftc/N                          ## first average(N times)
        mean = {'Dimerization':D ,'ZL':dfavc.mean()}  ## second average(L/2 times)
        dfstr.loc[d] = mean                     ## total average times = N * L/2

    plt.plot(dfstr['Dimerization'] ,dfstr['ZL'],"o-", markersize = 8, label = 'L=%d' %(L))
    #plt.plot(dfstr['delta'] ,dfstr['O^z'], color = 'b')

plt.xlabel(r'$Dimerization$', fontsize=14)
plt.ylabel(r'$Z(L)$', fontsize=12)
#plt.xlim(0.1,1.5)
#plt.ylim(0, 1)
#plt.xscale('log')
#plt.yscale('log')
plt.title(r'Dimerization vs $Z(L)$(average %d),spin = %s,$\delta$ = %s, $\chi$ = 30' % (int(N), spin,J), fontsize=12)
plt.legend(loc = 'best',fontsize=12)
plt.savefig( BC + '_' + Jdis +'_P10_m30_N' + str(N) +'_ZL-Dimerization.pdf', format='pdf', dpi=4000)
plt.show()
         