#Matplotlib Plotting
#Autor: Javier Arturo Hernández Sosa
#Fecha: 30/Sep/2017
#Descripcion: Ejecicios Matplotlib Plotting - Alexandre Devert - (11)
#Gráfica de Barras

import matplotlib.pyplot as plt
#Generamos los datos
data = [5.,25.,50.,20,]
#Creamos la gráfica de barras, y pasamos por parametros la cordenada en x de cada barra
#,la altura de cada barra y la anchura de la barra
plt.bar(range(len(data)),data,width=0.5)
plt.show()