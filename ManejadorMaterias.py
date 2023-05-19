import csv
from ClaseMateriasAprobadas import Materia_Aprobada

class ManejadorMa():
    def __init__(self):
        self.__materiasAprobadas = []
        
    def cargarListaDesdeArchivo(self):
        archivo = open('materiasAprobadas.csv','r')
        reader = csv.reader(archivo, delimiter = ';')
        reader.__next__()
        for fila in reader:
            ma = Materia_Aprobada(fila[0], fila[1], fila[2], float(fila[3]), fila[4])
            self.__materiasAprobadas.append(ma)
        archivo.close()
    
    def menu(self):
        print("1- Informar promedio")
        print("2- Informar alumnos promocionales")
        print("3- Ver listado")
        print("0- Salir")
        
    def getPromedioAlumno(self, documento):
        acumNotas = 0
        contador = 0
        for materia in self.__materiasAprobadas:
            if materia.getDNI() == documento:
                contador += 1
                acumNotas += materia.getNota()
        promedio = 0
        if contador != 0:
            promedio = acumNotas / contador
        return promedio
    
    def listarAlumnosQueCumplen(self, nombreMateria):
        AlumnosQueCumplen = []
        for materia in self.__materiasAprobadas:
            if materia.getNombreMateria() == nombreMateria:
                if materia.getNota() >= 7 and materia.getAprobacion() == 'P':
                    AlumnosQueCumplen.append(materia)
        return AlumnosQueCumplen