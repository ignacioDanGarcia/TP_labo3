from Medidas import Medidas
from Cargas.Categorias import Categoria
class Carga:

    def __init__(self, medidas : Medidas, peso, categoria : Categoria):
        self.__medidas = medidas
        self.__peso = peso
        self.__categoria = categoria
        self.__id = 0 #Cuando tomamos un pedido seteamos el id de la carga en EmpresaDeposito cuándo cargamos un contenedor. Vinculamos la carga con el id del pedido.
    
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
    
    def get_id(self):
        return self.__id
    def set_id(self,id):
        self.__id = id
    id = property(get_id,set_id)
    'Fin getters y setters'
    
    def get_volumen(self):
        volumen = self.medidas.get_alto() * self.medidas.get_ancho() * self.medidas.get_largo()
        return volumen