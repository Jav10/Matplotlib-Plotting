#Matplotlib Plotting
#Autor: Javier Arturo Hernández Sosa
#Fecha: 30/Sep/2017
#Descripcion: Ejecicios Matplotlib Plotting - Alexandre Devert - (15)
#Gráficas Apiladas

import matplotlib.pyplot as plt

A = [5., 30., 45., 22.]
B = [5., 25., 50., 20.]

X = range(4)

plt.bar(X, A, color='b')
#Colocamos la parte inferior de la gráfica (B) en la parte superior de la Anterior (A)
plt.bar(X, B, color='r', bottom=A)
plt.show()