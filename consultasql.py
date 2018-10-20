# -*- coding: utf-8 -*-
import MySQLdb 

db = MySQLdb.connect(host="localhost", user="marcos", passwd="root210", db="movedb")

cursor = db.cursor()


class Registro:
	def __init__(self,c):
		#p = "SELECT Dirección,Ciudad,CódPostal from Clientes where CódPostal = 3012"
		self.c=c
	def imprimiruno(self):

		print (self.c.fetchone())
	def imprimirtodo(self):
		print (self.c.fetchall())
	def para(self):
		p = "SELECT Dirección,Ciudad,CódPostal from Clientes \
		where CódPostal = 3012"
		self.c.execute(p)
		#print(self.c.execute("SELECT * FROM Clientes"))
		#self.c.execute("SELECT COUNT(NombreCompañía) AS 'cantidad de compañías', País FROM Clientes WHERE País = 'Francia';")
		#self.c.execute"(SELECT Dirección,Ciudad,CódPostal from Clientes where CódPostal = 3012)"

prueba = Registro(cursor)

prueba.para()
