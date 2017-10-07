#Matplotlib Plotting
#Autor: Javier Arturo Hernández Sosa
#Fecha: 30/Sep/2017
#Descripcion: Ejecicios Matplotlib Plotting - Alexandre Devert - (22)
#Gráfica de Caja y Bigotes Multiple

import numpy as np
import matplotlib.pyplot as plt

#Generamos una matriz de 100 elementos cada uno entre (0,1)
data = np.random.randn(100,5)
#Gráfica de Caja Multiple
plt.boxplot(data)
plt.show()