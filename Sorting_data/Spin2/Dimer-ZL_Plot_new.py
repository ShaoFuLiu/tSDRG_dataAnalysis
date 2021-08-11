# Dimerization & twist Order Parameter
### Plot
import os
import math
import pandas as pd
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
Ms = [40]
Ls = [64]
# Jdis = ['Jdis070','Jdis075','Jdis080','Jdis085','Jdis090','Jdis095','Jdis100','Jdis110','Jdis120','Jdis130','Jdis140','Jdis150']
Jdis = ['Jdis050','Jdis070','Jdis075','Jdis080','Jdis085','Jdis090','Jdis095','Jdis100','Jdis110','Jdis120','Jdis130','Jdis140','Jdis150','Jdis200','Jdis210','Jdis220','Jdis240','Jdis000']
N = 1000

for i in range(len(Ls)):
    L = Ls[i]
    dfstr = pd.DataFrame(columns = ['Dimerization', 'O^z'])

    for m in range(len(Ms)):
        M = Ms[m]
        for j in range(len(Jdis)):
            jdis = Jdis[j]
            J = float(Jdis[j][4] + '.' + Jdis[j][5] + Jdis[j][6])
            if (jdis == 'Jdis000'):
                N = 1
            myfile = '/home/liusf/tSDRG_DataAnalysis/Sorting_data/Spin'+ str(spin) +'/metadata/ZL/'+ jdis + '/Dimer-ZL/'+ BC +'_L'+ str(L) +'_P' + str(P) + '_m' + str(M) + '_dim-zl_AV'+ str(N) +'.csv'
            df = pd.read_csv(myfile)


            plt.plot(df['Dimerization'], df['ZL'], '-o', color=carr[i+j+m], markersize = 2, label = 'L=%d, R=%.2f, AVG=%d, $\chi$=%d' %(L, J, N, M))
            # plt.errorbar(df['Dimerization'], df['ZL'], color=carr[i+j+m], yerr=df['error'], linestyle='None', capsize=3, capthick=1, label=None)

plt.xlabel(r'$Dimerization$', fontsize=12)
plt.ylabel(r'$Z(L)$', fontsize=12)
# plt.xlim(0.05,0.3)
# plt.ylim(-0.2,0.3)
#plt.xscale('log')
#plt.yscale('log')
plt.title('spin = %s, $\chi$ = %d' % (spin, M), fontsize=12)
# plt.title('spin = %s' % (spin), fontsize=12)
plt.legend(loc = 'best',fontsize=6)
plt.grid(linestyle='-', linewidth=1)
# plt.savefig( jdis + '_Spin'+ str(spin) +'_' + BC + '_P'+ str(P) +'_m'+ str(M) +'_ZL-Dimerization.pdf', format='pdf', dpi=4000)
plt.savefig( 'Spin'+ str(spin) +'_'+ BC +'_P'+ str(P) +'_m'+ str(M) +'_ZL-Dimerization2.pdf', format='pdf', dpi=4000)
plt.show()