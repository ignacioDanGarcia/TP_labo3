
import random
from typing import List
from Cargas.Carga import Carga
from EmpresaDirectorio.TipoVehiculo import TipoVehiculo
from GenerarId import GenerarId

class Pedidos:
    def __init__(self, id, cargas: List[Carga], tipo_vehiculos: List[TipoVehiculo], distancias: List[int]):
        self.__id = id #GenerarId.generar_numeros_distintos()
        self.__cargas = cargas
        self.__tipo_vehiculos = tipo_vehiculos
        self.__contenedores = [] #necesitamos que el pedido tenga los containers asociados a las cargas
        self.__distancias = distancias
        self.__precio_final_pedido = 0
    
    'Getters y setters:'
    def get_tipo_vehiculos(self):
        return self.__tipo_vehiculos
    def set_tipo_vehiculos(self, tipo_vehiculos):
        self.__tipo_vehiculos = tipo_vehiculos
    tipo_vehiculos = property(get_tipo_vehiculos,set_tipo_vehiculos)
    
    def get_distancias(self):
        return self.__distancias
    def set_distancias(self, distancias):
        self.__distancias = distancias
    distancias = property(get_distancias,set_distancias)
    
    def get_precio_final_pedido(self):
        return self.__precio_final_pedido
    def set_precio_final_pedido(self, precio):
        self.__precio_final_pedido = precio
    precio_final_pedido = property(get_precio_final_pedido,set_precio_final_pedido)
    
    def get_contenedores(self):
        return self.__contenedores
    def set_contenedores(self, c):
        self.__contenedores = c
    contenedores = property(get_contenedores,set_contenedores)

    def get_necesita_transporte_camion(self):
        return self.__necesita_transporte_camion
    def set_necesita_transporte_camion(self, necesita_transporte_camion):
        self.__necesita_transporte_camion = necesita_transporte_camion
    necesita_transporte_camion = property(get_necesita_transporte_camion,set_necesita_transporte_camion)

    def get_id(self):
        return self.__id
    
    def get_retira_en_puerto(self):
        return self.__retira_en_puerto
    def set_retira_en_puerto(self, ret):
        self.__retira_en_puerto = ret
    retira_en_puerto = property(get_retira_en_puerto,set_retira_en_puerto)
    
    def get_cargas(self):
        return self.__cargas
    def set_cargas(self, cargas):
        self.__cargas.append(cargas)
    cargas = property(get_cargas,set_cargas)
    'Fin getters y setters'
    
    def get_cant_contenedores(self):
        cant = len(self.get_contenedores())
        return cant