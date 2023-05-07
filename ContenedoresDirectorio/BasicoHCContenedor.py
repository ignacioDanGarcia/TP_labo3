from ..Contenedores import Contenedores


class BasicoHCContenedor(Contenedores):
    def __init__(self, id, volumen, precioCarga, peso, medidas):
        super().__init__(id, volumen, peso, precioCarga, medidas)
    