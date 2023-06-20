
import random
from typing import List
from Cargas.Carga import Carga
from GenerarId import GenerarId

class Pedidos:
    def __init__(self, id, cargas: List[Carga], distancia, puerta_a_puerta):
        self.__id = id #GenerarId.generar_numeros_distintos()
        self.__puerta_a_puerta = puerta_a_puerta #bool
        self.__cargas = cargas
        self.__contenedores_ids = [] 
        self.__distancia = distancia
        self.__precio_final_pedido = 0
    
    'Getters y setters:'    
    def get_puerta_a_puerta(self):
        return self.__puerta_a_puerta
    def set_puerta_a_puerta(self, puerta_a_puerta):
        self.__puerta_a_puerta = puerta_a_puerta
    puerta_a_puerta = property(get_puerta_a_puerta,set_puerta_a_puerta)
    
    def get_distancia(self):
        return self.__distancia
    def set_distancia(self, distancia):
        self.__distancia = distancia
    distancia = property(get_distancia,set_distancia)
    
    def get_precio_final_pedido(self):
        return self.__precio_final_pedido
    def set_precio_final_pedido(self, precio):
        self.__precio_final_pedido = precio
    precio_final_pedido = property(get_precio_final_pedido,set_precio_final_pedido)
    
    def get_contenedores_ids(self):
        return self.__contenedores_ids
    def set_contenedores_ids(self, c):
        self.__contenedores_ids = c
    contenedores_ids = property(get_contenedores_ids,set_contenedores_ids)

    def get_necesita_transporte_camion(self):
        return self.__necesita_transporte_camion
    def set_necesita_transporte_camion(self, necesita_transporte_camion):
        self.__necesita_transporte_camion = necesita_transporte_camion
    necesita_transporte_camion = property(get_necesita_transporte_camion,set_necesita_transporte_camion)

    def get_id(self):
        return self.__id
    def set_id(self, id):
        self.__id = id
    id = property(get_id,set_id)
    
    def get_cargas(self):
        return self.__cargas
    def set_cargas(self, cargas):
        self.__cargas.append(cargas)
    cargas = property(get_cargas,set_cargas)
    'Fin getters y setters'
    
    def get_cant_contenedores(self):
        cant = len(self.get_contenedores_ids())
        return cant
    
    def agregar_contenedor(self, id):
        self.__contenedores_ids.append(id)