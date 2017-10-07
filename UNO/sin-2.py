#Matplotlib Plotting
#Autor: Javier Arturo Hernández Sosa
#Fecha: 30/Sep/2017
#Descripcion: Ejecicios Matplotlib Plotting - Alexandre Devert - (3)

import numpy as np
import matplotlib.pyplot as plt

#Se crean 100 valores de 0 a 2PI
X = np.linspace(0,2*np.pi,100)
#Se crean 100 valores evaluando los anteriores en seno() para Y
Y = np.sin(X)
#Se grafica y se muestra
plt.plot(X, Y)
plt.show()