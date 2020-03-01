from utils.types import strict_types
from empleos import Empleo
from trabajador import Trabajador

class Empresa:
    @strict_types
    def __init__(self, nombre: str, tipo: Empleo):
        self.nombre = nombre
        self.tipo = tipo
        self.empleados = []

    @strict_types
    def contratar(self, empleado: Trabajador):
        empleo_switch = {
            "PROGRAMACION": "programador",
            "DISENO": "diseñador",
            "CONSTRUCCION": "obrero"
        }
        empleo = empleo_switch.get(Empleo.tostr(self.tipo))

        if empleado.empleo != self.tipo:
            raise Exception("{} no pasó la entrevista, no es un {}".format(empleado.nombre, empleo))
        else:
            self.empleados.append(empleado)

    def trabajar_jornada(self):
        for trabajador in self.empleados:
            trabajador.trabajar()
