class Contenedor_no_aceptado_exception(Exception):
    def __init__(self, mensaje) -> None:
        self.mensaje = mensaje
    def __str__(self) -> str:
        return self.mensaje