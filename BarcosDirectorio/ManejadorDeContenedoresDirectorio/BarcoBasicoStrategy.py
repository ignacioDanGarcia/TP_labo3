from BarcosDirectorio.Barcos import Barco
from BarcosDirectorio.ManejadorDeContenedoresDirectorio.StrategyBarcos import StrategyBarcos
from ContenedoresDirectorio.Contenedores import Contenedor
from TiposDeContenedores.TipoContenedor import TipoContenedor


class BarcoBasicoStrategy(StrategyBarcos):
    def verificar_contenedor(self, contenedor: Contenedor, barco: Barco):
        puede_llevarla = True
        entra = True
        
        if contenedor.get_tipo() != TipoContenedor.BASICO:
            puede_llevarla = False
            
        if barco.get_cant_contenedores_max()<= len(barco.get_contenedores()):
            entra = False
            
        return puede_llevarla and entra