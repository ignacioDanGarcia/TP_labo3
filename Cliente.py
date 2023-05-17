# este es un comentario a ver si me funciona la branch correctamente

class Cliente:
    def __init__(self, apellido, nombre, id):
        self.__apellido = apellido
        self.__nombre = nombre
        self.__id = id
    
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
    