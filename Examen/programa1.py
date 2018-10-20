num1 = int(raw_input("Ingrese Primer Numero : "))
num2 = int(raw_input("Ingrese segundo Numero : "))
num3 = int(raw_input("ingrese tercer numero : "))

multi = num1 * num2

if num3 > multi:
	print "El tercer numero es mayor a la multiplicacion %s " %(multi)
if num3 == multi:
	print "El tercer numero es igual a la multiplicacion %s " %(multi)
if num3 < multi:
	print "El tercer numero es menor a la multiplicacion %s " %(multi)

if num3 > num1:
	print "El tercer numero Es mayor al primer numero %s " %(num1)
if num3 < num1:
	print "El tercer numero es Es mayor al primer numero %s " %(num1)
if num3 == num1:
	print "El tercer numero es Es igual al primer numero %s " %(num1) 
