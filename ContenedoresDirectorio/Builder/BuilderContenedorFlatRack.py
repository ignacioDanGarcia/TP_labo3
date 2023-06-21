from ContenedoresDirectorio.Builder.Builder_contenedor import Contenedor_builder
from Medidas import Medidas
from TiposDeContenedores.TipoContenedor import TipoContenedor
class BuilderContenedorFlatRack(Contenedor_builder):
    def __init__(self) -> None:
        super().__init__()
        
    def set_tipo(self):
        self.contenedor.set_tipo(TipoContenedor.FLATRACK)
        return self
    def set_volumen_maximo(self):
        self.contenedor.set_volumen_max(33)
        return self
    def set_peso_maximo(self):
        self.contenedor.set_peso_max(45000)
        return self
    def set_medidas_interior(self):
        self.contenedor.set_medidas_interior(Medidas(6.0,100000,2.3))
        return self
    def set_medidas_exterior(self):
        self.contenedor.set_medidas_exterior(Medidas(6.1,100000,2.3))
        return self
