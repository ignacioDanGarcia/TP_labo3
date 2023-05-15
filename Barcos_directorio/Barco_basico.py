from Barcos_directorio.Barcos import Barco


class Barco_basico(Barco):
    def __init__(self, id, peso_max, cant_contenedores_max, lleva_mat_esp):
        super().__init__(id, peso_max, cant_contenedores_max, lleva_mat_esp)
        