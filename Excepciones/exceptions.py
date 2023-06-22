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
    
class TipoDeBarcoInvalido(AttributeError):
    def __init__(self, mensaje) -> None:
        self.mensaje = mensaje
    def __str__(self) -> str:
        return self.mensaje
class CombustibleInsuficienteException(Exception):
    def __init__(self, mensaje) -> None:
        self.mensaje = mensaje
    def __str__(self) -> str:
        return self.mensaje

class No_hay_camiones_disponibles(Exception):
    def __init__(self, mensaje) -> None:
        self.mensaje = mensaje
    def __str__(self) -> str:
        return self.mensaje
    
class No_hay_barcos_disponibles(Exception):
    def __init__(self, mensaje) -> None:
        self.mensaje = mensaje
    def __str__(self) -> str:
        return self.mensaje
    
class distancia_incorrecta(Exception):
    def __init__(self, mensaje) -> None:
        self.mensaje = mensaje
    def __str__(self) -> str:
        return self.mensaje
class tiempo_incorrecto(Exception):
    def __init__(self, mensaje) -> None:
        self.mensaje = mensaje
    def __str__(self) -> str:
        return self.mensaje
    
class Hay_cargas_que_no_entraron_en_contenedores(Exception):
    def __init__(self, mensaje) -> None:
        self.mensaje = mensaje
    def __str__(self) -> str:
        return self.mensaje
    
    

class el_contenedor_basico_no_puede_mat_especial(Exception):
    def __init__(self, mensaje) -> None:
        self.mensaje = mensaje
    def __str__(self) -> str:
        return self.mensaje
    

class contenedor_no_puede_llevar_carga(Exception):
    def __init__(self, mensaje) -> None:
        self.mensaje = mensaje
    def __str__(self) -> str:
        return self.mensaje


class medidas_incorrectas(Exception):
    def __init__(self, mensaje) -> None:
        self.mensaje = mensaje
    def __str__(self) -> str:
        return self.mensaje
    
class no_existe_carga(Exception):
    def __init__(self, mensaje) -> None:
        self.mensaje = mensaje
    def __str__(self) -> str:
        return self.mensaje