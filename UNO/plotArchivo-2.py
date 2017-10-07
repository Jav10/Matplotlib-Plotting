#Matplotlib Plotting
#Autor: Javier Arturo Hernández Sosa
#Fecha: 30/Sep/2017
#Descripcion: Ejecicios Matplotlib Plotting - Alexandre Devert - (8)

import numpy as np
import matplotlib.pyplot as plt

'''
    Cargamos el archivo con numpy
    hace la separación y la transforma en array
    con listas normales la sintaxis para seleccionar columas sería así:
    datos[:][0]   datos[:][1]
'''
datos = np.loadtxt('data1.txt')
plt.plot(datos[:,0],datos[:,1])
plt.show()