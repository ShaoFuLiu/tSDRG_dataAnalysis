## Distribution of Jlist ##
## plot ##

import os
import math
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt 
from scipy.optimize import curve_fit

L = 10000
Jdis = 'J0'
Dimer = ['D0']
for i in range(len(Dimer)):
    myfile = '/home/liusf/test/spin1/Distribution_Jdis/'+ Jdis + Dimer[i] +'_list.csv'
    df = pd.read_csv(myfile)
    up = 0
    down = 0.05
    n = 0.05
    df1 = pd.DataFrame(columns = ['mid', 'Prob'])
    df2 = pd.DataFrame(columns = ['mid', 'Prob'])

    for j in range(40):
        selected1 = df[df['J'].between(up,down)]['J']
        #selected2 = df[df['J2'].between(up,down)]['J2']
        mid = (up+down)/2 
        up += n
        down += n
        Prob1 = len(selected1)/L
        #Prob2 = len(selected2)/L
        mean1 = {'mid':mid ,'Prob':Prob1}
        #mean2 = {'mid':mid ,'Prob':Prob2}
        df1.loc[j] = mean1
        #df2.loc[j] = mean2
    plt.plot(df1['mid'], df1['Prob'], 'o-', markersize = 8, label = 'Dimer = %s' %(Dimer[i]))
#    plt.plot(df2['mid'], df2['Prob'], 'o-', markersize = 8, label = 'Dimer = %s' %(Dimer[i]))
#df['J2'].hist()

plt.xlabel('$J$', fontsize=14)
plt.ylabel('$P(J)$', fontsize=14)
plt.title(Jdis + 'D0_power-law_distribution', fontsize=12)
#plt.xlim(0,1)
#plt.ylim(0,0.1)
plt.legend(loc = 'best', fontsize=12)
plt.grid()
#plt.savefig('/home/liusf/test/spin1/Distribution_Jdis/'+ Jdis + Dimer +'_power-law_distribution.pdf', format='pdf', dpi=4000)
plt.savefig('/home/liusf/test/spin1/Distribution_Jdis/J0D0_distribution.pdf', format='pdf', dpi=4000)
plt.show()
