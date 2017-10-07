#Matplotlib Plotting
#Autor: Javier Arturo Hernández Sosa
#Fecha: 30/Sep/2017
#Descripcion: Ejecicios Matplotlib Plotting - Alexandre Devert - (5)

import numpy as np
import matplotlib.pyplot as plt

X = np.linspace(0,2*np.pi,100)
Ys = np.sin(X)
Yc = np.cos(X)

plt.plot(X, Ys)
plt.plot(X,Yc)
plt.show()