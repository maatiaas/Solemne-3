from persona import Persona

class Docente(Persona):

    def __init__(self, nombre, edad, sueldo, grado, jornada):
        super().__init__(nombre, edad, sueldo)
        self.__grado = grado
        self.__jornada = jornada

    def __str__(self):
        return super().__str__()+", Grado: {} , Jornada: {}".format(self.__grado,self.__jornada)
    
    def GetGrado(self):
        return self.__grado
    
    def SetGrado(self,grado):
        self.__grado = grado

    def GetJornada(self):
        return self.__jornada

    def SetJornada(self,jornada):
        self.__jornada = jornada