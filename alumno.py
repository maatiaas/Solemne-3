from persona import Persona

class Alumno(Persona):

    def __init__(self,nombre, edad, sueldo,curso,):
        super().__init__(nombre, edad, sueldo)
        self.__curso = curso

    def __str__(self):
        return super().__str__()+", Curso: {}".format(self.__curso)
    
    def GetCurso(self):
        return self.__curso
    
    def SetCurso(self,curso):
        self.__curso = curso