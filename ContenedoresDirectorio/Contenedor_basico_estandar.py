from Contenedores import Contenedor


class Contenedor_Basico_Estandar(Contenedor):
    def __init__(self, id, volumen, precioCarga, peso, medidas):
        super().__init__(id, volumen, peso, precioCarga, medidas)
    