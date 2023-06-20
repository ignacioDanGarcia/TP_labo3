from Pedidos import Pedidos
from Cargas.Carga import Carga

from GenerarId import GenerarId


class Cliente:

    def __init__(self, id, apellido, nombre):
        self.__apellido = apellido
        self.__nombre = nombre
        self.__id = id # GenerarId.generar_numeros_distintos()
        self.__pedido = None
        self.__cargas = []
        
    
    'Getters y Setters:'
    def get_id(self):
        return self.__id
    def set_id(self,id):
        self.__id = id
    id = property(get_id, set_id)
    
    def get_apellido(self):
        return self.__apellido
    def set_apellido(self,a):
        self.__apellido = a
    apellido = property(get_apellido,set_apellido)
    
    def get_nombre(self):
        return self.__nombre
    def set_nombre(self,nombre):
        self.__nombre = nombre
    nombre = property(get_nombre,set_nombre)
    
    
    # Variable de cargas para poder armarme un pedido con la cantidad de cargas que se le cante al cliente
    def armar_una_carga(self, medidas, peso, mat_especial):
        carga = Carga(medidas, peso, mat_especial)
        return carga
    def get_cargas(self):
        return self.__cargas
    def agregar_carga(self,carga):
        self.__cargas.append(carga)
    cargas = property(get_cargas,agregar_carga)
    
    
    def get_pedido(self):
        return self.__pedido
    # a set pedido le tengo que pasar los datos de una carga para que lo pueda armar
    def set_pedido(self, retiraEnPuerto, conteneCompleto):
        
        pedido = Pedidos(retiraEnPuerto, conteneCompleto, self.get_cargas())
        
        self.__pedido = pedido
    pedido = property(get_pedido,set_pedido)
    
    """
    a la empresa le tiene que llegar un cliente con el pedido cargado, por lo cual,
    en los tests lo que podriamos hacer es instanciar un objeto cliente, con ese cliente
    instanciar un objeto pedido, con ese pedido instanciar un objeto carga, guardarlo en
    pedido, y guardar el pedido en cliente, y ahi pasarle por parametro a el metodo de
    empresa al cliente
    """
    