from Medidas import Medidas
from TasadorDeCargas import TasadorDeCargas

class Carga:

    def __init__(self, medidas, peso, material_especial):

        self.__medidas = medidas
        self.__peso = peso
        self.__material_especial = material_especial
        #falta id de carga, y sino sacar el getter
    
    'Getters y setters'
    def get_id(self):
        return self.__id
    
    def get_medidas(self):
        return self.__medidas
    def set_medidas(self,m):
        self.__medidas = m
    medidas = property(get_medidas,set_medidas)
    

    
    def get_peso(self):
        return self.__peso
    def set_peso(self, peso):
        self.__peso = peso
    peso = property(get_peso,set_peso)
    
    def get_material_especial(self):
        return self.__material_especial
    def set_material_especial(self,mat):
        self.__material_especial = mat
    material_especial = property(get_material_especial,set_material_especial)
    
    def get_volumen(self):
        volumen = self.medidas.get_alto() * self.medidas.get_ancho() * self.medidas.get_largo()
        return volumen
    
    