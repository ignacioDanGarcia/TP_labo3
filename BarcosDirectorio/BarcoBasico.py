from Excepciones.exceptions import *
from BarcosDirectorio.Barcos import Barco
import sys
sys.path.insert(0,'ContenedoresDirectorio\Contenedor_basico_abstracto.py')
from ContenedorBasicoAbstracta import ContenedorBasicoAbstracta

class BarcoBasico(Barco):
    def __init__(self, peso_max, cant_contenedores_max, lleva_material_especial):
        super().__init__(peso_max, cant_contenedores_max, lleva_material_especial)
    
    def puede_cargar_esta_carga(self, carga):
        if not (isinstance(carga, ContenedorBasicoAbstracta)):
            raise Contenedor_no_aceptado_exception("Este barco solo puede llevar contenedores básicos")
        #Hay que ver como manejamos en la carga si lleva alguna carga especial o no.
        if not self.lleva_material_especial and carga.get_material_especial():
            raise Material_no_compatible_con_barco_Exceptionn("Este barco no puede llevar el material que se intenta cargar.")
        return True
        
    def tiene_lugar(self, contenedor):
        if self.contenedores.size() == self.cant_contenedores_max:
            # falta ver donde se catchea esta excepcion (sacar este comentario cuando ya este)
            raise Cantidad_contenedores_maxima_alcanzada_exception("El barco está lleno. No es posible cargar el contenedor.")
        
        if ( contenedor.get_peso() + self.obtener_peso_actual() )> self.peso_max:
            raise Peso_excedido_exception(f"Este peso es mucho para el barco. Sobran {self.obtener_peso_actual() + contenedor.get_peso() - self.peso_max} kgs")
        return True
    
    def cargar(self, contenedor):
        if self.puede_cargar_esta_carga(contenedor) and self.tiene_lugar(contenedor):
            self.contenedores.append(contenedor)
    
    
    'Probando'
    