def inversa(a):
	cont = 0
	cont2 = 0
	salir = False
	palabra = []
	alreves = []
	for i in a:
		palabra.append(i)
		cont = cont + 1

	cont2 = cont
	while salir == False:
		alreves.append(palabra[cont2-1])
		cont2 = cont2-1
		if cont2 == 0:
			salir = True
	return str(alreves)
	#return palabra
jerjes = "soy re gato"

print inversa(jerjes)
