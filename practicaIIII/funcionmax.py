n1= int(raw_input("ingrese primer numero"))
n2= int(raw_input("ingrese segundo numero"))

def numgrande(a,b):
	if a > b:
		return a
	if b > a:
		return b
	if a == b:
		return "a y b iguales"

print numgrande(n1,n2,n3)
