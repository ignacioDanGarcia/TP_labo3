from BarcosDirectorio.Barcos import Barco
from BarcosDirectorio.ManejadorDeContenedoresDirectorio.StrategyBarcos import StrategyBarcos
from ContenedoresDirectorio.Contenedores import Contenedor
from ContenedoresDirectorio.TiposDeContenedores.TipoContenedor import TipoContenedor


class BarcoBasicoStrategy(StrategyBarcos):
    def verificar_contenedor(self, barco: Barco, contenedor: Contenedor):
        puede_llevarla = True
        entra = True
        
        if contenedor.get_tipo() != TipoContenedor.BASICO:
            puede_llevarla = False
            
        if barco.get_cant_contenedores_max()<= len(barco.get_contenedores()):
            entra = False
            
        
        if ( contenedor.peso_contenedor() + barco.obtener_peso_actual() )> barco.peso_max:
            '''raise Peso_excedido_exception("a")'''
            entra = False
            
        return puede_llevarla and entra