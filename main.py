# -*- coding: utf-8 -*-
"""

## Modelo epidemiologico (Modelo SIR ) de coronavirus con python

"""



#importamos librerias necesarias
import scipy.integrate as spi
import numpy as np
import pylab as pl

'''tamaño de la población'''
N=1*1e-8
beta=1.4247
gamma=0.14286
'''condiciones iniciales'''
TS=1.0   #Tiempo
S=1-1e-6 #S
I=1e-6   #I
R=0.0    #R
ND=70.0   

con_inicial = (S, I, R)


#parámetros del modelo (coeficientes de las variables)
def ecuaciones_diferenciales(INPUT,t):  
    Y=np.zeros((3))
    V = INPUT
    '''Las ecuaciones diferenciales'''
    Y[0] = - beta * V[0] * V[1]
    Y[1] = beta * V[0] * V[1] - gamma * V[1]
    Y[2] = gamma * V[1]
    return Y   

tiempo_inicial = 0.0; tiempo_final = ND; t_init = TS
rango_tiempo = np.arange(tiempo_inicial, tiempo_final+t_init, t_init)
RES = spi.odeint(ecuaciones_diferenciales,con_inicial,rango_tiempo)

#Gráfica
pl.plot(RES[:,0]*N, '-g', label='Susceptibles')
pl.plot(RES[:,2]*N, '-k', label='Recuperados')
pl.plot(RES[:,1]*N, '-r', label='Infectados')
pl.legend(loc=0)
pl.title('Modelo SIR ')
pl.xlabel('Tiempo')
pl.savefig('SIR_model')
