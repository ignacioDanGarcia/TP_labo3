from ContenedoresDirectorio.Contenedor_basico_abstracta import Cont_basico_abstracto

from Medidas import Medidas

class BasicoHCContenedor(Cont_basico_abstracto):
    
    def __init__(self, mat_especial):
        super().__init__( mat_especial)
        self.medidas_exterior = Medidas(12.1,2.45,2.6)
        self.medidas_interior = Medidas(12.0,2.35,2.3)
        self.volumen_max = 67.7
        self.peso_max = 32500
        

    def verificar_carga(self, carga):
        return super().verificar_carga(carga)
       
    