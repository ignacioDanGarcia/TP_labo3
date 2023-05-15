from Contenedores import Contenedor
from Medidas_contenedores import Medidas


class FlatRackContenedor(Contenedor):
    def __init__(self,id, precio_transporte):
        super().__init__(id, precio_transporte)
        self.medidas_exterior = Medidas(6.1,100000,2.3)
        self.medidas_interior = Medidas(6.0,100000,2.3)
        self.volumen_max = 33
        self.peso_max = 45000
        self.carga = None

    def verificar_carga(self, carga):
        carga_verificada = False
        
    