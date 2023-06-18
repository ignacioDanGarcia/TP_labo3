from abc import ABC, abstractmethod
class SistemaNavegacion(ABC):
    def __init__(self,barco) -> None:
        self.barco = barco
    
    def set_barco(self, barco):
        self.barco = barco
        
    @abstractmethod
    def navegar(self, horas, barco):
        pass
    abstractmethod
    def mostrar_tipo(self):
        pass