from Excepciones.exceptions import *
from BarcosDirectorio.Barcos import Barco
from Excepciones.exceptions import Cantidad_contenedores_maxima_alcanzada_exception, Peso_excedido_exception
from ContenedoresDirectorio.Contenedores import Contenedor

class BarcoBasico(Barco):
    def __init__(self, peso_max, cant_contenedores_max):
        super().__init__(peso_max, cant_contenedores_max, "Basico")
    
    def puede_cargar_esta_carga(self, contenedor: Contenedor):
        if not contenedor.get_tipo().value in [1, 2]:
            raise Contenedor_no_aceptado_exception("Este barco solo puede llevar contenedores básicos")
        #Hay que ver como manejamos en la carga si lleva alguna carga especial o no.
        
        return True
        
    def tiene_lugar(self, contenedor: Contenedor):
        if len(self.contenedores) == self.cant_contenedores_max:
            # falta ver donde se catchea esta excepcion (sacar este comentario cuando ya este)
            raise Cantidad_contenedores_maxima_alcanzada_exception("El barco está lleno. No es posible cargar el contenedor.")
        
        if ( contenedor.peso_contenedor() + self.obtener_peso_actual() )> self.peso_max:
            raise Peso_excedido_exception(f"Este peso es mucho para el barco. Sobran {self.obtener_peso_actual() + contenedor.peso_contenedor() - self.peso_max} kgs")
        return True
    
    def cargar(self, contenedor):
        if self.puede_cargar_esta_carga(contenedor) and self.tiene_lugar(contenedor):
            self.contenedores.append(contenedor)
 