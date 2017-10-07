#Matplotlib Plotting
#Autor: Javier Arturo Hernández Sosa
#Fecha: 30/Sep/2017
#Descripcion: Ejecicios Matplotlib Plotting - Alexandre Devert - (12)
#Gráficas de Barras Horizontales

import matplotlib.pyplot as plt
#Barra Horizontal
#Generamos los datos
data = [5.,25.,50.,20,]
#Creamos la gráfica de barras, y pasamos por parametros la cordenada en x de cada barra
#,la anchura de cada barra y la altura de la barra
plt.barh(range(len(data)), data, height=0.5)
plt.show()