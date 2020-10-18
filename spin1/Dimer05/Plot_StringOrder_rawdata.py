import os
import math
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt 
from scipy.optimize import curve_fit
## String Order Parameter ##
## plot delta vs O^z ##
BC = 'PBC'
Ls = [32, 64, 128]
Jdis = ['Jdis01','Jdis02','Jdis03','Jdis04','Jdis05','Jdis06','Jdis07','Jdis08','Jdis09','Jdis10','Jdis11','Jdis12','Jdis13','Jdis14','Jdis15']
Dim = 0.5
N = 100  

arr = []
for j in range(N):
    n = str(1+j)
    arr.append(n)

for i in range(len(Ls)):
    L = Ls[i]
    dfstr = pd.DataFrame(columns = ['delta', 'O^z'])
    
    for d in range(len(Jdis)):
        J = Jdis[d]
        delta = Jdis[d][4] + '.' + Jdis[d][5]
        D = float(delta)
        
        for k in range(len(arr)):
            num = arr[k] 
            myfile = '/home/liusf/tSDRG/MainDim/data/'+ BC +'/'+ J +'/L'+ str(L) +'_P10_m30_'+ num + '/L'+ str(L) +'_P10_m30_'+ num +'_string.csv'
            df = pd.read_csv(myfile)  
            if(k == 0):
                dftc = df['corr']
            dfc = df['corr']

            if(k != 0):
                dftc += dfc

        dfavc = dftc/N                          ## first average(N times)
        mean = {'delta':D ,'O^z':dfavc.mean()}  ## second average(L/2 times)
        dfstr.loc[d] = mean                     ## total average times = N * L/2

    plt.plot(dfstr['delta'] ,dfstr['O^z'],"o-", markersize = 8, label = 'L=%d' %(L))
    #plt.plot(dfstr['delta'] ,dfstr['O^z'], color = 'b')

plt.xlabel(r'$delta$', fontsize=14)
plt.ylabel(r'$O^z(r=L/2)$', fontsize=14)
#plt.xlim(0.1,1.5)
#plt.ylim(0, 0.4)
#plt.xscale('log')
#plt.yscale('log')
plt.title(r'delta vs $O^z(r=L/2)$(average %d), Dimer = %s, $\chi$ = 30' % (int(N), Dim), fontsize=12)
plt.legend(loc = 'best',fontsize=12)
plt.savefig( BC + '_D05_P10_m30_N' + str(N) +'_Oz-delta.pdf', format='pdf', dpi=4000)
plt.show()