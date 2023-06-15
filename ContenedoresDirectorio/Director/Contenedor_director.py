from ContenedoresDirectorio.Builder.Builder_contenedor import Contenedor_builder
from GenerarId import GenerarId
from TasadorDeContenedores import TasadorDeContenedores

class Contenedor_director:
    def __init__(self, builder : Contenedor_builder) -> None:
      self.builder = builder
      
    def change_builder(self, builder):
      self.builder = builder
    
    '''
    Lo comento por si volvemos con el cambio.
    def crear_contenedor_basico(self, material_especial):
      return self\
      .crear_contenedor(material_especial) \
      .set_tipo_basico() \
      .set_medidas_exterior_basico()\
      .set_medidas_interior_basico()\
      .set_peso_maximo_basico()\
      .set_volumen_maximo_basico() \
      .get_contenedor()
    
    def crear_contenedor_hc(self, material_especial):
      return self\
      .crear_contenedor(material_especial) \
      .set_tipo_hc() \
      .set_medidas_exterior_hc()\
      .set_medidas_interior_hc()\
      .set_peso_maximo_hc()\
      .set_volumen_maximo_hc() \
      .get_contenedor()
        
    def crear_contenedor_flatrack(self, material_especial):
      return self\
      .crear_contenedor(material_especial) \
      .set_tipo_flatrack() \
      .set_medidas_exterior_flatrack()\
      .set_medidas_interior_flatrack()\
      .set_peso_maximo_flatrack()\
      .set_volumen_maximo_flatrack() \
      .get_contenedor()'''
            
    def crear_contenedor(self, material_especial):
      self.builder \
      .reset(material_especial) 
      return self.builder \
      .set_tipo() \
      .set_peso_maximo() \
      .set_medidas_interior() \
      .set_medidas_exterior() \
      .set_volumen_maximo() \
      .get_contenedor()