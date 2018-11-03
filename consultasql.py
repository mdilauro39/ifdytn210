
import MySQLdb

db = MySQLdb.connect(host="localhost", user="marcos",passwd="root210", db="movedb")

cursor = db.cursor(MySQLdb.cursors.DictCursor)

cursor.execute("SELECT * FROM Clientes")

resultado = cursor.fetchall()

for row in resultado:

	print (row["Fax"])


