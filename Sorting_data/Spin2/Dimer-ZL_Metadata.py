# Dimerization & String Order Parameter 
### average raw data to meta data

import os
import math
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt 
from scipy.optimize import curve_fit

BC = 'PBC'
Ls = [64]
Jdis = ['Jdis000']

init_D = 5 #0.05
final_D = 100 #1.0
space = 5
file_num = int ((final_D - init_D)/space+1)
Dimer = ['Dim000']
for i in range(file_num):
    D = init_D + space*i
    if (D < 10):
        d = '00' + str(D)[0]
        Dimer.append('Dim' + d)
    elif (D >= 10 and D < 100):
        d = '0' + str(D)[0] + str(D)[1]
        Dimer.append('Dim' + d)
    elif (D >= 100):
        d = str(D)[0] + str(D)[1] + str(D)[2]
        Dimer.append('Dim' + d)
    print(d)
P = 10
N = 1
m = 40
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
            D = float(Dimer[d][3] + '.' + Dimer[d][4] + Dimer[d][5])
            
            for k in range(len(arr)):
                num = arr[k] 
                #myfile = '/home/liusf/tSDRG/MainDim/data2/'+ BC +'/'+ jdis + '/'+ dimer + '/L'+ str(L) +'_P'+ str(P) +'_m30_'+ num + '/ZL.csv'
                myfile = '/home/liusf/tSDRG/2_MainDimZL/data2/'+ BC +'/'+ jdis + '/'+ dimer + '/L'+ str(L) +'_P'+ str(P) +'_m'+ str(m) +'_'+ num + '/ZL.csv'
                df = pd.read_csv(myfile)  
                if(k == 0):
                    dftc = df['ZL']
                dfc = df['ZL']

                if(k != 0):
                    dftc += dfc

            dfavc = dftc/N                          ## first average(N times)
            mean = {'Dimerization':D ,'ZL':dfavc.mean()}  ## second average(L/2 times)
            dfstr.loc[d] = mean                     ## total average times = N * L/2
            
        direc = '/home/liusf/tSDRG/Sorting_data/Spin2/metadata/ZL/'+ jdis 
        if (os.path.exists(direc) == False):
            os.mkdir(direc)
        direc2 = direc + '/Dimer-ZL' 
        if (os.path.exists(direc2) == False):
            os.mkdir(direc2)
        path = direc2 +'/'+ BC +'_L'+ str(L) +'_P' + str(P) + '_m'+str(m)+'_dim-zl_AV'+ str(N) +'.csv'
        dfstr.to_csv(path,index=0)
print('done')
