#Matplotlib Plotting
#Autor: Javier Arturo Hernández Sosa
#Fecha: 30/Sep/2017
#Descripcion: Ejecicios Matplotlib Plotting - Alexandre Devert - (16)
#Gráfico de Barras Apilado

import numpy as np
import matplotlib.pyplot as plt

#Generamos los datos
A = np.array([5., 30., 45., 22.])
B = np.array([5., 25., 50., 20.])
C = np.array([1., 2., 1., 1.])
#generamos las coordenadas en X
X = np.arange(4)

#Colocamos las barras una sobre otra
plt.bar(X, A, color='b')
#Colocamos la parte inferior de la gráfica (B) en la parte superior de la Anterior (A)
plt.bar(X, B, color='g', bottom=A)
#Colocamos la parte inferior de la gráfica (C) en la parte superior de las Anteriores (A + B)
plt.bar(X, C, color='r', bottom=A + B)
plt.show()