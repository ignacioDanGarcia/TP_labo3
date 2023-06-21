from BarcosDirectorio.Barcos import Barco
from BarcosDirectorio.ManejadorDeContenedoresDirectorio.StrategyBarcos import StrategyBarcos
from ContenedoresDirectorio.Contenedores import Contenedor
from TiposDeContenedores.TipoContenedor import TipoContenedor


class BarcoEspecialStrategy(StrategyBarcos):
    def verificar_contenedor(self, contenedor: Contenedor, barco: Barco):
        entra = True
            
        if barco.get_cant_contenedores_max()<= len(barco.get_contenedores()):
            entra = False
            
        return entra