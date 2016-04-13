
# Almacenar en una tupla 5 nombres. Luego generar un valor aleatorio entre 2 y 4. Copiar a una tupla
# el nombre de la posición indicada por el valor aleatorio y los nombres que se encuentran en la posición anterior y posterior.
import random

nombre=('juan','ana','luis','carlos','roman')
aleatoreo=random.randint(1,3)
tresnombres=nombre[aleatoreo-1:aleatoreo+2]
print tresnombres