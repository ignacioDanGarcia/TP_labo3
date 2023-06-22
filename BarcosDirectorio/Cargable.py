from abc import ABC, abstractmethod
class Cargable(ABC):
    def tiene_lugar(self):
        pass
    def puede_cargar_esta_carga(self, contenedor):
        pass
    def cargar(self, contenedor):
        pass