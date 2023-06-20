from BarcosDirectorio.Factory.CreadorBarcos import CreadorDeBarcos
from BarcosDirectorio.BarcoBasico import BarcoBasico
from BarcosDirectorio.TiposDeBarcos import TiposBarcos
class CreadorBarcosBasicos(CreadorDeBarcos):
    def __init__(self) -> None:
        super().__init__()
        
    def crear_barco(self, id, peso_max, cant_contenedores_max, combustible_maximo, sensor_viento = None):
        barco = BarcoBasico(id, peso_max,cant_contenedores_max,combustible_maximo, TiposBarcos.BASICO, sensor_viento)
        return barco