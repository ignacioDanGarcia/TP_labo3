from Medidas import Medidas
from Tasador_de_cargas import Tasador_de_cargas

class Carga:

    def __init__(self, medidas, peso):
        tas = Tasador_de_cargas()
        
        p = tas.setear_precio_carga()

        self.__medidas = medidas
        self.__precio = p
        self.__peso = peso
    
    'Getters y setters'
    def get_medidas(self):
        return self.__medidas
    def set_medidas(self,m):
        self.__medidas = m
    medidas = property(get_medidas,set_medidas)
    
    def get_precio(self):
        return self.__precio
    def set_precio(self):
        pass
    precio = property(get_precio,set_precio)
    
    def get_peso(self):
        return self.__peso
    def set_peso(self, peso):
        self.__peso = peso
    peso = property(get_peso,set_peso)

    