from abc import ABC, abstractmethod

class MetodosViajes(ABC):
    @abstractmethod
    def viajar():
        pass
    
    @abstractmethod
    def definirPrecioViaje(self,viaje):
        pass