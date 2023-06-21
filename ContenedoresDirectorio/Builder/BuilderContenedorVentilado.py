from ContenedoresDirectorio.Builder.Builder_contenedor import Contenedor_builder
from Medidas import Medidas
from ContenedoresDirectorio.TiposDeContenedores.Tipo import TipoContenedor
class BuilderContenedorVentilado(Contenedor_builder):
    def __init__(self) -> None:
        super().__init__()
    
    
    def set_tipo(self):
        self.contenedor.set_tipo(TipoContenedor.VENTILADO)
        return self
    def set_volumen_maximo(self):
        self.contenedor.set_volumen_max(32.6)
        return self
    def set_peso_maximo(self):
        self.contenedor.set_peso_max(24000)
        return self
    def set_medidas_interior(self):
        self.contenedor.set_medidas_interior( Medidas(6.0,2.35,2.3))
        return self
    def set_medidas_exterior(self):
        self.contenedor.set_medidas_exterior(Medidas(6.1,2.45,2.6))
        return self
    