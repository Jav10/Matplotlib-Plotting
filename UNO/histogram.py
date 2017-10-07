#Matplotlib Plotting
#Autor: Javier Arturo Hernández Sosa
#Fecha: 30/Sep/2017
#Descripcion: Ejecicios Matplotlib Plotting - Alexandre Devert - (20)
#Histograma

import matplotlib.pyplot as plt
import numpy as np

#Generamos un vector con mil elementos aleatorios entre (0,1)
X = np.random.randn(1000)

#Partimos el histograma en 20 partes
plt.hist(X, bins=20)
plt.show()
