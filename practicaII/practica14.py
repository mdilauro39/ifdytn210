#!/usr/bin/python
Numeros = []
numero_max_min = []
med = 0
#Se crea 2 listas para que se alojen los 3 numeros
a = int(raw_input("ingrese primer numero:"))
b = int(raw_input("Ingrese segundo lado:"))
c = int(raw_input("ingrese tercer lado:"))
#se pide al usuario que ingrese 3 numeros y esos se alojan en 3 variabes a,b,c
Numeros.append(a)
Numeros.append(b)
Numeros.append(c)
#el contenido de las variables a , b , c , se ingresan en  la lista Numeros
max = max(Numeros)
min = min(Numeros)

#aqui se extrae de la lista el numero maximo y minimo,
# luego se ponen los mismo en 2 variables.
numero_max_min.append(max)
numero_max_min.append(min)
#se indexa las variables max y min en la lista numero_max_min . 
conj1= set(Numeros)
conj2= set(numero_max_min)
#se configura los 2 conjuntos para restarlos y asi descubrir el numero del medio. 

if med == 0:
	med = min
print med

if ((med + min) > max) or ((med + min) == max):
	print "si se pued armar un triangulo"
else:
	print "no se puede armar un triangulo"







