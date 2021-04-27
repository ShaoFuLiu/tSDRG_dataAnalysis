# Dimerization & String Order Parameter 
### Plot
import os
import math
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt 
from scipy.optimize import curve_fit

def choose_color(L):
    if (L % 4== 0):
        color = "r"
        #marker = "o-"
    elif (L % 4== 1):
        color = "g"
        #marker = "x-"
    elif (L % 4== 2):
        color = "b"
        #marker = "v-"
    elif (L % 4== 3):
        color = "y"
        #marker = "*-"
    return color

def choose_marker(delta):
    if (delta % 4 == 0):
        #color = "r"
        marker = "o-"
    elif (delta % 4 == 1):
        #color = "g"
        marker = "x-"
    elif (delta % 4 == 2):
        #color = "b"
         marker = "v-"
    elif (delta % 4 == 3):
        #color = "y"
        marker = "*-"
    return marker

spin = 2.0
BC = 'PBC'
P = 10
Ls = [64]
Jdis =['Jdis200','Jdis205','Jdis210','Jdis215','Jdis220']
chis = [40]
datanum = 4000
N = datanum

for i in range(len(Ls)):
    L = Ls[i]
    
    for m in range(len(chis)):

        for j in range(len(Jdis)):
            jdis = Jdis[j]
            """if j == 0:
                N = 1
            elif j != 0:
                N = datanum"""
            print(jdis)
            J = float(Jdis[j][4] + '.' + Jdis[j][5] + Jdis[j][6])
            M = chis[m]
            myfile = '/home/liusf/test/Sorting_data/Spin'+ str(int(spin)) +'/metadata/SOP/'+ jdis + '/Dimer-Oz/'+ BC +'_L'+ str(L) +'_P' + str(P) + '_m'+ str(M) +'_dim-sop_AV'+ str(N) +'.csv'
            df = pd.read_csv(myfile)
            plt.plot(df['Dimerization'] ,df['O^z'], 'o-', markersize = 6, label = 'L=%d, $\delta$ = %s, AVG(%d*%d)' %(L, J, N, L/2))
            plt.errorbar(df['Dimerization'], df['O^z'], yerr=df['error'], linestyle='None', capsize=3, capthick=1, label=None)        
        
plt.xlabel(r'$Dimerization$', fontsize=14)
plt.ylabel(r'$O^z(r=L/2)$', fontsize=14)
#plt.xlim(0.1,1.5)
#plt.ylim(0, 0.4)
#plt.xscale('log')
#plt.yscale('log')
plt.title(r'Dimerization vs $O^z(r=L/2)$, $\chi$ = %d'%(M), fontsize=12)
plt.legend(loc = 'best',fontsize=8)
plt.savefig( 'Spin2_'+ BC +'_P'+ str(P) +'_Oz-Dimerization2.pdf', format='pdf', dpi=4000)
plt.show()