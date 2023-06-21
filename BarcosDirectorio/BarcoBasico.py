from Excepciones.exceptions import *
from BarcosDirectorio.Barcos import Barco
from Excepciones.exceptions import Cantidad_contenedores_maxima_alcanzada_exception, Peso_excedido_exception
from ContenedoresDirectorio.Contenedores import Contenedor
from BarcosDirectorio.TiposDeBarcos import TiposBarcos
from ContenedoresDirectorio.TiposDeContenedores.TipoContenedor import TipoContenedor
class BarcoBasico(Barco):
    def __init__(self, id, peso_max, cant_contenedores_max, combustible_maximo,tipoBarco=None,  sensor_viento=None):
        super().__init__(id, peso_max, cant_contenedores_max, combustible_maximo, TiposBarcos.BASICO, sensor_viento)
    
    '''def puede_cargar_esta_carga(self, contenedor: Contenedor):
        if not contenedor.get_tipo() in [TipoContenedor.BASICO, TipoContenedor.BASICOHC]:
            return False
    
        return True
        
    def tiene_lugar(self, contenedor: Contenedor):
        if len(self.contenedores) == self.cant_contenedores_max:
            return False
        
        if ( contenedor.peso_contenedor() + self.obtener_peso_actual() )> self.peso_max:
            return False
        return True
    
    def cargar(self, contenedor):
        if self.puede_cargar_esta_carga(contenedor) and self.tiene_lugar(contenedor):
            self.contenedores.append(contenedor)
    '''