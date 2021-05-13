# Dimerization & String Order Parameter
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
'coral':                '#FF7F50',
'cornflowerblue':       '#6495ED',
'cornsilk':             '#FFF8DC',
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
'lavender':             '#E6E6FA',
'lavenderblush':        '#FFF0F5',
'lawngreen':            '#7CFC00',
'lemonchiffon':         '#FFFACD',
'lime':                 '#00FF00',
'limegreen':            '#32CD32',
'linen':                '#FAF0E6',
'magenta':              '#FF00FF',
'maroon':               '#800000',
'mediumaquamarine':     '#66CDAA',
'mediumblue':           '#0000CD',
'mediumorchid':         '#BA55D3',
'mediumpurple':         '#9370DB',
'mediumseagreen':       '#3CB371',
'mediumslateblue':      '#7B68EE',
'mediumspringgreen':    '#00FA9A',
'mediumturquoise':      '#48D1CC',
'mediumvioletred':      '#C71585',
'midnightblue':         '#191970',
'mintcream':            '#F5FFFA',
'mistyrose':            '#FFE4E1',
'moccasin':             '#FFE4B5',
'navajowhite':          '#FFDEAD',
'navy':                 '#000080',
'oldlace':              '#FDF5E6',
'olive':                '#808000',
'olivedrab':            '#6B8E23',
'orange':               '#FFA500',
'orangered':            '#FF4500',
'orchid':               '#DA70D6'}
carr = []
for cmap in cnames.keys():
    carr.append(cmap)

spin = int(2)
BC = 'PBC'
P = 10
M = 40
Ls = [16,32,48,64,96,128,256]
#Jdis = ['Jdis050','Jdis100','Jdis150','Jdis200','Jdis250','Jdis300','Jdis350','Jdis400','Jdis450']
Dimer = ["Dim000"]
Ns = [2000,2000,2000,2000,1000,1000,500]
init_seed = 1

for l in range(len(Ls)):
    L = Ls[l]
    N = Ns[l]

    for d in range(len(Dimer)):
        dimer = Dimer[d]
        D = float(Dimer[d][3] + '.' + Dimer[d][4])
        myfile = '/home/liusf/test/Sorting_data/Spin'+ str(spin) +'/metadata/ZL/'+ dimer + '/Jdis-ZL/'+ BC +'_L'+ str(L) +'_P' + str(P) + '_m' + str(M) + '_jdis-zl_AV'+ str(N) +'.csv'
        df = pd.read_csv(myfile)
        plt.plot(df['Jdis'], df['ZL'], "o-", color=carr[l+d], markersize = 2, label = 'L=%d, AVG(%d)' %(L, N))
        if (N != 1):
            plt.errorbar(df['Jdis'], df['ZL'], yerr=df['error'], linestyle='None', capsize=3, capthick=1, color=carr[l+d], label=None)

plt.xlabel(r'$R$', fontsize=14)
plt.ylabel(r'$Z(L)$', fontsize=12)
#plt.xlim(0.6,1)
#plt.ylim(0.15, 0.2)
#plt.xscale('log')
#plt.yscale('log')
plt.title('spin = %s, $\dimer$ = %s, $\chi$ = 40' % (spin, D), fontsize=12)
plt.legend(loc = 'best',fontsize=12)
plt.grid(linestyle='-', linewidth=1)
#plt.savefig( 'Spin'+ str(spin) +'_' + BC +'_'+ dimer +'_P'+ str(P) +'_m40_ZL-Jdis.pdf', format='pdf', dpi=4000)
plt.savefig( 'Spin'+ str(spin) +'_' + BC + '_P'+ str(P) +'_ZL-Jdis.pdf', format='pdf', dpi=4000)
plt.show()