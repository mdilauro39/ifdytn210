# -*- coding: utf-8 *-*
from persona import Persona
from persona_view import PersonaView


class PaisController:

    def __init__(self):
        self.vista = PersonaView()
        self.persona_controller()

    def persona_controller(self):
        """Controlador general de País"""
        peticion = self.vista.mostrar_menu()
        self.peticion = int(peticion)

        if self.peticion == 1:
            self.crear_persona_controller()
        elif self.peticion == 2:
            self.listar_persona_controller()
        elif self.peticion == 3:
            self.editar_persona_controller()
        elif self.peticion == 4:
            self.eliminar_persona_controller()

    def crear_persona_controller(self):
        """Controlador para creación de nuevo país"""
        (persona_id_per, persona_nombre) = self.vista.crear_persona()
        persona = Persona()
        persona.persona = persona_id_per
        persona.nombre = persona_nombre
        persona.create()
        self.vista.confirmar_creacion()
        self.persona_controller()

    def traer_paises(self):
        """Trae una lista de todos los países"""
        pais = Pais()
        listado = pais.read_all()
        return listado

    def listar_paises_controller(self):
        """Controlador del listado de países"""
        listado = self.traer_paises()
        self.vista.listar_paises(listado)
        self.pais_controller()

    def editar_pais_controller(self):
        """Controlador para editar un país"""
        listado = self.traer_paises()
        (id, nombre, abbr) = self.vista.editar_pais(listado)
        pais = Pais()
        pais.id = int(id)
        pais.pais = nombre
        pais.abbr = abbr
        pais.update()
        self.vista.confirmar_editar_pais()
        self.pais_controller()

    def eliminar_pais_controller(self):
        """Controlador para eliminar un país"""
        listado = self.traer_paises()
        id = self.vista.eliminar_pais(listado)
        id = int(id)
        pais = Pais()
        pais.id = id
        pais.delete()
        self.vista.confirmar_eliminar_pais()
        self.pais_controller()


controller = PaisController()
