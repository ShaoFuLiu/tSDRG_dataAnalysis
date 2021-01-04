# String Order Parameter 
### Plot L vs Oz

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

for j in range(len(Jdis)):
    J = Jdis[j][4] + '.' + Jdis[j][5]
    delta = float(J)
    dfstr = pd.DataFrame(columns = ['L', 'O^z'])
    #dfstrLOG = pd.DataFrame(columns = ['ln(L)', 'ln(O^z)'])
    
    for i in range(len(Ls)):
        direc = './metadata/SOP/' + Jdis[j] + '/' + Dimer
        myfile = direc +'/'+ BC +'_L'+ str(Ls[i]) +'_P' + str(P) + '_m30_sop_AV'+ str(N) +'.csv'
        df = pd.read_csv(myfile)
        mean = {'L':Ls[i] ,'O^z': df['corr'].mean()}
        #meanLOG = {'ln(L)':math.log(Ls[i]) ,'ln(O^z)': math.log(df['corr'].mean())}    # sometimes its can't do because sop=0
        dfstr.loc[i] = mean
        #dfstrLOG.loc[i] = mean

    plt.plot(dfstr['L'] ,dfstr['O^z'], "o-", markersize = 8, label = '$\delta$ = %s' %(delta))
    #plt.plot(dfstrLOG['ln(L)'] ,dfstrLOG['ln(O^z)'], "o-", markersize = 8, label = '$\delta$ = %s' %(delta))

plt.xlabel(r'$L$', fontsize=14)
plt.ylabel(r'$O^z(L/2)$', fontsize=14)
#plt.xlim(3.3,5.7)
# plt.ylim(-4.6, -1.4)
#plt.xscale('log')
#plt.yscale('log')
plt.title(r'L vs $O^z(r=L/2)$(average %d), Dimer = %s,$\chi$ = 30' % (int(N), D), fontsize=12)
plt.legend(loc = 'best')
plt.savefig( BC +'_P'+ str(P) + '_' + Dimer + '_m30_L-Oz_AV' + str(N) +'.pdf', format='pdf', dpi=4000)
plt.show()