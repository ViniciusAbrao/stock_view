# -*- coding: utf-8 -*-
"""
Created on Mon Aug 12 09:46:31 2019

@author: vinic_000
"""

import pandas_datareader as pdr
import datetime
import matplotlib.pyplot as plt
import numpy as np
from termcolor import colored

var_dia=0
simbolos = ['cnto3.SA','brkm5.SA','wege3.SA','qual3.SA','prio3.SA','guar3.SA','vivt4.SA','jslg3.SA','vvar3.SA']
sups=np.array([39.30,31.55,39.41,41.63,44.78,27.14,59.39,30.84,13.90])
plt.figure(1)
plt.close()
    
for i in range(sups.size):
    print(' ')
    start = datetime.datetime(2019, 12, 2)
    end = datetime.datetime(2020, 2, 27)
    historico = pdr.get_data_yahoo(simbolos[i], start=start, end=end)
    dados=historico.iloc[:,0:5].values
    plt.subplot(3,4,i+1)
    plt.title(simbolos[i])
    plt.plot(dados[:,3])
    ultima=dados[dados[:,3].size-1,3]*np.ones(dados[:,3].size)
    plt.plot(ultima)
    suporte=sups[i]*np.ones(dados[:,3].size)
    plt.plot(suporte)
    if dados[dados[:,3].size-1,3]>sups[i]:
        print(colored(simbolos[i], 'green'))
    else:
        print(colored(simbolos[i], 'red'))   
    var_dia=var_dia+dados[dados[:,3].size-1,3]-dados[dados[:,3].size-2,3]
    if dados[dados[:,3].size-1,3]>dados[dados[:,3].size-2,3]:
        print(colored(dados[dados[:,3].size-1,3], 'green'), sups[i])
    else:
        print(colored(dados[dados[:,3].size-1,3], 'red'), sups[i])

print(' ')
if var_dia>0:
    print(colored('variacao do dia:', 'green'))
    print(var_dia)
else:
    print(colored('variacao do dia:', 'red'))
    print(var_dia)

#np.savetxt('data1.csv', dados2, delimiter=',')