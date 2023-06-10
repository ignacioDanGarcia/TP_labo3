from Carga import Carga
import random
from GenerarId import GenerarId

class Pedidos:
    def __init__(self, retira_en_puerto, contenedor_completo, cargas, necesita_transporte_camion):
        gen = GenerarId()
        self.__retira_en_puerto = retira_en_puerto #bool
        self.__contenedor_completo = contenedor_completo #bool
        self.__id = gen.generar_numeros_distintos()
        self.__cargas = cargas
        self.__containers = None #necesitamos que el pedido tenga los containers asociados a las cargas
        self.__necesita_transporte_camion = necesita_transporte_camion #bool si es False no sumamos el precio de 
                                                       #transporte carga x camion en el costo total del pedido
        'pruebas de git'
    
    'Getters y setters:'

    
    def get_containers(self):
        return self.__containers
    
    def get_cant_containers(self):
        cant = len(self.get_containers)
        return cant

    def get_necesita_transporte_camion(self):
        return self.__necesita_transporte_camion

    def get_id(self):
        return self.__id
    
    def get_retira_en_puerto(self):
        return self.__retira_en_puerto
    def set_retira_en_puerto(self, ret):
        self.__retira_en_puerto = ret
    retira_en_puerto = property(get_retira_en_puerto,set_retira_en_puerto)

    def get_contenedor_completo(self):
        return self.__contenedor_completo
    def set_contenedor_completo(self, completo):
        self.__contenedor_completo = completo
    contenedor_completo = property(get_contenedor_completo,set_contenedor_completo)

    
    def get_cargas(self):
        return self.__cargas
    def set_cargas(self, cargas):
        self.__cargas.append(cargas)
    cargas = property(get_cargas,set_cargas)
        