#!/usr/bin/python
# -*- coding: utf-8 -*-

#variable usada por el while, mientras sea 1 su valor, el while seguira, si es 0 el while termina.
salir=1
#diccionario donde el while almacenara los alumnos con sus respectivos datos.
alumnos={}
#alumnos con un promedio mayor que 7.
alumnosmayor7={}
#dni trozado
numerospliteado={}
#variable donde aparecen los alumnos con almenos 3 numeros impares.
dni3numerosimpares={}

#funcion que hace un promedio de las notas

def pro(a,b,c,d):
	p=(a+b+c+d)/4
	return p

#funcion que convierte int a str cualquier numero y devuelve una lista con  los numeros separados en enteros. 
def listanum(a):
        #Si llega en Int comvierto a str
        num = str(a)
        #Declaro array list_num
        list_num = []
        for n in num:
        #Convierto a int
                n = int(n)
        #Guardo n en el array
                list_num.append(n)
        return list_num



# aqui el while  se usa para armar lista de los alumnos con sus respectivos datos.
while salir==1:
	promedio=0
	nombre =""
	apellido=""
	dni=0
	ingreso=0
	notalengua=0
	notamatematica=0
	notaingles=0
	notaprogramacion=0
	nombre=(str(raw_input("Ingrese el nombre: ")))
	apellido=(str(raw_input("ingrese apellido: ")))
	dni=(int(raw_input("ingrese dni: ")))
	ingreso=int(raw_input("ingrese año de ingreso: "))
	notamatematica=(int(raw_input("ingrese nota de matematica: ")))
	notalengua=(int(raw_input("ingrese nota de lengua: ")))
	notaingles=(int(raw_input("ingrese nota de ingles: ")))
	notaprogramacion=(int(raw_input("ingrese nota de programacion I: ")))
	promedio = range(int(pro(notalengua,notamatematica,notaingles,notaprogramacion)),int(pro(notalengua,notamatematica,notaingles,notaprogramacion))+1)
	numerospliteado[nombre+" "+apellido]={'dni':listanum(dni),'ingreso':range(ingreso,ingreso+1)}
	alumnos[nombre+" "+apellido]={'nombre':nombre,'apellido':apellido,'dni':dni,'ingreso':range(ingreso,ingreso+1),'lengua':notalengua,'matematica':notamatematica,'ingles':notaingles,'programacion':notaprogramacion,'promedionotas':promedio}
	salir = int(raw_input("para terminar pulse 0, para continuar 1"))

#imprime nombre,apellido y el promedio total de cada alumno. ademas llena el diccionario alumnosmayor7 con los estudiantes que tengan una nota mayor a 7.
for k in alumnos:
	for i in alumnos[k]['promedionotas']:
		print "el promedio total de todas las materias aprobadas de %s es de %s puntos"%(k,i)
		if i > 7:
			alumnosmayor7[k] = i
			print"el alumno %s tiene un promedio mayor a 7"%(k)

#recorre el diccionario numerospliteado para analizar cada numero que componen el dni en busca de impares
for estudiante in numerospliteado:
	n=0
	for impar in numerospliteado[estudiante]['dni']:
		if impar%2 != 0:
			n=n+1
#for que recorre el año de ingreso del alumno que va desde el año 2008 a 2010 y  si tiene al menos 3 numeros impares en su dni .
	for ingreso in numerospliteado[estudiante]['ingreso']:
		if n >=3:
			if ingreso in range(2007,2011):
				print"el alumno %s tiene al menos 3 numeros impares en su dni e ingreso en el anio %s"%(estudiante,ingreso)
