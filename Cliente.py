# este es un comentario a ver si me funciona la branch correctamente
from Pedidos import Pedidos
from Carga import Carga


class Cliente:
    def __init__(self, apellido, nombre, id):
        self.__apellido = apellido
        self.__nombre = nombre
        self.__id = id
        self.__pedido = None
    
    'Getters y Setters:'
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
    
    def get_id(self):
        return self.__id
    def set_id(self,id):
        self.__id = id
    id = property(get_id,set_id)
    
    def get_pedido(self):
        return self.__pedido
    
    # a set pedido le tengo que pasar los datos de una carga para que lo pueda armar
    def set_pedido(self, medidas, peso, mat_especial, retiraEnPuerto, conteneCompleto):
        carga = Carga(medidas, peso, mat_especial)
        
        pedido = Pedidos(retiraEnPuerto, conteneCompleto, carga)
        
        self.__pedido = pedido
    pedido = property(get_pedido,set_pedido)
    
    """
    a la empresa le tiene que llegar un cliente con el pedido cargado, por lo cual,
    en los tests lo que podriamos hacer es instanciar un objeto cliente, con ese cliente
    instanciar un objeto pedido, con ese pedido instanciar un objeto carga, guardarlo en
    pedido, y guardar el pedido en cliente, y ahi pasarle por parametro a el metodo de
    empresa al cliente
    """
    