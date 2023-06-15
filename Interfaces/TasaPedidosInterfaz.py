from abc import ABC, abstractmethod

class TasaPedidosInterfaz(ABC):
    @abstractmethod
    def definirPrecioViaje(self,pedido):
       pass