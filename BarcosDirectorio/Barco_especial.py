from BarcosDirectorio.Barcos import Barco
from Excepciones.exceptions import Cantidad_contenedores_maxima_alcanzada_exception, Material_no_compatible_con_barco_Exceptionn, Peso_excedido_exception

class Barco_especial(Barco):
    def __init__(self, id, peso_max, cant_contenedores_max, lleva_mat_esp):
        super().__init__(id, peso_max, cant_contenedores_max, lleva_mat_esp)
    
    def puede_cargar_esta_carga(self, contenedor):
        if not self.lleva_mat_esp and contenedor.get_mat_especial():
            raise Material_no_compatible_con_barco_Exceptionn("Este barco no puede llevar el material que se intenta cargar.")
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