class Figuras:
    def __init__(self,x,y,visible):
        self.x=x
        self.y=y
        self.visible=visible

    def estaVisible(self):
        return f"visible = {self.visible}"
    
    def mostrar(self):
        return f"x= {self.x} \n y= {self.y}"
    
    def ocultar(self):
        return ""
    
    def mover(self):
        return f"x={self.y} \n y= {self.x}"
    
    def calcularArea(self):
        return f"Area: "
    
class Rectangulos(Figuras):
    def __init__(self, x, y, visible,alto,ancho):
        super().__init__(x, y, visible)
        self.__alto=alto
        self.__ancho=ancho

    @property
    def alto(self):
        return self.__alto
    @alto.setter
    def alto(self,alto):
        self.__alto=alto

    @property
    def ancho(self):
        return self.__ancho
    @alto.setter
    def alto(self,ancho):
        self.__ancho=ancho

    def ocultar(self):
        return super().ocultar()
    
    def mostrar(self):
        return super().mostrar()
    
    def calcularArea(self):
        return f"Area de un rectangulo= {self.ancho/self.alto}"
    
class Circulos(Figuras):
    def __init__(self, x, y, visible,radio):
        super().__init__(x, y, visible)
        self.__radio=radio

    @property
    def radio(self):
        return self.__radio
    @radio.setter
    def radio(self,radio):
        self.__radio=radio

    def ocultar(self):
        return super().ocultar()
    
    def mostrar(self):
        return super().mostrar()
    
    def calcularArea(self):
        return f"Area de un circulo= {(self.radio*self.radio)*3.14}"
    
rectangulo1=Rectangulos(3,4,True,10,20)
print(f"\n x={rectangulo1.x} \n y={rectangulo1.y} \n visible={rectangulo1.visible} \n alto={rectangulo1.alto} \n ancho={rectangulo1.ancho}")
print(rectangulo1.calcularArea())

circulo1=Circulos(3,3,True,6)
print(f"\n x={circulo1.x} \n y={circulo1.y} \n visible={circulo1.visible} \n radio={circulo1.radio}")
print(circulo1.calcularArea())