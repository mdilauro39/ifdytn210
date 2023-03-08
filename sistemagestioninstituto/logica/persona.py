# -*- coding: utf-8 *-*
from db_conn import DBConn


class Persona:

    def __init__(self):
        self.idpersona =''
        self.nombre = ''
        self.apellido = ''
        self.dni = 0
        self.fecha_nacimiento = ''
        self.db = DBConn()

    def create(self):
        """Crear un nuevo registro"""
        query = "INSERT INTO persona (idpersona, nombre, apellido, dni) VALUES (null, %s, %s, %s)"
        values = (self.nombre, self.apellido, self.dni)
        self.db.ejecutar(query, values)

    def update(self):
        """Actualizar un registro existente"""
        query = "UPDATE persona SET nombre = %s, apellido = %s, dni = %s WHERE idpersona = %s"
        values = (self.nombre, self.apellido, self.dni, self.idpersona)
        return self.db.ejecutar(query, values)

    def read_all(self):
        """Leer todos los registros"""
        query = "SELECT idpersona, nombre , apellido , dni FROM persona"
        return self.db.ejecutar(query)

    def read(self):
        query = "SELECT idpersona, nombre, apellido, dni FROM persona WHERE idpersona = %s"
        values = (self.idpersona)
        return self.db.ejecutar(query, values)
    
    def delete_roto(self):
        """Elimina uno o todos los registros"""
        query = "DELETE FROM persona WHERE idpersona = %d"
        values = int(self.idpersona)
        return self.db.ejecutar(query, values)
    
    def delete(self):
        """Elimina uno o todos los registros"""
        query = 'DELETE FROM persona WHERE idpersona = ' + str(self.idpersona)
        #values = self.idpersona
        #return self.db.ejecutar(query, values)
        return self.db.ejecutar(query)