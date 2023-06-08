from ContenedoresDirectorio.Contenedores import Contenedor
from Medidas import Medidas


class FlatRackContenedor(Contenedor):
    def __init__(self, mat_especial):
        super().__init__(mat_especial)
        self.medidas_exterior = Medidas(6.1,100000,2.3)
        self.medidas_interior = Medidas(6.0,100000,2.3)
        self.volumen_max = 33
        self.peso_max = 45000
        self.carga = None

    def verificar_carga(self, carga):
        return super().verificar_carga(carga)
        
    