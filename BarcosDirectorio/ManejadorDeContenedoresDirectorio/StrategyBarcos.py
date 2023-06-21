from abc import ABC, abstractmethod
from Cargas.Carga import Carga

class StrategyBarcos(ABC):
    @abstractmethod
    def verificar_contenedor(self, barco, contenedor):
        pass