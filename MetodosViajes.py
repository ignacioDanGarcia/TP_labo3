from abc import ABC, abstractmethod

class MetodosViajes(ABC):
    @abstractmethod
    def viajar(self):
        pass
    
    @abstractmethod
    def definirPrecioViaje(self,pedido):
        pass
    
    
    # ambas funciones estan en barco, empresa y contenedores. Capaz hay que acomodar esto