from BarcosDirectorio.Factory.CreadorBarcos import CreadorDeBarcos
from BarcosDirectorio.TiposDeBarcos import TiposBarcos
from Excepciones.exceptions import TipoDeBarcoInvalido
class SelectorCreador():
    def __init__(self) -> None:
        pass
    
    def crear_factoria_de_tipo_de_barco(self, tipoBarco :TiposBarcos):
        if tipoBarco == tipoBarco.BASICO or tipoBarco == tipoBarco.ESPECIAL:
            creador = CreadorDeBarcos(tipoBarco)
            return creador
        
        raise TipoDeBarcoInvalido("No hay una factoría para este tipo de barco.")