tiempo ={}
Salir = False
pregunta = 0
temp_max = 9999
temp_min = -9999
problluvia_max = 9999
problluvia_min = 0
while Salir == False:
    Temperatura = int(raw_input("Ingrese temperatura actual: "))
    Humedad = int(raw_input("Ingrese humedad actual: "))
    Proballuvia = int(raw_input("Ingrese probabilidad de llluvia actual: "))
    Velocidaddeviento = int(raw_input("Ingrese velocidad del viento: "))
    Direccion = raw_input("Ingrese direccion del viento: ")
    Nombre = raw_input("Ingrese Nombre del dia: ")
    Dia = int(raw_input("Ingrese el numero del dia: "))
    Hora = int(raw_input("ingrese hora actual: "))
    tiempo[Nombre]=(Temperatura,Humedad,Proballuvia,Velocidaddeviento,Direccion,Dia,Hora)
    pregunta = input("Desea salir?: escriba 1 para salir, 0 para seguir: ")
    if pregunta ==1:
        print("chau")
        Salir = True
    else:
        print("Sigamos")
        if Temperatura > temp_max:
        	temp_max = Temperatura
        else:
        	temp_min = Temperatura

        if Proballuvia > problluvia_max:
                problluvia_max = Proballuvia
        else: 
                problluvia_min = Proballuvia 


print tiempo
print("fin de ingreso de datos")

print problluvia_max
print problluvia_min

