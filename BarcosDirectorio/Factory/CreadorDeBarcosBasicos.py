from BarcosDirectorio.Factory.CreadorBarcos import CreadorDeBarcos
from BarcosDirectorio.BarcoBasico import BarcoBasico
class CreadorBarcosBasicos(CreadorDeBarcos):
    def __init__(self) -> None:
        super().__init__()
        
    def crear_barco(self, peso_max, cant_contenedores_max):
        barco = BarcoBasico(peso_max,cant_contenedores_max)
        return barco