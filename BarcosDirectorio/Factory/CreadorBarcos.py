from BarcosDirectorio.TiposDeBarcos import TiposBarcos
from BarcosDirectorio.Barcos import Barco
class CreadorDeBarcos():
    def __init__(self, tipoBarco :TiposBarcos) -> None:
        self.__tipoBarco = tipoBarco
    
    def crear_barco(self, id, peso_max, cant_contenedores_max, combustible_maximo, sensor_viento = None):
        barco = Barco(id,peso_max,cant_contenedores_max,combustible_maximo,self.__tipoBarco,sensor_viento)
        return barco

    def get_tipoBarco(self):
        return self.__tipoBarco
    def set_tipoBarco(self,tipo):
        self.__tipoBarco = tipo
    tipoBarco = property(get_tipoBarco,set_tipoBarco)