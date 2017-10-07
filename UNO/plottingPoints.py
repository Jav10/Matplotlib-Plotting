#Matplotlib Plotting
#Autor: Javier Arturo Hernández Sosa
#Fecha: 30/Sep/2017
#Descripcion: Ejecicios Matplotlib Plotting - Alexandre Devert - (10)
#Grágica de dispersión

import numpy as np
import matplotlib.pyplot as plt

#Generamos dos vectores con 1024 números aleatorios entre 0-1
data = np.random.rand(1024,2)

#Generamos una gráfica de disperción
plt.scatter(data[:,0],data[:,1])
plt.show()