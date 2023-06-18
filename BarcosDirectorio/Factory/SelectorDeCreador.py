from BarcosDirectorio.TiposDeBarcos import TiposBarcos
from BarcosDirectorio.Factory.CreadorDeBarcosBasicos import CreadorBarcosBasicos
from BarcosDirectorio.Factory.CreadorDeBarcosEspeciales import CreadorBarcosEspeciales
class SelectorCreador():
    def __init__(self) -> None:
        pass
    
    def crear_factoria(self, tipoBarco :TiposBarcos):
        if tipoBarco == tipoBarco.BASICO:
            return CreadorBarcosBasicos()
        if tipoBarco == tipoBarco.ESPECIAL:
            return CreadorBarcosEspeciales()
        raise AttributeError("No hay una factoría para este tipo de barco.")