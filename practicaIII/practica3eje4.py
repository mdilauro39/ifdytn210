tiempo ={}
Salir = False
pregunta = "no"

while Salir == False:
    Temperatura = raw_input("Ingrese temperatura actual: ")
    Humedad = raw_input("Ingrese humedad actual: ")
    Proballuvia = raw_input("Ingrese probabilidad de llluvia actual: ")
    Velocidaddeviento = raw_input("Ingrese velocidad del viento: ")
    Direccion = raw_input("Ingrese direccion del viento: ")
    Nombre = raw_input("Ingrese Nombre del usuario: ")
    Dia = raw_input("Ingrese fecha de hoy: ")
    Hora = raw_input("ingrese hora actual2: ")
    tiempo[Nombre]=("Temperatura: "+ Temperatura +"Grados","humedad: "+ Humedad + "%","Probabilidad de lluvia: "+Proballuvia + "%","Velocidad del viento: "+Velocidaddeviento + "KMPH","Direccion: "+Direccion,"Dia: "+Dia,"Hora: "+Hora,)
    pregunta = str(raw_input("¿Desea salir?; escriba si para salir o cualquier tecla para sefuir: "))
    if pregunta == "si":
        print("chau")
        Salir = True
    else:
        print("Sigamos")
print tiempo
print("fin de ingreso de datos")

