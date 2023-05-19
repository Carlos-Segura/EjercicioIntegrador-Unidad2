import numpy as np
import csv
from ClaseAlumnos import Alumno


class ManejadorAl():
    def __init__(self):
        self.__alumnos = 0
    
    def abrirArchivo(self):
        contador = 0
        archivo = open('alumnos.csv','r')
        reader = csv.reader(archivo, delimiter = ';')
        reader.__next__()                                      #Salta la primera linea // Cabecera
        for alu in reader:
            contador += 1
        self.__alumnos = np.empty(contador, dtype=ManejadorAl)
        archivo.seek(0)
        reader.__next__()
        indice = 0
        for alu in reader:
            instanciaAlumno = Alumno(alu[0], alu[1], alu[2], alu[3], alu[4])
            self.__alumnos[indice] = instanciaAlumno
            indice += 1
        archivo.close()
        
    def __gt__(self, otro):
        bandera = False
        if self.__alumnos.getApellidoNombre() > otro.getApellidoNombre():
            if self.__alumnos.getDocumento() > otro.getDocumento():
                bandera = True
        return bandera
                
        
    def encuentraAlumnoDeEsaMateria(self, listaAlumnosQueCumplen):
        i = 0
        N = len(listaAlumnosQueCumplen)
        while N != 0:
            alu = self.__alumnos[i]
            j = 0
            while j < N and listaAlumnosQueCumplen[j].getDNI() != alu.getDocumento():
                j += 1
            if j < N:
                print("***DATOS***")
                print ("{:^15}".format(alu.getDocumento()), format(alu.getApellidoNombre()), format(listaAlumnosQueCumplen[j].getFecha()), format(listaAlumnosQueCumplen[j].getNota()), format(alu.getAnioCursado()))
                listaAlumnosQueCumplen.pop(j)
                N -= 1
            i += 1
            
    def listadoDeAlumnos(self):
        longitud = len(self.__alumnos)
        cont = 0
        ordenado = False
        for _ in range(0, longitud):
            if ordenado == True:
                break
            for j in range(0, longitud-1):
                ordenado = True
                cont += 1
                if self.__alumnos[j] > self.__alumnos[j+1]:
                    ordenado = False
                    aux = self.__alumnos[j]
                    self.__alumnos[j] = self.__alumnos[j+1]
                    self.__alumnos[j+1] = aux
            longitud -= 1
        for indice in range(len(self.__alumnos)):
            print(self.__alumnos[indice])