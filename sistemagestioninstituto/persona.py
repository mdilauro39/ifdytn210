# -*- coding: utf-8 *-*
from db_conn import DBConn


class Persona:

    def __init__(self):
        self.idpersona = 0
        self.nombre = ''
        self.apellido = ''
        self.db = DBConn()

    def create(self):
        """Crear un nuevo registro"""
        query = "INSERT INTO persona (idpersona, nombre, apellido) VALUES (null, %s, %s)"
        values = (self.nombre, self.apellido)
        self.db.ejecutar(query, values)

    def update(self):
        """Actualizar un registro existente"""
        query = "UPDATE persona SET nombre = %s, apellido = %s WHERE idpersona = %s"
        values = (self.nombre, self.apellido, self.idpersona)
        return self.db.ejecutar(query, values)

    def read_all(self):
        """Leer todos los registros"""
        query = "SELECT idpersona, nombre, apellido FROM persona"
        return self.db.ejecutar(query)

    def read(self):
        query = "SELECT idpersona, nombre, apellido FROM persona WHERE idpersona = %d"
        values = (self.idpersona)
        return self.db.ejecutar(query, values)

    def delete(self):
        """Elimina uno o todos los registros"""
        query = "DELETE FROM persona WHERE idpersona = %s"
        values = self.idpersona
        return self.db.ejecutar(query, values)
