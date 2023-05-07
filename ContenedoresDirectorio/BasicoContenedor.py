from ..Contenedores import Contenedores


class BasicoContenedor(Contenedores):
    def __init__(self, id, volumen, precioCarga, peso, medidas):
        super().__init__(id, volumen, peso, precioCarga, medidas)
    