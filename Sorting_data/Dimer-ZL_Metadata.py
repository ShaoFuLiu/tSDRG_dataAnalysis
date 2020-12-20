# Dimerization & String Order Parameter 
### average raw data to meta data

import os
import math
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt 
from scipy.optimize import curve_fit

BC = 'PBC'
Ls = [32,64,128]
Jdis = ['Jdis00']
Dimer = ['Dim01','Dim02','Dim03','Dim04','Dim05','Dim06','Dim07','Dim08','Dim09','Dim10']
P = 10
N = 1
init_seed = 1

arr = []
for j in range(N):
    n = str(init_seed+j)
    arr.append(n)

for i in range(len(Ls)):
    L = Ls[i]
    dfstr = pd.DataFrame(columns = ['Dimerization', 'ZL'])
    
    for j in range(len(Jdis)):
        jdis = Jdis[j]
        J = float(Jdis[j][4] + '.' + Jdis[j][5])

        for d in range(len(Dimer)):
            dimer = Dimer[d]
            D = float(Dimer[d][3] + '.' + Dimer[d][4])
            
            for k in range(len(arr)):
                num = arr[k] 
                #myfile = '/home/liusf/tSDRG/MainDim/data2/'+ BC +'/'+ jdis + '/'+ dimer + '/L'+ str(L) +'_P'+ str(P) +'_m30_'+ num + '/ZL.csv'
                myfile = '/home/liusf/tSDRG/MainDimZL/data2/'+ BC +'/'+ jdis + '/'+ dimer + '/L'+ str(L) +'_P'+ str(P) +'_m30_'+ num + '/ZL.csv'
                df = pd.read_csv(myfile)  
                if(k == 0):
                    dftc = df['ZL']
                dfc = df['ZL']

                if(k != 0):
                    dftc += dfc

            dfavc = dftc/N                          ## first average(N times)
            mean = {'Dimerization':D ,'ZL':dfavc.mean()}  ## second average(L/2 times)
            dfstr.loc[d] = mean                     ## total average times = N * L/2
            
        direc = '/home/liusf/tSDRG/Sorting_data/metadata/ZL/'+ jdis 
        if (os.path.exists(direc) == False):
            os.mkdir(direc)
        direc2 = direc + '/Dimer-ZL' 
        if (os.path.exists(direc2) == False):
            os.mkdir(direc2)
        path = direc2 +'/'+ BC +'_L'+ str(L) +'_P' + str(P) + '_m30_dim-zl_AV'+ str(N) +'.csv'
        dfstr.to_csv(path,index=0)
print('done')
