import os
import math
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt 
from scipy.optimize import curve_fit

BC = 'PBC'
P = 20
Ls = [32]
Jdis = ['Jdis01','Jdis05','Jdis10']
Dimer = ['Dim01','Dim02','Dim03','Dim04','Dim05','Dim06','Dim07','Dim08','Dim09','Dim10','Dim11','Dim12','Dim13','Dim14','Dim15',]
N = 100  

arr = []
for l in range(N):
    n = str(1+l)
    arr.append(n)

for i in range(len(Ls)):
    L = Ls[i]
    dfstr = pd.DataFrame(columns = ['Dimerization', 'O^z'])
    
    for j in range(len(Jdis)):
        delta = Jdis[j]
        J = float(Jdis[j][4] + '.' + Jdis[j][5])

        for d in range(len(Dimer)):
            Dim = Dimer[d]
            D = float(Dimer[d][3] + '.' + Dimer[d][4])
            
            for k in range(len(arr)):
                num = arr[k] 
                myfile = '/home/liusf/tSDRG/MainDim/data2/'+ BC +'/'+ delta + '/'+ Dim + '/L'+ str(L) +'_P'+ str(P) +'_m30_'+ num + '/L'+ str(L) +'_P' + str(P) + '_m30_'+ num +'_string.csv'
                df = pd.read_csv(myfile)  
                if(k == 0):
                    dftc = df['corr']
                dfc = df['corr']

                if(k != 0):
                    dftc += dfc

            dfavc = dftc/N                          ## first average(N times)
            mean = {'Dimerization':D ,'O^z':dfavc.mean()}  ## second average(L/2 times)
            dfstr.loc[d] = mean                     ## total average times = N * L/2

        plt.plot(dfstr['Dimerization'] ,dfstr['O^z'],"o-", markersize = 8, label = 'L=%d, $\delta$ = %s ' %(L, J))
        #plt.plot(dfstr['delta'] ,dfstr['O^z'], color = 'b')

plt.xlabel(r'$Dimerization$', fontsize=14)
plt.ylabel(r'$O^z(r=L/2)$', fontsize=14)
#plt.xlim(0.1,1.5)
#plt.ylim(0, 0.4)
#plt.xscale('log')
#plt.yscale('log')
plt.title(r'Dimerization vs $O^z(r=L/2)$(average %d), $\chi$ = 30' % (int(N)), fontsize=12)
plt.legend(loc = 'best',fontsize=12)
plt.savefig( BC + '_L_J_P'+ str(P) +'_m30_N' + str(N) +'_Oz-Dimerization.pdf', format='pdf', dpi=4000)
plt.show()
         