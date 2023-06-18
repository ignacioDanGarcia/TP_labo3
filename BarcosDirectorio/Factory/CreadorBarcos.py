from abc import ABC, abstractmethod
class CreadorDeBarcos(ABC):
    @abstractmethod
    def crear_barco(self, peso_max, cant_contenedores_max):
        pass