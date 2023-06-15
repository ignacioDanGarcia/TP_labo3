from abc import ABC, abstractmethod
from Cargas.Carga import Carga

class Estrategia(ABC):
    @abstractmethod
    def verificar_carga(self, carga : Carga, contenedor):
        pass
