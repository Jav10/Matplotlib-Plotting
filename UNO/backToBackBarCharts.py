#Matplotlib Plotting
#Autor: Javier Arturo Hernández Sosa
#Fecha: 30/Sep/2017
#Descripcion: Ejecicios Matplotlib Plotting - Alexandre Devert - (18)
#Gráficas de barras espalda con espalda

import numpy as np
import matplotlib.pyplot as plt

women_pop=np.array([5., 30., 45., 22.])
men_pop=np.array([5., 25., 50., 20.])

X=np.arange(4)

plt.barh(X, women_pop, color='r')
#Hacemos negativos los valores de la población de hombres para que
#se vea el efecto
plt.barh(X, -men_pop, color='b')
plt.show()
