from ContenedoresDirectorio.Builder.Builder_contenedor import Contenedor_builder
from Medidas import Medidas
from TiposDeContenedores.TipoContenedor import TipoContenedor

class BuilderContenedorBasicoHC(Contenedor_builder):
    def __init__(self) -> None:
        super().__init__()
        
    def set_tipo(self):
        self.contenedor.set_tipo(TipoContenedor.BASICOHC)
        return self
    
    def set_volumen_maximo(self):
        self.contenedor.set_volumen_max(67.7)
        return self
    
    def set_peso_maximo(self):
        self.contenedor.set_peso_max(32500)
        return self
    
    def set_medidas_interior(self):
        self.contenedor.set_medidas_interior(Medidas(12.0,2.35,2.3))
        return self
    
    def set_medidas_exterior(self):
        self.contenedor.set_medidas_exterior(Medidas(12.1,2.45,2.6))
        return self
    
