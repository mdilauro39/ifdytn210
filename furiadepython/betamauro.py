#!/usr/bin/python

#datos personales:

nom_1=raw_input("ingrese nombre: ")

ape_1=raw_input("ingrese apellido: ")

dni_1= int(input("ingrese documento: "))

fecha_1=int(input ("fecha de ingreso: "))

nom_2= raw_input("ingrese nombre: ")

ape_2= raw_input("ingrese apellido: ")

dni_2= int(input("ingrese documento: "))

fecha_2=int(input ("fecha de ingreso: "))

nom_3= raw_input("ingrese nombre: ")

ape_3= raw_input("ingrese apellido: ")

dni_3= int(input("ingrese documento: "))

fecha_3=int(input ("fecha de ingreso: "))

per_1={"nombre" : nom_1, "apellido" : ape_1, "documento" : dni_1, "fecha de ingreso" : fecha_1}

per_2={"nombre" : nom_2, "apellido" : ape_2, "documento" : dni_2, "fecha de ingreso" : fecha_2}

per_3={"nombre" : nom_3, "apellido" : ape_3, "documento" : dni_3, "fecha de ingreso" : fecha_3}

alumnos=[per_1, per_2, per_3]

#datos de materias

mate_1 = raw_input("ingrese materia: ")

nota_1 = input("ingrese nota: ")

nota_2 = input("ingrese nota: ")

nota_3 = input("ingrese nota: ")

mate_2 = raw_input("ingrese materia: ")

nota_4 = input("ingrese nota: ")

nota_5 = input("ingrese nota: ")

nota_6 = input("ingrese nota: ")

mate_3 = raw_input("ingrese materia: ")

nota_7 = input("ingrese nota: ")

nota_8 = input("ingrese nota: ")

nota_9 = input("ingrese nota: ")

mate_4 = raw_input("ingrese materia: ")

nota_10 = input("ingrese nota: ")

nota_11 = input("ingrese nota: ")

nota_12 = input("ingrese nota: ")

mate_5 = raw_input("ingrese materia: ")

nota_13 = input("ingrese nota: ")

nota_14  = input("ingrese nota: ")

nota_15 = input("ingrese nota: ")

mater_1={"materia" : mate_1, "aprobado" : "aprobado", "nota" : nota_1,"materia1" : mate_1, "aprobado1" : "aprobado", "nota1" : nota_2,"materia2" : mate_1, "aprobado2" : "aprobado", "nota2" : nota_3}

mater_2={"materia" : mate_2, "aprobado" : "aprobado", "nota" : nota_4,"materia1" : mate_2, "aprobado1" : "aprobado", "nota1" : nota_5,"materia2" : mate_2, "aprobado2" : "aprobado", "nota2" : nota_6}

mater_3={"materia" : mate_3, "aprobado" : "aprobado", "nota" : nota_7,"materia1" : mate_3, "aprobado1" : "aprobado", "nota1" : nota_8,"materia2" : mate_3, "aprobado2" : "aprobado", "nota2" : nota_9}

mater_4={"materia" : mate_4, "aprobado" : "aprobado", "nota" : nota_10,"materia1" : mate_4, "aprobado1" : "aprobado", "nota1" : nota_11,"materia2" : mate_4, "aprobado2" : "aprobado", "nota2" : nota_12}

mater_5={"materia" : mate_5, "aprobado" : "aprobado", "nota" : nota_13,"materia1" : mate_5, "aprobado1" : "aprobado", "nota1" : nota_14,"materia2" : mate_5, "aprobado2" : "aprobado", "nota2" : nota_15}

materias=[mater_1, mater_2, mater_3, mater_4, mater_5]

print alumnos

print materias 

def prom(materias, alumno):

    alumno = raw_input("ingrese nombre: ")
      
    if alumnos == nom_1 and ((nota_1 > 4) and (nota_4 > 4) and (nota_7 > 4) and (nota_10 >4) and(nota_>13)):

           promedio = (nota_1 + nota_4 + nota_7 + nota_10 + nota_13) / 5

           return prom
