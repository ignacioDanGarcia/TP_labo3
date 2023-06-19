from Medidas import Medidas
from Cargas.Categorias import Categoria
class Carga:

    def __init__(self, medidas : Medidas, peso, categoria : Categoria):

        self.__medidas = medidas
        self.__peso = peso
        self.__categoria = categoria
    
    'Getters y setters'
        
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
    
    def get_categoria(self):
        return self.__categoria
    def set_categoria(self,categoria):
        self.__categoria = categoria
    material_especial = property(get_categoria,set_categoria)
    
    def get_volumen(self):
        volumen = self.medidas.get_alto() * self.medidas.get_ancho() * self.medidas.get_largo()
        return volumen
    
    
    'Fin getters y setters'