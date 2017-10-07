#Matplotlib Plotting
#Autor: Javier Arturo Hernández Sosa
#Fecha: 30/Sep/2017
#Descripcion: Ejecicios Matplotlib Plotting - Alexandre Devert - (9)

import numpy as np
import matplotlib.pyplot as plt

#Leemos los datos
data = np.loadtxt('data2.txt')

#Transponemos los datos para que cada fila sea Y1, Y2 y Y3 y la primera fila  siempre sea X
#X,Y1  -  X,Y2 - X,Y3
for column in data.T:
    plt.plot(data[:,0], column)
'''
Otra forma sería como se viene trabajando en anteriores ejercicios
plt.plot(data[:,0],data[:,0])
plt.plot(data[:,0],data[:,1])
plt.plot(data[:,0],data[:,2])
'''
plt.show()