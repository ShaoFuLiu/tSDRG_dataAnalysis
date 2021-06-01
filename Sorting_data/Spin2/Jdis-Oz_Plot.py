# Dimerization & String Order Parameter
### Plot
import os
import math
import pandas as pd
import random
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

cnames = {
'blue':                 '#0000FF',
'blueviolet':           '#8A2BE2',
'brown':                '#A52A2A',
'burlywood':            '#DEB887',
'cadetblue':            '#5F9EA0',
'chocolate':            '#D2691E',
'crimson':              '#DC143C',
'cyan':                 '#00FFFF',
'darkblue':             '#00008B',
'darkcyan':             '#008B8B',
'darkgoldenrod':        '#B8860B',
'darkgray':             '#A9A9A9',
'darkgreen':            '#006400',
'darkkhaki':            '#BDB76B',
'darkmagenta':          '#8B008B',
'darkolivegreen':       '#556B2F',
'darkorange':           '#FF8C00',
'darkorchid':           '#9932CC',
'darkred':              '#8B0000',
'darksalmon':           '#E9967A',
'darkseagreen':         '#8FBC8F',
'darkslateblue':        '#483D8B',
'darkslategray':        '#2F4F4F',
'darkturquoise':        '#00CED1',
'darkviolet':           '#9400D3',
'deeppink':             '#FF1493',
'deepskyblue':          '#00BFFF',
'dimgray':              '#696969',
'dodgerblue':           '#1E90FF',
'firebrick':            '#B22222',
'floralwhite':          '#FFFAF0',
'forestgreen':          '#228B22',
'fuchsia':              '#FF00FF',
'gainsboro':            '#DCDCDC',
'ghostwhite':           '#F8F8FF',
'gold':                 '#FFD700',
'goldenrod':            '#DAA520',
'gray':                 '#808080',
'green':                '#008000',
'greenyellow':          '#ADFF2F',
'honeydew':             '#F0FFF0',
'hotpink':              '#FF69B4',
'indianred':            '#CD5C5C',
'indigo':               '#4B0082',
'ivory':                '#FFFFF0',
'khaki':                '#F0E68C',
'orangered':            '#FF4500',
'orchid':               '#DA70D6'}
carr = []
for cmap in cnames.keys():
    carr.append(cmap)

spin = int(2)
BC = 'PBC'
P = 10
M = 40
Ls = [32,48,64,96,128,256]
# Jdis = ['Jdis090','Jdis095','Jdis100','Jdis105','J1is110','Jdis115','Jdis120']
Dimer = ["Dim000"]
Ns = [1000,1000,1000,1000,1000,500]
init_seed = 1

for l in range(len(Ls)):
    L = Ls[l]
    N = Ns[l]

    for d in range(len(Dimer)):
        dimer = Dimer[d]
        D = float(Dimer[d][3] + '.' + Dimer[d][4])

        myfile = '/home/liusf/tSDRG_DataAnalysis/Sorting_data/Spin'+ str(spin) +'/metadata/SOP/'+ dimer + '/Jdis-Oz/'+ BC +'_L'+ str(L) +'_P' + str(P) + '_m'+ str(M) +'_jdis-sop_AV'+ str(N) +'.csv'
        df = pd.read_csv(myfile)
        plt.plot(df['Jdis'], df['O^z'], "o-", color=carr[l+d], markersize = 2, label = 'L=%d, AVG(%d)' %(L, N))
        if (N != 1):
            plt.errorbar(df['Jdis'], df['O^z'], yerr=df['error'], linestyle='None', capsize=3, capthick=1, color=carr[l+d], label=None)

plt.xlabel(r'$R$', fontsize=12)
plt.ylabel(r'$O^z(r=L/2)$', fontsize=12)
#plt.xlim(0.9,1.2)
plt.ylim(0.1, -0.3)
#plt.xscale('log')
#plt.yscale('log')
plt.grid(linestyle='-', linewidth=1)
plt.title('spin = %s, $\dimer$ = %s, $\chi$ = %d' % (spin, D, M), fontsize=12)
plt.legend(loc = 'best',fontsize=8)
plt.savefig( 'Spin'+ str(spin) +'_' + BC + '_P'+ str(P) +'_Oz-Jdis.pdf', format='pdf', dpi=4000)
plt.show()