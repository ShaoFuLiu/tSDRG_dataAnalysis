# Phase-Diagram
### Plot
import os
import math
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

spin = 1.0
BC = 'PBC'
P = 10
L = 64
M = 30
N = 1000

myfile = '/home/liusf/tSDRG_DataAnalysis/Sorting_data/Spin1/Phase-Diagram.csv'
df = pd.read_csv(myfile)
plt.plot( df['Dimerization'],df['Disorder'], '-o', markersize = 4)

plt.xlabel(r'$Dimerization$', fontsize=14)
plt.ylabel(r'$Disorder(J)$', fontsize=12)
plt.xlim(0,0.5)
#plt.ylim(-1, 1)
#plt.xscale('log')
#plt.yscale('log')
#plt.legend(loc = 'best',fontsize=8)
plt.title(r'Dimerization vs Disorder(J), spin = %s, L=%d, $\chi$= %d' % (spin, L, M), fontsize=12)
plt.grid(linestyle='-', linewidth=1)
plt.savefig( 'Spin1_'+ BC +'_P'+ str(P) +'_ZL-J2.pdf', format='pdf', dpi=4000)
plt.show()