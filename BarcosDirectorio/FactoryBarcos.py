import abc
from BarcosDirectorio.Barcos import Barco

class FactoryBarcos:
    
    @staticmethod
    def obtener_tipos_barcos():
        subclases_barco = Barco.__subclasses__()
        tipos_barcos = [subclase.__name__ for subclase in subclases_barco]
        return tipos_barcos

    @staticmethod
    def crear_barco(tipo_barco, *args, **kwargs):
        subclases_barco = Barco.__subclasses__()

        for subclase in subclases_barco:
            if subclase.__name__ == tipo_barco:
                return subclase(*args, **kwargs)

        raise ValueError(f"No se encontró una subclase de Barco con el nombre '{tipo_barco}'")