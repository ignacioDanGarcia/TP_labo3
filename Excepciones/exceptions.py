
# excepciones barcos
class Contenedor_no_aceptado_exception(Exception):
    def __init__(self, mensaje) -> None:
        self.mensaje = mensaje
    def __str__(self) -> str:
        return self.mensaje
    
class Material_no_compatible_con_barco_Exceptionn(Exception):
    def __init__(self, mensaje) -> None:
        self.mensaje = mensaje
    def __str__(self) -> str:
        return self.mensaje
    
class Peso_excedido_exception(Exception):
    def __init__(self, mensaje) -> None:
        self.mensaje = mensaje
    def __str__(self) -> str:
        return self.mensaje
    
class Cantidad_contenedores_maxima_alcanzada_exception(Exception):
    def __init__(self, mensaje) -> None:
        self.mensaje = mensaje
    def __str__(self) -> str:
        return self.mensaje
    

 # Excepciones Empresa... esto habria que cambiarlo de lugar pero por ahora lo dejo aca
 
class No_hay_camiones_disponibles(Exception):
    def __init__(self, mensaje) -> None:
        self.mensaje = mensaje
    def __str__(self) -> str:
        return self.mensaje
    
class distancia_incorrecta(Exception):
    def __init__(self, mensaje) -> None:
        self.mensaje = mensaje
    def __str__(self) -> str:
        return self.mensaje
    
# excepcion contenedor basico abstracto
class el_contenedor_basico_no_puede_mat_especial(Exception):
    def __init__(self, mensaje) -> None:
        self.mensaje = mensaje
    def __str__(self) -> str:
        return self.mensaje