dict ={}
Salir = False
pregunta = 0
dias = {} 
while Salir == False:
    Temperatura = int(raw_input("Ingrese temperatura actual: "))
    Humedad = int(raw_input("Ingrese humedad actual: "))
    Proballuvia = int(raw_input("Ingrese probabilidad de llluvia actual: "))
    Velocidaddeviento = int(raw_input("Ingrese velocidad del viento: "))
    Direccion = raw_input("Ingrese direccion del viento: ")
    Nombre = raw_input("Ingrese Nombre del dia: ")
    Dia = int(raw_input("Ingrese el numero del dia: "))
    Hora = int(raw_input("ingrese hora actual: "))
    dict[Nombre]={"Temperatura":Temperatura,"Humedad":Humedad,"Probabilidad de lluvia":Proballuvia,"Velocidad del viento":Velocidaddeviento,"Direccion del viento":Direccion,"Dia":Dia,"Hora":Hora}
    pregunta = input("Desea salir?: escriba 1 para salir, 0 para seguir: ")
    if pregunta ==1:
        print("chau")
        Salir = True
    else:
        print("Sigamos")
print("fin de ingreso de datos")

dias = tiempo.keys()
datos = tiempo.values()
print dias
print datos





