from BarcosDirectorio.TiposDeBarcos import TiposBarcos
from BarcosDirectorio.Factory.CreadorDeBarcosBasicos import CreadorBarcosBasicos
from BarcosDirectorio.Factory.CreadorDeBarcosEspeciales import CreadorBarcosEspeciales
from Excepciones.exceptions import TipoDeBarcoInvalido
class SelectorCreador():
    def __init__(self) -> None:
        pass
    
    def crear_factoria(self, tipoBarco :TiposBarcos):
        if tipoBarco == tipoBarco.BASICO:
            return CreadorBarcosBasicos()
        if tipoBarco == tipoBarco.ESPECIAL:
            return CreadorBarcosEspeciales()
        raise TipoDeBarcoInvalido("No hay una factoría para este tipo de barco.")