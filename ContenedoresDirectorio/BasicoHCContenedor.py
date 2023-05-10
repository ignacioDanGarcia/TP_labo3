from Contenedores import Contenedor
from Medidas_contenedores import Medidas


class BasicoHCContenedor(Contenedor):
    
    def __init__(self,id, precio_transporte):
        super().__init__(id, precio_transporte)
        self.medidas_exterior = Medidas(12.1,2.45,2.6)
        self.medidas_interior = Medidas(12.0,2.35,2.3)
        self.volumen_max = 67.7
        self.peso_max = 32500
        self.carga = None

    
       
    