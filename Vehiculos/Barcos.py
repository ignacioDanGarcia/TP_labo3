import ABC, abstractmethod

class Barcos(ABC):
    def __init__(self, id, pesoMax, conteneMax, dimensiones_interior, dimensiones_exterior):
        self.id = id
        self.disponible = True
        self.pesoMax = pesoMax
        self.conteneMax = conteneMax
        self.kmRecorrido = 0
        self.dimensiones_interior = dimensiones_interior
        self.dimensiones_exterior = dimensiones_exterior
        
    @abstractmethod
    def cargar(self, carga):
        #redefinir en cada clase que ereda de barco
        pass
