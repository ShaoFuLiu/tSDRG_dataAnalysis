# Bulk Correlation 
### average raw data to meta data

import os
import math
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt 
from scipy.optimize import curve_fit

BC = 'PBC'
Ls = [32, 64]
Jdis = 'Jdis01'
J = float(Jdis[4] + '.' + Jdis[5])
Dimer = ['Dim01','Dim02','Dim03','Dim04','Dim05','Dim06','Dim07','Dim08','Dim09','Dim10']
P = 10
N = 100
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
            df = pd.read_csv(myfile)  
            dfr = df['x2'] - df['x1']
            DataColle = {'x2-x1': dfr}
            dfR = pd.DataFrame(DataColle, columns=['x2-x1'])
            dfc = df['corr']
            
            if(i == 0):
                dftc = df['corr']

            if(i != 0):
                dftc += dfc

        for j in range(len(dftc)):  #Cb(r) = [(−1)^r·Si· Si+r⟩]
                dftc[j] = pow(-1,dfr[j])*dftc[j]  

        dfavc = dftc/N
        dfavc = pd.concat([dfR,dfavc],axis=1)

        dfM = pd.DataFrame(columns = ['x2-x1', 'corr'])
        for dist in range(int(Ls[l]/2)):
            r = dist+1
            dfsr = dfavc.loc[dfavc['x2-x1'] == r]
            mean = {'x2-x1':r ,'corr': dfsr['corr'].mean()}
            dfM.loc[dist] = mean

        direc = '/home/liusf/test/Sorting_data/metadata/Corr/'+ dimer
        if (os.path.exists(direc) == False):
            os.mkdir(direc)
        path = direc +'/'+ BC +'_L'+ str(L) +'_P' + str(P) + '_m30_corr_AV'+ str(N) +'.csv'
        dfM.to_csv(path,index=0)
