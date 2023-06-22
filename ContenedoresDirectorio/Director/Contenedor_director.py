from ContenedoresDirectorio.Builder.Builder_contenedor import Contenedor_builder


class Contenedor_director:
    def __init__(self, builder : Contenedor_builder) -> None:
      self.builder = builder
      
    def change_builder(self, builder):
      self.builder = builder
            
    def crear_contenedor(self, id, material_especial):
      self.builder \
      .reset(id, material_especial) 
      return self.builder \
      .set_tipo() \
      .set_peso_maximo() \
      .set_medidas_interior() \
      .set_medidas_exterior() \
      .set_volumen_maximo() \
      .get_contenedor()