#Matplotlib Plotting
#Autor: Javier Arturo Hernández Sosa
#Fecha: 30/Sep/2017
#Descripcion: Ejecicios Matplotlib Plotting - Alexandre Devert - (21)
#Gráfica de Caja y Bigotes

import numpy as np
import matplotlib.pyplot as plt

#Generamos un vector con cien elementos aleatorios entre (0,1)
data = np.random.randn(100)

#diagrama de caja
plt.boxplot(data)
plt.show()