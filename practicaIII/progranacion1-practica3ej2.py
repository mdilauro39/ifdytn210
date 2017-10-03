cuenta ={}
nombre = raw_input("Ingrese Nombre =")
apellido = raw_input("Ingrese Apellido =")
edad = int(raw_input("Ingrese Edad ="))
dni = int(raw_input("Ingrese D.N.I ="))
clave = dni * (len(nombre)+len(apellido))
cuenta['Nombre'] = nombre
cuenta['Apellido'] = apellido
cuenta['Edad'] = edad
cuenta['DNI'] = dni
cuenta['Clave'] = clave
print cuenta


