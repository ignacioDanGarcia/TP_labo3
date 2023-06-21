from BarcosDirectorio.ManejadorDeContenedoresDirectorio.BarcoBasicoStrategy import BarcoBasicoStrategy
from BarcosDirectorio.ManejadorDeContenedoresDirectorio.BarcoEspecialStrategy import BarcoEspecialStrategy
from BarcosDirectorio.TiposDeBarcos import TiposBarcos



class SelectoraEstrategiaPorBarco():
    def __init__(self) -> None:
        pass
    # Si se mete una nueva estrategia la agregaríamos acá! ;)
    def estrategia_por_categoria(self, categoria):
        estrategias = {
        TiposBarcos.BASICO: BarcoBasicoStrategy(),
        TiposBarcos.ESPECIAL: BarcoEspecialStrategy()
    }
        return estrategias.get(categoria)