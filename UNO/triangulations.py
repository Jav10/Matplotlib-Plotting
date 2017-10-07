#Matplotlib Plotting
#Autor: Javier Arturo Hernández Sosa
#Fecha: 30/Sep/2017
#Descripcion: Ejecicios Matplotlib Plotting - Alexandre Devert - (23)
#Redes de Triangulaciones se usa en geodesia y topología

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.tri as tri

data = np.random.rand(100,2)

triangles = tri.Triangulation(data[:,0], data[:,1])

plt.triplot(triangles)
plt.show()