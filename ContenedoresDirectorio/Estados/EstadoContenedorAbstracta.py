from abc import ABC, abstractmethod

class EstadoContenedorAbstracta(ABC):

    def transicion(self, distancia, carga):
        if not self.condicion(distancia):
            self.cambiar_estado_siguiente()
            
            return self.estado_siguiente.transicion(distancia, carga)
        else:
            
            return self.calcular_precio_adicional_estado(carga)

    @abstractmethod
    def calcular_precio_adicional_estado(self, carga):
        pass
    
    @abstractmethod
    def condicion(self, distancia):
        pass
    @abstractmethod
    def cambiar_estado_siguiente(self):
        pass
