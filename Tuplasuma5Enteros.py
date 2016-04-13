enteros=(5,8,9,25,105)
contador=0
acumulador=0
while contador<=len(enteros)-1:
	acumulador=enteros[contador]+acumulador
	contador=contador+1
print acumulador