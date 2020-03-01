from utils.types import strict_types

from empleos import Empleo
from trabajador import Trabajador
from empresa import Empresa

import os

def cls():
    os.system('cls' if os.name == 'nt' else 'clear')

def tipo_empleo() -> Empleo:
    empleos = {
        1: "Programación",
        2: "Diseño",
        3: "Construcción"
    }

    for index, empleo in empleos.items():
        print("(%i) %s." % (index, empleo))

    print()

    empleo = input("Ingrese el tipo de empleo: ")

    return Empleo(int(empleo))

def crearEmpresa() -> Empresa:
    nombre = input("Ingrese el nombre: ")
    print()
    empleo = tipo_empleo()

    return Empresa(str(nombre), empleo)

def crearTrabajador() -> Trabajador:
    nombre = input("Ingrese el nombre: ")
    print()
    empleo = tipo_empleo()

    return Trabajador(str(nombre), empleo)

def ver_empresas(empresas: list, ver_empleados: bool = True):
    if len(empresas) >= 1:
        for index, empresa in enumerate(empresas):
            empleo_switch = {
                "PROGRAMACION": "Programación",
                "DISENO": "Diseño",
                "CONSTRUCCION": "Construcción"
            }
            empleo = empleo_switch.get(Empleo.tostr(empresa.tipo))
            print("(%i) %s - %s" % (index, empresa.nombre, empleo))
            print()
            if len(empresa.empleados) >= 1 and ver_empleados:
                print("\tEmpleados:")
                print()
                for index, empleado in enumerate(empresa.empleados):
                    print("\t(%i) %s" % (index, empleado.nombre))
                print()
    else:
        print("No hay empresas asociadas.")

    print()
    if ver_empleados:
        input("Presione cualquier tecla para continuar...")
    else:
        if len(empresas) < 1:
            input("Presione cualquier tecla para continuar...")

def main():
    salir = False
    empresas = []

    while not salir:
        opciones = {
            1: "Ver empresas",
            2: "Crear empresas",
            3: "Contratar empleados",
            4: "Salir"
        }

        for index, opcion in opciones.items():
            print("(%i) %s." % (index, opcion))

        print()

        opcion = int(input("¿Qué desea hacer? "))

        cls()

        if opcion == 1:
            ver_empresas(empresas)
            cls()
        if opcion == 2:
            empresas.append(crearEmpresa())
            cls()
        if opcion == 3:
            while True:
                try:
                    ver_empresas(empresas, False)
                    if len(empresas) < 1:
                        break
                    opcion_empresa = empresas[(int(input("Escoge la empresa: "))) - 1]
                    print()
                    opcion_empresa.contratar(crearTrabajador())
                    break
                except Exception as error:
                    cls()
                    print(error)
                    print()
            cls()
        elif opcion == 4:
            salir = True
        else:
            print("Opción inválida.")
            print()

if __name__ == "__main__":
    main()
