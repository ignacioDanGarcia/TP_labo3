from Contenedores import Contenedor
from Medidas_contenedores import Medidas


class Contenedor_Basico_Estandar(Contenedor):
    def __init__(self, id, volumen, precioCarga, peso, medidas):
        super().__init__(id, volumen, peso, precioCarga, medidas)
        self.medidas_exterior = Medidas(6.1,2.45,2.6)
        self.medidas_interior = Medidas(6.0,2.35,2.3)
        self.peso_max = 24000
        self.volumen_max
    