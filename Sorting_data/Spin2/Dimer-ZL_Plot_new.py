# Dimerization & twist Order Parameter
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
#Jdis = ['Jdis000','Jdis050','Jdis100','Jdis150','Jdis200','Jdis250']
Jdis = ['Jdis200','Jdis205','Jdis210','Jdis215','Jdis220']
chis = [40]
datanum = 7000
N = datanum

for i in range(len(Ls)):
    L = Ls[i]

    for m in range(len(chis)):

        for j in range(len(Jdis)):
            jdis = Jdis[j]
            J = float(Jdis[j][4] + '.' + Jdis[j][5] + Jdis[j][6])
            """if(jdis == 'Jdis200'):
                N = 1000
            elif(jdis != 'Jdis200'):
                N = datanum"""
            M = chis[m]
            myfile = '/home/liusf/test/Sorting_data/Spin'+ str(int(spin)) +'/metadata/ZL/'+ jdis + '/Dimer-ZL/'+ BC +'_L'+ str(L) +'_P' + str(P) + '_m' + str(M) + '_dim-zl_AV'+ str(N) +'.csv'
            df = pd.read_csv(myfile)
            plt.plot(df['Dimerization'], df['ZL'], choose_marker(j), markersize = 4, label = 'L=%d, R=%.2f, $\chi$= %d, AVG=%d' %(L, J, M, N))
            plt.errorbar(df['Dimerization'], df['ZL'], yerr=df['error'], linestyle='None', capsize=3, capthick=1, label=None)

plt.xlabel(r'$Dimerization$', fontsize=14)
plt.ylabel(r'$Z(L)$', fontsize=14)
plt.xlim(0.2,0.45)
plt.ylim(-0.005, 0.005)
#plt.xscale('log')
#plt.yscale('log')
plt.title(r'Dimerization vs $Z(L)$, spin = %s' % (spin), fontsize=12)
plt.legend(loc = 'best',fontsize=8)
plt.grid(linestyle='-', linewidth=1)
plt.savefig( 'Spin2_' + BC + '_P'+ str(P) +'_ZL-Dimerization7-2.pdf', format='pdf', dpi=4000)
plt.show()