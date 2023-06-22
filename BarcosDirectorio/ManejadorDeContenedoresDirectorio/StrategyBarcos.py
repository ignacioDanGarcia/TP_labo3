from abc import ABC, abstractmethod

class StrategyBarcos(ABC):
    @abstractmethod
    def verificar_contenedor(self, barco, contenedor):
        pass