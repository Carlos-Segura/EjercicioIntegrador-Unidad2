import csv

class Alumno():
    def __init__(self, dni, apellido, nombre, carrera, anioCursado):
        self.__dni = dni
        self.__apellido = apellido.title()
        self.__nombre = nombre.title()
        self.__carrera = carrera
        self.__anioCursado = anioCursado
        
    def getNombre(self):
        return self.__nombre
    
    def getApellido(self):
        return self.__apellido
    
    def getApellidoNombre(self):
        return self.getApellido() + ' ' + self.getNombre()
    
    def getDocumento(self):
        return self.__dni
    
    def getCarrera(self):
        return self.__carrera
    
    def getAnioCursado(self):
        return self.__anioCursado
    
    def __str__(self):
        return str(self.__anioCursado) + " " + self.getApellidoNombre() + " " + self.__dni + " " + self.__carrera 
    
    def __lt__(self, otro):
        return self.getAnioCursado() < otro.getAnioCursado() or self.getApellidoNombre() < otro.getApellidoNombre()
    
    def abrirArchivo(alumnos):
            archivo = open('alumnos.csv','r')
            reader = csv.reader(archivo, delimiter = ';')
            reader.__next__()                                      #Salta la primera linea // Cabecera
            for alu in reader:
                instancia = Alumno(alu[0], alu[1], alu[2], alu[3], alu[4].strip())
                alumnos.append(instancia)
            archivo.close()
            return alumnos