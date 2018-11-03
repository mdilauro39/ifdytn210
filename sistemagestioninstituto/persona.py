# -*- coding: utf-8 *-*
from db_conn import DBConn


class Persona:

    def __init__(self):
        self.db = DBConn()
	self.idpersona = ''
        self.nombre = ''
        self.apellido = ''
	self.dni = ''
	self.fecha_nacimiento = ''
	self.tel = ''
	self.cel = ''
	self.sexo = ''
	self.mail= ''
	self.cod_per = ''
	self.ingreso= ''
	self.id_mate = ''
	self.id_tit = ''
	self.id_dom = ''
	self.id_carre= ''
	self.cod_dis = ''
	self.cod_afi = ''
	self.observaciones = ''
    def create(self):
        """Crear un nuevo registro"""
        query = "INSERT INTO persona (idpersona , nombre , apellido , dni , fecha_nacimiento , tel, cel , sexo , mail , cod_per , ingreso , id_mate , id_tit , id_dom , id_carre , cod_dis , cod_afi , observaciones) VALUES (null , %s , %s , %d , %s , %d , %d , %s, %s, %s, %s, %d, %d, %d , %d, %s, %s, %s)"
        values = (self.idpersona , self.nombre , self.apellido)
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
