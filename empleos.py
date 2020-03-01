from enum import IntEnum

class Empleo(IntEnum):
    PROGRAMACION = 1
    DISENO = 2
    CONSTRUCCION = 3

    @classmethod
    def names(cls):
        return [
            "PROGRAMACION",
            "DISENO",
            "CONSTRUCCION"
        ]

    @classmethod
    def tostr(cls, value):
        return cls.names()[value - cls.PROGRAMACION]

    @classmethod
    def toint(cls, s):
        return cls.names().index(s) + cls.PROGRAMACION
