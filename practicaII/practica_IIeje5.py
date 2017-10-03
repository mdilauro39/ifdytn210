ano = int(raw_input("Ingrese el ano"))

if ano%4 == 0 and ano%100 != 0 or ano%400 == 0:
	print("bisiesto")
else:
	print("no bisiesto")


