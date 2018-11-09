# -*- coding: utf-8 *-*
from db_conn import DBConn


class Pais:

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
