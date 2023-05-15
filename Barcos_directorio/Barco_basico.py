from Barcos_directorio.Barcos import Barco
from Cont_basico_interfaz import Cont_basico_interfaz
from Barcos_directorio.Excepciones.Contenedor_no_aceptado_exception import Contenedor_no_aceptado_exception
from Barcos_directorio.Excepciones.Peso_excedido_exception import Peso_excedido_exception

class Barco_basico(Barco):
    def __init__(self, id, peso_max, cant_contenedores_max, lleva_mat_esp):
        super().__init__(id, peso_max, cant_contenedores_max, lleva_mat_esp)
    
    def puede_cargar(self, carga):
        if not (isinstance(carga, Cont_basico_interfaz)):
            raise Contenedor_no_aceptado_exception("Este barco solo puede llevar contenedores básicos")
        else:
            if ( carga.get_peso() + self.obtener_peso_actual() )> self.peso_max:
                raise Peso_excedido_exception(f"Este peso es mucho para el barco. Sobran {self.obtener_peso_actual() + carga.get_peso() - self.peso_max} kgs")