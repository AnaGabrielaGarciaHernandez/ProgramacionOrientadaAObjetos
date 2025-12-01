class Personas:
    def __init__(self,nombre,edad,tel):
        self.nombre=nombre
        self.edad=edad
        self.tel=tel

    def info_persona(self):
        return f"nombre: {self.nombre} \n edad: {self.edad} \n tel{self.tel}"
    

class Estudiantes(Personas):
    def __init__(self,nombre,edad,tel,carrera,matricula):
        super().__init__(nombre,edad,tel)
        self.__carrera=carrera
        self.__matricula=matricula

    @property
    def carrera(self):
        return self.__carrera
    
    @carrera.setter
    def carrera(self,carrera):
        self.__carrera=carrera

    @property
    def matricula(self):
        return self.__matricula
    
    @matricula.setter
    def matricula(self,matricula):
        self.__matricula=matricula
    
    def info_persona(self):
        return f"nombre: {self.nombre} \n edad: {self.edad} \n tel{self.tel}"
    
    def info_carrera(self):
        return f"carrera: {self.carrera}"
    
estudiante1=Estudiantes("Ana",19,123,"TI",12345)
print(estudiante1.info_persona())
print(estudiante1.info_carrera())
print(f"Matricula: {estudiante1.matricula}")

