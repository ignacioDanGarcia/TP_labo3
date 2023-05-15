from abc import ABC, abstractmethod
class Cargable(ABC):
    def puede_cargar(self, carga):
        pass
    def cargar(self, carga):
        pass