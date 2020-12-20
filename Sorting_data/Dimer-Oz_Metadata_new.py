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
Jdis = ['Jdis01']
##Dimer = ['Dim010','Dim012']
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
N = 10
init_seed = 1

arr = []
for j in range(N):
    n = str(init_seed+j)
    arr.append(n)

for i in range(len(Ls)):
    L = Ls[i]
    
    for j in range(len(Jdis)):
        dfstr = pd.DataFrame(columns = ['Dimerization', 'O^z', 'error'])
        jdis = Jdis[j]
        J = float(Jdis[j][4] + '.' + Jdis[j][5])

        for d in range(len(Dimer)):
            dimer = Dimer[d]
            D = float(Dimer[d][3] + '.' + Dimer[d][4] + Dimer[d][5])
            x = 0
            
            for k in range(len(arr)):
                num = arr[k]
                myfile = '/home/liusf/tSDRG/MainDim/data2/'+ BC +'/'+ jdis + '/'+ dimer + '/L'+ str(L) +'_P'+ str(P) +'_m30_'+ num + '/L'+ str(L) +'_P'+ str(P) +'_m30_'+ num +'_string.csv'
                df = pd.read_csv(myfile)
                dfc = df['corr']
                if(k == 0):
                    dftc = df['corr']                                
                if(k != 0):
                    dftc += dfc

            dfavc = dftc/N                          ## first average(N times)
            ## STD(Standard Deviation) and SEM(Standard Error of Mean) = error           
            for m in range(len(arr)):
                num = arr[m]
                myfile = '/home/liusf/tSDRG/MainDim/data2/'+ BC +'/'+ jdis + '/'+ dimer + '/L'+ str(L) +'_P'+ str(P) +'_m30_'+ num + '/L'+ str(L) +'_P'+ str(P) +'_m30_'+ num +'_string.csv'
                df = pd.read_csv(myfile)
                for l in range(int(L/2)):
                    x += np.square(df['corr'][l]-dfavc.mean()) ## second average(L/2 times)
            
            std = np.sqrt(x/(N*L/2-1))
            error = std/np.sqrt(N*L/2)
            mean = {'Dimerization':D ,'O^z':dfavc.mean(),'error':error}  
            ## total average times = N * L/2
            dfstr.loc[d] = mean
        
        direc = '/home/liusf/test/Sorting_data/metadata/SOP/'+ jdis 
        if (os.path.exists(direc) == False):
            os.mkdir(direc)
        direc2 = direc + '/Dimer-Oz' 
        if (os.path.exists(direc2) == False):
            os.mkdir(direc2)
        path = direc2 +'/'+ BC +'_L'+ str(L) +'_P' + str(P) + '_m30_dim-sop_AV'+ str(N) +'.csv'
        dfstr.to_csv(path,index=0)

print('all done')
