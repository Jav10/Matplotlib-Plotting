#Matplotlib Plotting
#Autor: Javier Arturo Hernández Sosa
#Fecha: 30/Sep/2017
#Descripcion: Ejecicios Matplotlib Plotting - Alexandre Devert - (4)

import numpy as np
import matplotlib.pyplot as plt

'''
    Graficar el binomio x^2-2X+1
'''
X = np.linspace(-3,2,200)
Y = X ** 2 - 2 *X +1

plt.plot(X,Y)
plt.show()