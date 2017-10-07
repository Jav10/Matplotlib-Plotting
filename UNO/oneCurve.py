#Matplotlib Plotting
#Autor: Javier Arturo Hernández Sosa
#Fecha: 30/Sep/2017
#Descripcion: Ejecicios Matplotlib Plotting - Alexandre Devert - (1)

import matplotlib.pyplot as plt

#Se generan los valores para X y Y
X = range(100)
Y = [value ** 2 for value in X]

#Se crea el gráfico
plt.plot(X,Y)
#Muestra el gráfico
plt.show()
