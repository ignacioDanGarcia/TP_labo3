from BarcosDirectorio.Factory.CreadorBarcos import CreadorDeBarcos
from BarcosDirectorio.BarcoEspecial import BarcoEspecial
class CreadorBarcosEspeciales(CreadorDeBarcos):
    def __init__(self) -> None:
        super().__init__()
        
    def crear_barco(self, peso_max, cant_contenedores_max):
        barco = BarcoEspecial(peso_max,cant_contenedores_max)
        return barco