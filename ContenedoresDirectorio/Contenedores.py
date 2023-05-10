from abc import ABC
from Medidas_contenedores import Medidas

class Contenedor(ABC):

    def __init__(self, id, volumen, precioCarga, peso, medidas):
        self.volumen