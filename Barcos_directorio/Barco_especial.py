from Barcos_directorio.Barcos import Barco
from Barcos_directorio.Cargable import Cargable

class Barco_especial(Barco):
    def __init__(self, id, peso_max, cant_contenedores_max, lleva_mat_esp):
        super().__init__(id, peso_max, cant_contenedores_max, lleva_mat_esp)
    
    def puede_cargar(self, carga):
        pass
    