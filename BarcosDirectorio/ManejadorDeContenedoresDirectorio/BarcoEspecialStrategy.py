from BarcosDirectorio.Barcos import Barco
from BarcosDirectorio.ManejadorDeContenedoresDirectorio.StrategyBarcos import StrategyBarcos
from ContenedoresDirectorio.Contenedores import Contenedor
class BarcoEspecialStrategy(StrategyBarcos):
    def verificar_contenedor(self,barco: Barco, contenedor: Contenedor):
        entra = True
            
        if barco.get_cant_contenedores_max()<= len(barco.get_contenedores()):
            entra = False
        
        if ( contenedor.peso_contenedor() + barco.obtener_peso_actual() )> barco.peso_max:
            entra = False
        return entra
