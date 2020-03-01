from utils.types import strict_types
from empleos import Empleo

class Trabajador:
    @strict_types
    def __init__(self, nombre: str, empleo: Empleo):
        self.nombre = nombre
        self.empleo = empleo

    def trabajar(self):
        empleo_switch = {
            "PROGRAMACION": "programando",
            "DISENO": "diseñando",
            "CONSTRUCCION": "construyendo"
        }

        empleo = empleo_switch.get(Empleo.tostr(self.empleo))

        print("%s está %s." % (self.nombre, empleo))
