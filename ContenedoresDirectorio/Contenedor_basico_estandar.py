from Contenedor_basico_abstracta import Cont_basico_abstracto
from Contenedores import Contenedor
from Medidas import Medidas


class Contenedor_Basico_Estandar(Cont_basico_abstracto):
    def __init__(self,id, mat_especial):
        super().__init__(id, mat_especial)
        self.medidas_exterior = Medidas(6.1,2.45,2.6)
        self.medidas_interior = Medidas(6.0,2.35,2.3)
        self.peso_max = 24000
        self.volumen_max = 32.6
        self.carga = None
    