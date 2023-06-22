from ContenedoresDirectorio.Contenedores import Contenedor
from abc import ABC, abstractmethod

class Contenedor_builder(ABC):
    
    def __init__(self) -> None:
      pass

    def reset(self, id, material_especial):
      self.contenedor = Contenedor(id, material_especial)
      return self
    
    def get_contenedor(self):
        return self.contenedor
    
    @abstractmethod
    def set_tipo(self):
        return self
    @abstractmethod
    def set_volumen_maximo(self):
        return self
    @abstractmethod
    def set_peso_maximo(self):
        return self
    @abstractmethod
    def set_medidas_interior(self):
        return self
    @abstractmethod
    def set_medidas_exterior(self):
        return self