## Bulk Correlation for OBC/PBC ##
## average raw data ##import os

import os
import math
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt 
from scipy.optimize import curve_fit

BC = 'OBC'
Ls = [32, 48, 64, 96, 128, 256]
Jdis = ['Jdis10']
N = 200  
init_seed = 1

for j in range(len(Jdis)):
    delta = Jdis[j]

    for i in range(len(Ls)):
        L = Ls[i]
        arr = []  #arr = ['1','2','3','4','5'...]

        for i in range(N):
            n = str(init_seed+i)
            arr.append(n)

        for i in range(len(arr)):
            num = arr[i] 
            myfile = '/home/liusf/tSDRG/Main/data/data/'+ BC +'/'+ delta +'/L'+ str(L) +'_P10_m30_'+ num + '/L'+ str(L) +'_P10_m30_'+ num +'_corr1.csv'
            df = pd.read_csv(myfile)  
            dfr = df['x2'] - df['x1']
            DataColle = {'x2-x1': dfr}
            dfR = pd.DataFrame(DataColle, columns=['x2-x1'])
            dfc = df['corr']
            
            if(i == 0):
                dftc = df['corr']

            if(i != 0):
                dftc += dfc

        for j in range(len(dftc)):
                dftc[j] = pow(-1,dfr[j])*dftc[j]  

        dfavc = dftc/N
        dfavc = pd.concat([dfR,dfavc],axis=1)

        direc = '/home/liusf/test/'+ delta
        path = direc +'/'+ BC +'_L'+ str(L) +'_P10_m30_corr1_N'+ str(N) +'.csv'
        if (os.path.exists(direc) == False):
            os.mkdir(direc)
        dfavc.to_csv(path,index=0)