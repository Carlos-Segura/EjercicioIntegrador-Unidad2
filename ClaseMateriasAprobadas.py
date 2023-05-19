class Materia_Aprobada():
    
    def __init__(self, dni, nombreMateria, fecha, nota, aprobación):
        self.__dni = dni
        self.__nombreMateria = nombreMateria
        self.__fecha = fecha
        self.__nota = nota
        self.__aprobacion = aprobación
        
    def getDNI(self):
        return self.__dni
    
    def getNombreMateria(self):
        return self.__nombreMateria
    
    def getFecha(self):
        return self.__fecha
    
    def getNota(self):
        return self.__nota
    
    def getAprobacion(self):
        return self.__aprobacion