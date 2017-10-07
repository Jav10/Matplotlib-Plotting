#Matplotlib Plotting
#Autor: Javier Arturo Hernández Sosa
#Fecha: 30/Sep/2017
#Descripcion: Ejecicios Matplotlib Plotting - Alexandre Devert - (17)
#Gráfico de Barras Apilado
import numpy as np
import matplotlib.pyplot as plt

data = np.array([[5., 30., 45., 22.],
                 [5., 25., 50., 20.],
                 [1., 2., 1., 1.]])

color_list=['b', 'g', 'r']
#La función .shape() regresa las filas y las columnas
#  .shape[0] número de filas .shape[1] número de columnas
X=np.arange(data.shape[1]) #Esto es igual a X=np.arange(4)

for i in range(data.shape[0]): #Esto es igual a range(3)
    plt.bar(X, data[i],
            # np.sum() suma los arrays dados en el eje x-> axis=0 (filas), eje y ->y axis=1 (columnas)
            bottom=np.sum(data[:i], axis=0),
            color=color_list[i%len(color_list)])


plt.show()