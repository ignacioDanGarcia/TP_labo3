from abc import ABC, abstractmethod

class ViajeraInterfaz(ABC):
    @abstractmethod
    def viajar(self, contenedores):
        pass
