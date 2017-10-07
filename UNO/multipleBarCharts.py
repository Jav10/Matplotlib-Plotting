#Matplotlib Plotting
#Autor: Javier Arturo Hernández Sosa
#Fecha: 30/Sep/2017
#Descripcion: Ejecicios Matplotlib Plotting - Alexandre Devert - (13)
#Gráfico de Barras Multiple

import matplotlib.pyplot as plt
import numpy as np

#Generamos los datos
data = [[5.,25.,50.,20,],
        [4.,23.,51.,17.],
        [6.,22.,52.,19.]]

#Se crea un vector de 0-3
X = np.arange(4)
#Creamos las gráficas de barras, y pasamos por parametros la cordenada en x de cada barra dejando un espacio
#para la siguiente, la altura de cada barra, el color y la anchura de la barra
#Si no colocamos una distancia -> X+0.25 se van a sobreponer una con otra
plt.bar(X + 0.00, data[0], color='b', width=0.25)
plt.bar(X + 0.25, data[1], color='g', width=0.25)
plt.bar(X + 0.50, data[2], color = 'r', width= 0.25)
plt.show()