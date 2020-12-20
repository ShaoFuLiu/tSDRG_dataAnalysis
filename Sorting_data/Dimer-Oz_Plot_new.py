# Dimerization & String Order Parameter 
### Plot
import os
import math
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt 
from scipy.optimize import curve_fit

BC = 'PBC'
Ls = [32,64,128,256]
Jdis = ['Jdis01','Jdis05','Jdis10']

init_D = 10
final_D = 60
space = 2
file_num = int ((final_D - init_D)/space+1)
Dimer = []
for i in range(file_num):
    D = init_D + space*i
    d = '0'+ str(D)[0] + str(D)[1]
    Dimer.append('Dim' + d)

def choose_color(L):
    if (L == 32):
        color = "r"
        #marker = "o-"
    elif (L == 64):
        color = "g"
        #marker = "x-"
    elif (L == 128):
        color = "b"
        #marker = "v-"
    elif (L == 256):
        color = "y"
        #marker = "*-"
    return color

def choose_marker(delta):
    if (delta == 0.1):
        #color = "r"
        marker = "o-"
    elif (delta == 0.5):
        #color = "g"
        marker = "x-"
    elif (delta == 1.0):
        #color = "b"
         marker = "v-"
    elif (delta == 1.5):
        #color = "y"
        marker = "*-"
    return marker

P = 10
init_seed = 1

for i in range(len(Ls)):
    L = Ls[i]
    print(L)
    dfstr = pd.DataFrame(columns = ['Dimerization', 'O^z'])
    
    if (L == 32 or L == 64):
        Jdis = ['Jdis01','Jdis05','Jdis10']
    if (L == 128 or L == 256):
        Jdis = ['Jdis01','Jdis05']
    
    for j in range(len(Jdis)):
        print(Jdis[j])
        if (L == 32):
            N = 10000
        """elif (L == 32 and j != 0):
            N = 1000"""
        if (L == 128 or L == 64):
            N = 1000
        elif (L == 256):
            N = 100

        jdis = Jdis[j]
        J = float(Jdis[j][4] + '.' + Jdis[j][5])

        myfile = '/home/liusf/test/Sorting_data/metadata/SOP/'+ jdis + '/Dimer-Oz/'+ BC +'_L'+ str(L) +'_P' + str(P) + '_m30_dim-sop_AV'+ str(N) +'.csv'
        df = pd.read_csv(myfile)
        
        if (L == 32 or L == 64):
            myfile2 = '/home/liusf/test/Sorting_data/metadata/SOP/'+ jdis + '/Dimer0-Oz/'+ BC +'_L'+ str(L) +'_P' + str(P) + '_m30_dim-sop_AV100.csv'
            
        if (L == 128 or L == 256):
            myfile2 = '/home/liusf/test/Sorting_data/metadata/SOP/'+ jdis + '/Dimer0-Oz/'+ BC +'_L'+ str(L) +'_P' + str(P) + '_m30_dim-sop_AV10.csv'
            
        df2 = pd.read_csv(myfile2)
        df = df2.append(df)

        plt.plot(df['Dimerization'] ,df['O^z'],choose_color(L)+choose_marker(J), markersize = 6, label = 'L=%d, $\delta$ = %s, AVG(%d)' %(L, J, N))
        plt.errorbar(df['Dimerization'], df['O^z'], yerr=df['error'], linestyle='None', capsize=3, capthick=1, label=None)        
        
        


plt.xlabel(r'$Dimerization$', fontsize=14)
plt.ylabel(r'$O^z(r=L/2)$', fontsize=14)
#plt.xlim(0.1,1.5)
#plt.ylim(0, 0.4)
#plt.xscale('log')
#plt.yscale('log')
plt.title(r'Dimerization vs $O^z(r=L/2)$, $\chi$ = 30', fontsize=12)
plt.legend(loc = 'best',fontsize=12)
plt.savefig( BC + '_P'+ str(P) +'_m30_Oz-Dimerization.pdf', format='pdf', dpi=4000)
plt.show()