# Dimerization & String Order Parameter 
### average raw data to meta data

import os
import math
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt 
from scipy.optimize import curve_fit

BC = 'PBC'
Ls = [32, 64]
Jdis = ['Jdis01','Jdis05','Jdis10']
Dimer = ['Dim01','Dim02','Dim03','Dim04','Dim05','Dim06','Dim07','Dim08','Dim09','Dim10']
P = 10
N = 100
init_seed = 1

arr = []
for j in range(N):
    n = str(init_seed+1)
    arr.append(n)

for i in range(len(Ls)):
    L = Ls[i]
    dfstr = pd.DataFrame(columns = ['Dimerization', 'O^z'])
    
    for j in range(len(Jdis)):
        jdis = Jdis[j]
        J = float(Jdis[j][4] + '.' + Jdis[j][5])

        for d in range(len(Dimer)):
            dimer = Dimer[d]
            D = float(Dimer[d][3] + '.' + Dimer[d][4])
            
            for k in range(len(arr)):
                num = arr[k] 
                myfile = '/home/liusf/tSDRG/MainDim/data2/'+ BC +'/'+ jdis + '/'+ dimer + '/L'+ str(L) +'_P10_m30_'+ num + '/L'+ str(L) +'_P10_m30_'+ num +'_string.csv'
                df = pd.read_csv(myfile)  
                if(k == 0):
                    dftc = df['corr']
                dfc = df['corr']

                if(k != 0):
                    dftc += dfc

            dfavc = dftc/N                          ## first average(N times)
            mean = {'Dimerization':D ,'O^z':dfavc.mean()}  ## second average(L/2 times)
            dfstr.loc[d] = mean                     ## total average times = N * L/2
            
        direc = '/home/liusf/test/Sorting_data/metadata/SOP/'+ jdis 
        if (os.path.exists(direc) == False):
            os.mkdir(direc)
        direc2 = direc + '/Dimer-Oz' 
        if (os.path.exists(direc2) == False):
            os.mkdir(direc2)
        path = direc2 +'/'+ BC +'_L'+ str(L) +'_P' + str(P) + '_m30_dim-sop_AV'+ str(N) +'.csv'
        dfstr.to_csv(path,index=0)
