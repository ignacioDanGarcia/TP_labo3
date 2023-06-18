from BarcosDirectorio.Barcos import Barco
from Excepciones.exceptions import Cantidad_contenedores_maxima_alcanzada_exception, Peso_excedido_exception
from ContenedoresDirectorio.Contenedores import Contenedor
from BarcosDirectorio.TiposDeBarcos import TiposBarcos

class BarcoEspecial(Barco):
    def __init__(self, peso_max, cant_contenedores_max, combustible_maximo, tipoBarco=None, sensor_viento=None):
        super().__init__(peso_max, cant_contenedores_max, combustible_maximo, TiposBarcos.ESPECIAL, sensor_viento)
    
    def puede_cargar_esta_carga(self, contenedor: Contenedor):
        return True
    
    def tiene_lugar(self,contenedor):
        if len(self.contenedores) >= self.cant_contenedores_max:
            # falta ver donde se catchea esta excepcion (sacar este comentario cuando ya este)
            raise Cantidad_contenedores_maxima_alcanzada_exception("El barco está lleno. No es posible cargar el contenedor.")
        
        if ( contenedor.peso_contenedor() + self.obtener_peso_actual() )> self.peso_max:
            raise Peso_excedido_exception(f"Este peso es mucho para el barco. Sobran {self.obtener_peso_actual() + contenedor.peso_contenedor() - self.peso_max} kgs")
        return True
    
    
    def cargar(self, contenedor):
        if self.puede_cargar_esta_carga(contenedor) and self.tiene_lugar(contenedor):
            self.contenedores.append(contenedor)
            return True