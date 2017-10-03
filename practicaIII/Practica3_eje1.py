palabra1 = raw_input("Ingrese la primer palabra:")
palabra2 = raw_input("ingrese la segunda palabra:")

if palabra1[-3:-1] == palabra2[-3:-1]:
	print "rima mucho"
elif palabra1[-2:-1] == palabra2[-2:-1]:
	print "rima poco"
else:
	print "No rima papu"


