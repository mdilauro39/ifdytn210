n1= int(raw_input("ingrese primer numero"))
n2= int(raw_input("ingrese segundo numero"))
n3= int(raw_input("ingrese tercer numero"))
def numgrande(a,b,c):
	if a > b:
		return a
	if b > a:
		return b
	if a > c:
		return a
	if c > a:
		return c
	if c > b:
		return c
	if b > c:
		return b
	if a==b:
		return a,b
	if a==c:
		return a,c
	if c==b:
		return c,b


print numgrande(n1,n2,n3)
