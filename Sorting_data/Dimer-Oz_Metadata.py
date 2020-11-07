# Dimerization & String Order Parameter 
### average raw data to meta data

import os
import math
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt 
from scipy.optimize import curve_fit

BC = 'PBC'
Ls = [32]
Jdis = ['Jdis01','Jdis05']

init_D = 10
final_D = 30
space = 2
file_num = int ((final_D - init_D)/space+1)
Dimer = []
for i in range(file_num):
    D = init_D + space*i
    d = '0'+ str(D)[0] + str(D)[1]
    Dimer.append('Dim' + d)
init_D2 = 40
for i in range(11):
    D = init_D2 + space*i
    d = '0'+ str(D)[0] + str(D)[1]
    Dimer.append('Dim' + d)

P = 20
N = 1000
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
            D = float(Dimer[d][3] + '.' + Dimer[d][4] + Dimer[d][5])
            
            for k in range(len(arr)):
                num = arr[k] 
                myfile = '/home/liusf/tSDRG/MainDim/data2/'+ BC +'/'+ jdis + '/'+ dimer + '/L'+ str(L) +'_P'+ str(P) +'_m30_'+ num + '/L'+ str(L) +'_P'+ str(P) +'_m30_'+ num +'_string.csv'
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
