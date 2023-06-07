from ContenedorBasicoAbstracta import ContenedorBasicoAbstracta
from Contenedores import Contenedor
from Medidas import Medidas


class ContenedorBasicoEstandar(ContenedorBasicoAbstracta):
    def __init__(self, mat_especial):
        super().__init__(mat_especial)
        self.medidas_exterior = Medidas(6.1,2.45,2.6)
        self.medidas_interior = Medidas(6.0,2.35,2.3)
        self.peso_max = 24000
        self.volumen_max = 32.6
        
    