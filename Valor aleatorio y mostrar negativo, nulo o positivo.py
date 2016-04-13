# Generar un valor aleatorio entre -10 y 10. Mostrar un mensaje si el valor generado es negativo, nulo o positivo.
 

import random

valor1=random.randint(-10,10)
print valor1
print '<br>'
if valor1<0:
    print 'El número es negativo'
else:
    if valor1==None:
        print 'El valor es nulo'
    else:
        print 'El número es positivo'

       