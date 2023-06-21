from ContenedoresDirectorio.Builder.Builder_contenedor import Contenedor_builder
from Medidas import Medidas
from TiposDeContenedores.TipoContenedor import TipoContenedor
from ContenedoresDirectorio.Builder.BuilderDecorators import agregar_precio_adicional_open_top


@agregar_precio_adicional_open_top
class BuilderContenedorOpenTop(Contenedor_builder):
    def __init__(self) -> None:
        super().__init__()
    
    
    def set_tipo(self):
        self.contenedor.set_tipo(TipoContenedor.OPENTOP)
        return self
    def set_volumen_maximo(self):
        self.contenedor.set_volumen_max(67.7) # = hc
        return self
    def set_peso_maximo(self):
        self.contenedor.set_peso_max(45000) # = flatrack
        return self
    # ojo que no podes meter cualquier cosa re alta, tambien hay que tener en cuenta el volumen
    def set_medidas_interior(self):
        self.contenedor.set_medidas_interior( Medidas(12.0,2.35,100000)) # paredes = hc
        return self
    def set_medidas_exterior(self):
        self.contenedor.set_medidas_exterior(Medidas(12.1,2.45,100000))
        return self