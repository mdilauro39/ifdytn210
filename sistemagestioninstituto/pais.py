# -*- coding: utf-8 *-*
from db_conn import DBConn


class Pais:

    def __init__(self):
        self.id_per = 0
        self.nombre = ''
        self.apellido = ''
        self.db = DBConn()
	self.fecha_nac = ''
	self.dni = ''
	self.sexo = ''
	self.nacionalidad = ''
	self.telefono = ''
	self.celular = ''
	self.mail = ''
	self.cod_per = ''
	self.ingreso = ''
	self.id_mate = ''
	self.cod_afi = ''
	self.cod_dis = ''
    def create(self):
        """Crear un nuevo registro"""
        query = "INSERT INTO persona(nombre , apellido) VALUES (null, %s, %s)"
	values = (self.nombre , self.apellido)
	self.db.ejecutar(query, values)

    def update(self):
        """Actualizar un registro existente"""
        query = "UPDATE paises SET pais = %s, abbr = %s WHERE id = %s"
        values = (self.pais, self.abbr, self.id)
        return self.db.ejecutar(query, values)

    def read_all(self):
        """Leer todos los registros"""
        query = "SELECT id, pais, abbr FROM paises"
        return self.db.ejecutar(query)

    def read(self):
        query = "SELECT id, pais, abbr FROM paises WHERE id = %d"
        values = (self.id)
        return self.db.ejecutar(query, values)

    def delete(self):
        """Elimina uno o todos los registros"""
        query = "DELETE FROM paises WHERE id = %s"
        values = self.id
        return self.db.ejecutar(query, values)
