#Matplotlib Plotting
#Autor: Javier Arturo Hernández Sosa
#Fecha: 30/Sep/2017
#Descripcion: Ejecicios Matplotlib Plotting - Alexandre Devert - (7)

import matplotlib.pyplot as plt

#Creamos dos listas
X,Y = [],[]

#Leemos cada linea del archivo
for line in open('data1.txt','r'):
    '''
        Capturamos los valores 'x y' de cada linea
        y con la función split(str=' ') los separamos
        teniendo como delimitador el espacio y guardamos
        cada valor en su correspondiente lista.
    '''
    values = [float(s) for s in line.split()]
    X.append(values[0])
    Y.append(values[1])

'''
Algo más corto:
with open('data1.txt','r') as f:
    X,Y = zip(*[[float(s) for s in line.split()] for line in f])
    
El * dentro de zip(*) se agrega para descomprimir una lista
X,Y = zip(*)    
'''

plt.plot(X,Y)
plt.show()
