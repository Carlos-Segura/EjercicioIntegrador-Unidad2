from ManejadorAlumnos import ManejadorAl
from ManejadorMaterias import ManejadorMa
from os import system

if __name__ == '__main__':
    manejadorM = ManejadorMa()
    manejadorA = ManejadorAl()
    manejadorM.cargarListaDesdeArchivo()
    manejadorA.abrirArchivo()
    print("\t***MENU DE OPCIONES***")
    manejadorM.menu()
    opcion = int(input('\nOpcion => '))
    system("cls")
    while opcion != 0:
        match opcion:
            case 1:
                documento = input('Ingrese un DNI: ')
                Promedio = manejadorM.getPromedioAlumno(documento)
                if Promedio == 0:
                    print("Alumno NO existe.")
                else:
                    print("El promedio del alumno con DNI: ", documento, " es: ", Promedio)
            case 2:
                nombreMateria = input('Ingrese el nombre de una materia: ')
                listaAlumnosQueCumplen = manejadorM.listarAlumnosQueCumplen(nombreMateria)
                if len(listaAlumnosQueCumplen) != 0:
                    manejadorA.encuentraAlumnoDeEsaMateria(listaAlumnosQueCumplen)
                else:
                    print("No hay alumnos con los datos de la materia", nombreMateria)

            case 3:
                print("\t***LISTA ALUMNOS ORDENADA***")
                manejadorA.listadoDeAlumnos()
            case _:
                print("***COMPLETAR***")
        print("\n-------------------------------------------------------------")
        print("\t\n***MENU DE OPCIONES***\n")
        manejadorM.menu()
        opcion = int(input('\nOpcion => '))
        system("cls")