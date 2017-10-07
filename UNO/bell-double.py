#Matplotlib Plotting
#Autor: Javier Arturo Hernández Sosa
#Fecha: 30/Sep/2017
#Descripcion: Ejecicios Matplotlib Plotting - Alexandre Devert - (6)

import numpy as np
import matplotlib.pyplot as plt

def plot_slope(x,y):
    #Modificamos la campana
    Xs = X[1:] - X[:-1]
    Ys = Y[1:] - Y[:-1]
    plt.plot(X[1:], Ys/Xs)

#Campana exponencial 1/e^(x^2)
X = np.linspace(-3,3,100)
Y = np.exp(-X ** 2)
plt.plot(X, Y)
plot_slope(X,Y)

#Mostramos las dos gráficas
plt.show()