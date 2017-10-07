#Matplotlib Plotting
#Autor: Javier Arturo Hernández Sosa
#Fecha: 30/Sep/2017
#Descripcion: Ejecicios Matplotlib Plotting - Alexandre Devert - (14)
#Gráfico de Barras Multiple

import matplotlib.pyplot as plt
import numpy as np

#Generamos los datos 3 gráficas
data = [[5.,25.,50.,20,],
        [4.,23.,51.,17.],
        [6.,22.,52.,19.]]

#Una lista con los colores
color_list = ['b', 'g', 'r']
#Creamos el ancho de las barras
gap=0.8/len(data)
#La función enumerate() enumera los valores del iterable desde 0 -> (0,valor1),(1,valor2)
for i, row in enumerate(data):
    #Creamos las coordenadas en X
    X = np.arange(len(row))
    #Pasamos los parámetros a la función bar() iterados por el for
    plt.bar(X + i * gap, row,
            width=gap,
            color=color_list[i % len(color_list)])

plt.show()