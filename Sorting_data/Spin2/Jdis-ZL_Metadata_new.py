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
Dimer = ["Dim000"]
Jdis = ['Jdis090','Jdis095','Jdis100','Jdis105','Jdis110','Jdis115','Jdis120']
P = 10
N = 100
init_seed = 1

arr = []
for j in range(N):
    n = str(init_seed+j)
    arr.append(n)

for i in range(len(Ls)):
    L = Ls[i]
    
    for d in range(len(Dimer)):
        dfstr = pd.DataFrame(columns = ['Jdis', 'ZL', 'error'])
        dimer = Dimer[d]
        
        for j in range(len(Jdis)):
            jdis = Jdis[j]
            J = float(Jdis[j][4] + '.' + Jdis[j][5] + Jdis[j][6])
            x = 0
            print(jdis+"_"+dimer)
            
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
            ## STD(Standard Deviation) and SEM(Standard Error of Mean) = error           
            for m in range(len(arr)):
                num = arr[m]
                myfile = '/home/liusf/tSDRG/MainDimZL/data2/'+ BC +'/'+ jdis + '/'+ dimer + '/L'+ str(L) +'_P'+ str(P) +'_m30_'+ num + '/ZL.csv'
                df = pd.read_csv(myfile)
                x += np.square(df['ZL'][0]-dfavc.mean()) ## second average(L/2 times)
            
            std = np.sqrt(x/(N-1))
            error = std/np.sqrt(N)
            mean = {'Jdis':J ,'ZL':dfavc.mean(),'error':error}  
            ## total average times = N * L/2
            dfstr.loc[j] = mean                     
            
        direc = '/home/liusf/tSDRG/Sorting_data/metadata/ZL/' + dimer 
        if (os.path.exists(direc) == False):
            os.mkdir(direc)
        direc2 = direc + '/Jdis-ZL' 
        if (os.path.exists(direc2) == False):
            os.mkdir(direc2)
        path = direc2 +'/'+ BC +'_L'+ str(L) +'_P' + str(P) + '_m30_jdis-zl_AV'+ str(N) +'.csv'
        dfstr.to_csv(path,index=0)
print('done')
