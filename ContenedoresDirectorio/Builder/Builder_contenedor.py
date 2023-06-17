from ContenedoresDirectorio.Contenedores import Contenedor
from Medidas import Medidas
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
    
    
    '''
    Lo comento por si volvemos con el cambio.
    #Basicos:
    def set_tipo_basico(self):
        self.contenedor.set_tipo("Basico estandar")
        return self
        
    def set_volumen_maximo_basico(self):
        self.contenedor.set_volumen_max(32.6)
        return self

    def set_peso_maximo_basico(self):
        self.contenedor.set_peso_max(24000)
        return self
    def set_medidas_interior_basico(self):
        self.contenedor.set_medidas_interior( Medidas(6.0,2.35,2.3))
        return self
    def set_medidas_exterior_basico(self):
        self.contenedor.set_medidas_exterior(Medidas(6.1,2.45,2.6))
        return self
    
    #HC:
    def set_tipo_hc(self):
        self.contenedor.set_tipo("Basico HC")
        return self
    
    def set_volumen_maximo_hc(self):
        self.contenedor.set_volumen_max(67.7)
        return self
    
    def set_peso_maximo_hc(self):
        self.contenedor.set_peso_max(32500)
        return self
    
    def set_medidas_interior_hc(self):
        self.contenedor.set_medidas_interior(Medidas(12.0,2.35,2.3))
        return self
    
    def set_medidas_exterior_hc(self):
        self.contenedor.set_medidas_exterior(Medidas(12.1,2.45,2.6))
        return self
    
    
    #Flatrack:
    def set_tipo_flatrack(self):
        self.contenedor.set_tipo("Flat Rack")
        return self
    
    def set_volumen_maximo_flatrack(self):
        self.contenedor.set_volumen_max(33)
        return self
    
    def set_peso_maximo_flatrack(self):
        self.contenedor.set_peso_max(45000)
        return self
    
    def set_medidas_interior_flatrack(self):
        self.contenedor.set_medidas_interior(Medidas(6.0,100000,2.3))
        return self
    
    def set_medidas_exterior_flatrack(self):
        self.contenedor.set_medidas_exterior(Medidas(6.1,100000,2.3))
        return self
        
        '''