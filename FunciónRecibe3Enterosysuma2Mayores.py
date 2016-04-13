def sumarmayor(x1,x2,x3):
	if x1>x2 and x1>x3:
		if x2>x3:
			return x1+x2
	elif x2>x1 and x2>x3:
		if x3>x1:
			return x2+x3
	else:
		return x3+x2

suma=sumarmayor(10,12,30)
print suma