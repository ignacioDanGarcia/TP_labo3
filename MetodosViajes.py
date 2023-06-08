from abc import ABC, abstractmethod

class MetodosViajes(ABC):
    @abstractmethod
    def viajar(self):
        pass
    
    @abstractmethod
    def definirPrecioViaje(self,pedido):
        pass