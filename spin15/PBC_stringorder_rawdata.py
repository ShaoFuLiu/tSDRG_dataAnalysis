## Bulk Correlation for OBC/PBC ##
## average raw data ##import os

import os
import math
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt 
from scipy.optimize import curve_fit

BC = 'PBC'
Ls = [32, 64]
#Jdis = ['Jdis08', 'Jdis09', 'Jdis10', 'Jdis11', 'Jdis12']
Jdis = ['Jdis10']
N = 100  

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
            myfile = '/home/liusf/tSDRG/Main15/data/'+ BC +'/'+ delta +'/L'+ str(L) +'_P10_m30_'+ num + '/L'+ str(L) +'_P10_m30_'+ num +'_string.csv'
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

        direc = '/home/liusf/test/spin15/'+ delta
        path = direc +'/'+ BC +'_L'+ str(L) +'_P10_m30_string_N'+ str(N) +'.csv'
        if (os.path.exists(direc) == False):
            os.mkdir(direc)
        dfavc.to_csv(path,index=0)