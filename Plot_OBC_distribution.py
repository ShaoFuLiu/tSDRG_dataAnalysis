## Distribution of End to end correlations ##
## plot ##

import os
import math
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt 
from scipy.optimize import curve_fit

BC = 'OBC'
Ls = [32, 48, 64, 96, 128, 256]
Jdis = 'Jdis10'
N = 200

for i in range(len(Ls)):
    myfile = '/home/liusf/test/Distribution_end_to_end_correlation/L' + str(Ls[i]) + '_P10_m30_Jdis10_sum200_corr1.csv'
    df = pd.read_csv(myfile)

    left = -1
    right = 0.5
    n = 1.5
    df2 = pd.DataFrame(columns = ['mid', 'lnP'])

    for j in range(6):
        #print((left+right)/2)
        mid = (left+right)/2 
        selected = df[df['corr'].between(left,right)]['corr']
        left += n
        right += n
        print(len(selected)/10000)
        lnP = math.log(len(selected)/10000)
        mean = {'mid':mid ,'lnP':lnP}  
        df2.loc[j] = mean

    plt.plot(df2['mid'], df2['lnP'], 'o-', markersize = 8, label = 'L=%d' %(Ls[i]))

plt.xlabel('$x = -ln(C_1(L))$', fontsize=14)
plt.ylabel('$lnP(x)$', fontsize=14)
plt.title('OBC correlation distribution(average %d) , %s, $\chi$ = 30' %(int(N), Jdis), fontsize=12)
plt.legend(loc = 'best', fontsize=12)
plt.grid()
plt.savefig( BC +'_distribution_P10_m30_'+ Jdis +'_sum'+ str(N) +'.pdf', format='pdf', dpi=4000)
plt.show()