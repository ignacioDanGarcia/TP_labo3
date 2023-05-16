
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