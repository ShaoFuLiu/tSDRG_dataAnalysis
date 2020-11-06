# String Order Parameter 
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

arr = []  #arr = ['1','2','3','4','5'...]
for i in range(N):
    n = str(init_seed+i)
    arr.append(n)

for j in range(len(Jdis)):
    jdis = Jdis[j]

    for l in range(len(Ls)):
        L = Ls[l]                

        for d in range(len(Dimer)):
            dimer = Dimer[d]

            for i in range(len(arr)):
                num = arr[i] 
                ## Source ##
                myfile = '/home/liusf/tSDRG/MainDim/data2/'+ BC +'/'+ jdis +'/'+ dimer +'/L'+ str(L) +'_P'+ str(P) +'_m30_'+ num + '/L'+ str(L) +'_P' + str(P) + '_m30_'+ num +'_string.csv'
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

            direc = '/home/liusf/test/Sorting_data/metadata/SOP/'+ jdis
            if (os.path.exists(direc) == False):
                os.mkdir(direc)
            direc2 = direc + '/' + dimer 
            if (os.path.exists(direc2) == False):
                os.mkdir(direc2)
            path = direc2 +'/'+ BC +'_L'+ str(L) +'_P' + str(P) + '_m30_sop_AV'+ str(N) +'.csv'
            dfavc.to_csv(path,index=0)

