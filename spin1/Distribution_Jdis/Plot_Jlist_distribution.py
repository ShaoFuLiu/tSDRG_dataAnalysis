## Distribution of Jlist ##
## plot ##

import os
import math
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt 
from scipy.optimize import curve_fit

L = 10000
Jdis = 'J1'
myfile = '/home/liusf/test/spin1/Distribution_Jdis/'+ Jdis +'_list.csv'
df = pd.read_csv(myfile)

up = 0
down = 0.05
n = 0.05
df2 = pd.DataFrame(columns = ['mid', 'Prob'])

for j in range(19):
    #print((left+right)/2)
    mid = (up+down)/2 
    selected = df[df['J'].between(up,down)]['J']
    up += n
    down += n
    Prob = len(selected)/L
    mean = {'mid':mid ,'Prob':Prob}  
    df2.loc[j] = mean

plt.plot(df2['mid'], df2['Prob'], 'o-', markersize = 8)

plt.xlabel('$J$', fontsize=14)
plt.ylabel('$P(J)$', fontsize=14)
plt.title(Jdis +'_power-law_distribution', fontsize=12)
plt.xlim(0,1)
#plt.ylim(0,0.1)
#plt.legend(loc = 'best', fontsize=12)
plt.grid()
plt.savefig('./'+ Jdis +'_power-law_distribution.pdf', format='pdf', dpi=4000)
plt.show()
