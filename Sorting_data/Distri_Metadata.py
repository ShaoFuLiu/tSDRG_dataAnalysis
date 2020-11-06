# Distribution of End to end correlations 
### raw data to meta data 

import os
import math
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt 
from scipy.optimize import curve_fit

BC = 'OBC'
Ls = [32, 64]
Jdis = 'Jdis10'
J = float(Jdis[4] + '.' + Jdis[5])
#Dimer = ['Dim01','Dim02','Dim03','Dim04','Dim05','Dim06','Dim07','Dim08','Dim09','Dim10']
P = 10
N = 10000
init_seed = 1

arr = []  #arr = ['1','2','3','4','5'...]
for i in range(N):
    n = str(init_seed+i)
    arr.append(n)

for l in range(len(Ls)):
    L = Ls[l]
        
    for d in range(len(Dimer)):
        dimer = Dimer[d]

        for i in range(len(arr)):
            num = arr[i] 
            ## Source ##
            myfile = '/home/liusf/tSDRG/MainDim/data2/'+ BC +'/'+ Jdis +'/'+ dimer +'/L'+ str(L) +'_P'+ str(P) +'_m30_'+ num + '/L'+ str(L) +'_P' + str(P) + '_m30_'+ num +'_corr1.csv'
            df2 = pd.read_csv(myfile)
            df2['corr'] = -df2['corr'].abs().apply(np.log)
            
            if (i == 0):
                df1 = pd.read_csv(myfile)
                df1['corr'] = -df1['corr'].abs().apply(np.log)
            else:
                df1 = pd.concat([df1,df2], ignore_index=True)

        direc = '/home/liusf/test/Sorting_data/metadata/Distribution_end_to_end_correlation/'+ dimer
        if (os.path.exists(direc) == False):
            os.mkdir(direc)
        path = direc + '/L' + str(L) + '_P' + str(P) + '_m30_'+ Jdis +'_Sample' + str(N) + '_corr1.csv'
        df1.to_csv(path,index=0)
