from BarcosDirectorio.Barcos import Barco
from BarcosDirectorio.ManejadorDeContenedoresDirectorio.StrategyBarcos import StrategyBarcos
from ContenedoresDirectorio.Contenedores import Contenedor
from ContenedoresDirectorio.TiposDeContenedores.TipoContenedor import TipoContenedor
from Excepciones.exceptions import Peso_excedido_exception
class BarcoEspecialStrategy(StrategyBarcos):
    def verificar_contenedor(self,barco: Barco, contenedor: Contenedor):
        entra = True
            
        if barco.get_cant_contenedores_max()<= len(barco.get_contenedores()):
            '''raise Cantidad_contenedores_maxima_alcanzada_exception("a)'''
            entra = False
        
        if ( contenedor.peso_contenedor() + barco.obtener_peso_actual() )> barco.peso_max:
            '''raise Peso_excedido_exception("a")'''
            entra = False
        ''' if ( contenedor.peso_contenedor() + barco.obtener_peso_actual() )> barco.peso_max:
            # no se si esta excepcion puede ser catcheada por el metodo que la usa, porque esta en esta misma clase
            raise Peso_excedido_exception(f"Este peso es mucho para el barco. Sobran {self.obtener_peso_actual() + contenedor.peso_contenedor() - self.peso_max} kgs")
        '''
        return entra
