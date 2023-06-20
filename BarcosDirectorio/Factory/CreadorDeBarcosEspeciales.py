from BarcosDirectorio.Factory.CreadorBarcos import CreadorDeBarcos
from BarcosDirectorio.BarcoEspecial import BarcoEspecial
from BarcosDirectorio.TiposDeBarcos import TiposBarcos
class CreadorBarcosEspeciales(CreadorDeBarcos):
    def __init__(self) -> None:
        super().__init__()
        
    def crear_barco(self, id, peso_max, cant_contenedores_max, combustible_maximo, sensor_viento = None):
        barco = BarcoEspecial(id, peso_max,cant_contenedores_max,combustible_maximo, TiposBarcos.ESPECIAL, sensor_viento)
        return barco