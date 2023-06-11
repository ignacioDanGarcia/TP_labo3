from BarcosDirectorio.Barcos import Barco
from Excepciones.exceptions import Cantidad_contenedores_maxima_alcanzada_exception, Material_no_compatible_con_barco_Exceptionn, Peso_excedido_exception

class BarcoEspecial(Barco):
    def __init__(self, peso_max, cant_contenedores_max, lleva_material_especial):
        super().__init__(peso_max, cant_contenedores_max, lleva_material_especial)
    
    def puede_cargar_esta_carga(self, contenedor):
        if not self.lleva_material_especial and contenedor.get_material_especial():
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