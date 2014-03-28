#Tarea 2 - para el martes 2 de abril
#------------------------------------

# Completar este programa para determinar las fuerzas y reacciones en un
# reticulado segun lo visto en clases. La tarea sera evaluada con un
# reticulado arbitrario.

from Truss import * # Importa el modulo con las funciones
filename='truss.in'; #nombre del archivo con la informacion del reticulado

tr=Truss(filename); # Se genera un objeto Truss, que tiene los sgtes atributos:
#tr.nodes [nro de nodos,2]: tiene la posicion X,Y de cada nodo en el mismo
#orden en que fueron especificados en el archivo.
#tr.bars [nro de barras,2]: contiene el numero de cada nodo que esta
#presente en la barra
#tr.reac [nro de reacciones, 3]: en la primera columna tiene los nodos en los
#que esta aplicada la reaccion. La 2da y 3ra corresponden a un vector
#unitario especificando la direccion de la reaccion.
#tr.force [nro de fuerzas,3]: en la primera columna tiene los nodos en los
#que esta aplicada la fuerza. La 2da y 3ra corresponden a un vector
#especificando la fuerza.

# Funciones:
tr.plot() # dibuja el reticulado. En negro se grafican las restricciones
# en rojo las fuerzas. Los vectores estan dibujados de manera que siempre
# apuntan al nodo.
#X(i,j) retorna el coeficiente X. Existe tambien Y(i,j)


A=np.zeros((len(tr.bars)+len(tr.reac),len(tr.bars)+len(tr.reac)))
f=np.zeros(len(tr.bars)+len(tr.reac))

nb=len(tr.bars)

# Aqu? va su desarrollo.

for k in range(nb):
	i=tr.bars[k,0]
	j=tr.bars[k,1]
	A[2*i,k]=tr.X(j,i)
	A[2*i+1,k]=tr.Y(j,i)
	A[2*j,k]=tr.X(i,j)
	A[2*j+1,k]=tr.Y(i,j)

for k in range(len(tr.reac)):
	node=tr.reac[k,0]
	A[2*node,nb+k]=tr.reac[k,1]
	A[2*node+1,nb+k]=tr.reac[k,2]

for k in range(len(tr.force)):
	node=tr.force[k,0]
	f[2*node]=-tr.force[k,1]
	f[2*node+1]=-tr.force[k,2]



# Una vez que lo tengan listo pueden descomentar las siguientes lineas.
    
F=np.linalg.solve(A,f) # para resolver. Llamar F al vector que contiene las fuerzas

tr.write_results(F,'output.txt') # Escribe los resultados a un
# archivo llamado output.txt
