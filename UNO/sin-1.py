#Matplotlib Plotting
#Autor: Javier Arturo Hernández Sosa
#Fecha: 30/Sep/2017
#Descripcion: Ejecicios Matplotlib Plotting - Alexandre Devert - (2)

#Se importan las librerias necesarias
import matplotlib.pyplot as plt
import math

#Se generan 100 muestras
T = range(100)
#Se parte el eje X en 100 partes usando Radianes
X = [(2*math.pi*t)/len(T) for t in T]
#Se crean los valores de Y apartir de los de X -> Y = sin(X)
Y = [math.sin(value) for value in X]

#Se grafican
plt.plot(X,Y)
plt.show()