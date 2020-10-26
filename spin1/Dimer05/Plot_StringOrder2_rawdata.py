import os
import math
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt 
from scipy.optimize import curve_fit

BC = 'PBC'
Ls = [32, 64, 128]
Jdis = ['Jdis06','Jdis07','Jdis08','Jdis09','Jdis10','Jdis11','Jdis12','Jdis13','Jdis14','Jdis15']
Dim = 0.5
N = 100
"""
for j in range(len(Jdis)):
    delta = Jdis[j]

    for i in range(len(Ls)):
        L = Ls[i]
        arr = []  

        for i in range(N):
            n = str(1+i)
            arr.append(n)

        for i in range(len(arr)):
            num = arr[i] 
            myfile = '/home/liusf/tSDRG/MainDim/data/'+ BC +'/'+ delta +'/L'+ str(L) +'_P10_m30_'+ num + '/L'+ str(L) +'_P10_m30_'+ num +'_string.csv'
            df = pd.read_csv(myfile)  
            dfr = df['x2'] - df['x1']
            DataColle = {'x2-x1': dfr}
            dfR = pd.DataFrame(DataColle, columns=['x2-x1'])

            if(i == 0):
                dftc = df['corr']
            dfc = df['corr']

            if(i != 0):
                dftc += dfc

        dfavc = dftc/N
        dfavc = pd.concat([dfR,dfavc],axis=1)

        direc = '/home/liusf/test/spin1/Dimer05/'+ delta
        path = direc +'/'+ BC +'_L'+ str(L) +'_P10_m30_string_N'+ str(N) +'.csv'
        if (os.path.exists(direc) == False):
            os.mkdir(direc)
        dfavc.to_csv(path,index=0)
"""
for j in range(len(Jdis)):
    delta = Jdis[j]
    dfstr = pd.DataFrame(columns = ['ln(L)', 'ln(O^z)'])
    
    for i in range(len(Ls)):
        myfile = '/home/liusf/test/spin1/Dimer05/'+ delta +'/'+ BC +'_L'+ str(Ls[i]) +'_P10_m30_string_N'+ str(N) +'.csv'
        df = pd.read_csv(myfile)
        #mean = {'ln(L)':math.log(Ls[i]) ,'ln(O^z)': math.log(df['corr'].mean())}
        mean = {'ln(L)': Ls[i] ,'ln(O^z)': df['corr'].mean()}
        dfstr.loc[i] = mean

    plt.plot(dfstr['ln(L)'] ,dfstr['ln(O^z)'], "o-", markersize = 8, label = delta)
    #plt.plot(dfstr['ln(L)'] ,dfstr['ln(O^z)'])
#plt.xlabel(r'$lnL$', fontsize=14)
#plt.ylabel(r'$lnO^z(L/2)$', fontsize=14)
plt.xlabel(r'$L$', fontsize=14)
plt.ylabel(r'$O^z(L/2)$', fontsize=14)
#plt.xlim(3.3,5.7)
#plt.ylim(-4.6, -1.4)
#plt.xscale('log')
#plt.yscale('log')
plt.title(r'String order parameter(average %d), Dimer = %s, $\chi$ = 30, $\delta$ = 0.6 to 1.5' % (int(N), Dim), fontsize=12)
plt.legend(loc = 'best')
plt.savefig( BC +'_D05_P10_m30_string_N' + str(N) +'.pdf', format='pdf', dpi=4000)
plt.show()
         