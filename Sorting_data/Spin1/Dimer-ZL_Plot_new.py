# Dimerization & twist Order Parameter
### Plot
import os
import math
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def choose_color(L):
    if (L == 0):
        color = "r"
        #marker = "o-"
    elif (L == 1):
        color = "g"
        #marker = "x-"
    elif (L == 2):
        color = "b"
        #marker = "v-"
    elif (L == 3):
        color = "y"
        #marker = "*-"
    return color

def choose_marker(delta):
    if (delta == 0):
        #color = "r"
        marker = "o-"
    elif (delta == 1):
        #color = "g"
        marker = "x-"
    elif (delta == 2):
        #color = "b"
         marker = "v-"
    elif (delta == 3):
        #color = "y"
        marker = "*-"
    return marker

spin = 1.0
BC = 'PBC'
P = 10
Ls = [64]
Jdis = ['Jdis000','Jdis020','Jdis040','Jdis060','Jdis080','Jdis100','Jdis105','Jdis110','Jdis150','Jdis200']
chis = [30]
N = 1000

for i in range(len(Ls)):
    L = Ls[i]
    dfstr = pd.DataFrame(columns = ['Dimerization', 'O^z'])
    """if(L == 64):
        N = 1000
    elif(L != 64):
        N = datanum"""
    for m in range(len(chis)):
        M = chis[m]
        for j in range(len(Jdis)):
            jdis = Jdis[j]
            J = float(Jdis[j][4] + '.' + Jdis[j][5] + Jdis[j][6])
            if(j == 0):
                N = 1
            elif(j != 0):
                N = 1000 # plot for both nonrandom and random

            myfile = '/home/liusf/test/Sorting_data/Spin1/metadata/ZL/'+ jdis + '/Dimer-ZL/'+ BC +'_L'+ str(L) +'_P' + str(P) + '_m' + str(M) + '_dim-zl_AV'+ str(N) +'.csv'
            df = pd.read_csv(myfile)
            #plt.plot(df['Dimerization'], df['ZL'], choose_color(i)+choose_marker(j), markersize = 4, label = 'L=%d, R=%.2f, $\chi$= %d, AVG=%d' %(L, J, M, N))
            plt.plot(df['Dimerization'], df['ZL'], '-o', markersize = 4, label = 'L=%d, R=%.2f, $\chi$= %d, AVG=%d' %(L, J, M, N))
            plt.errorbar(df['Dimerization'], df['ZL'], yerr=df['error'], linestyle='None', capsize=3, capthick=1, label=None)

plt.xlabel(r'$Dimerization$', fontsize=14)
plt.ylabel(r'$Z(L)$', fontsize=12)
plt.xlim(0,0.3)
plt.ylim(-0.2,0.2)
#plt.xscale('log')
#plt.yscale('log')
plt.title(r'Dimerization vs $Z(L)$, spin = %s' % (spin), fontsize=12)
plt.legend(loc = 'best',fontsize=8)
plt.grid(linestyle='-', linewidth=1)
plt.savefig( 'Spin1_'+ BC +'_P'+ str(P) +'_ZL-Dimerization.pdf', format='pdf', dpi=4000)
plt.show()