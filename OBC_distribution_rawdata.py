## Distribution of End to end correlations ##
## raw data to meta data ##

import os
import math
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt 
from scipy.optimize import curve_fit

BC = 'OBC'
Ls = [32, 48, 64, 96, 128, 256]
Jdis = ['Jdis10']
N = 200  #arr = ['1','2','3','4','5'...]
m = 30

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
            myfile = '/home/liusf/tSDRG/Main/data/data/'+ BC +'/'+ delta +'/L'+ str(L) +'_P10_m'+ str(m) +'_'+ num + '/L'+ str(L) +'_P10_m'+ str(m) +'_'+ num +'_corr1.csv'
            df2 = pd.read_csv(myfile)
            df2['corr'] = -df2['corr'].abs().apply(np.log)
            
            if (i == 0):
                df1 = pd.read_csv(myfile)
                df1['corr'] = -df1['corr'].abs().apply(np.log)
            else:
                df1 = pd.concat([df1,df2], ignore_index=True)
        
        direc = '/home/liusf/test/Distribution_end_to_end_correlation'
        path = direc + '/L' + str(L) + '_P10_m30_Jdis10_sum' + str(N) + '_corr1.csv'
        if (os.path.exists(direc) == False):
            os.mkdir(direc)
        df1.to_csv(path,index=0)