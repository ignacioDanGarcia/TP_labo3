import random
from ContenedoresDirectorio.Contenedores import Contenedor

class TasadorDeContenedores():
    def __init__(self) -> None:
        pass
    
    def setear_precio_contenedor(contenedor):
        contenedor.set_precio_transporte_base(random.randint(1, 20000))
        return