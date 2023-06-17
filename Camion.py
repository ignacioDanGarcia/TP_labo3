from Interfaces.ViajeraInterfaz import ViajeraInterfaz
from GenerarId import GenerarId

class Camion():
    def __init__(self, id):
        self.__costo = 20000
        self.__disponible = True #si lo instancias es porque no tiene nada
        self.__id = GenerarId.generar_numeros_distintos()
        self.__contenedor = None
    
    'Getters y setters:'
    def get_id(self):
        return self.__id
    def set_id(self,id):
        self.__id = id
    id = property(get_id,set_id)
    
    def get_costo(self):
        return self.__costo
    def set_costo(self,costo):
        self.__costo = costo
    costo = property(get_costo,set_costo)

    def get_disponible(self):
        return self.__disponible
    def set_disponible(self,d):
        self.__disponible = d
    disponible = property(get_disponible,set_disponible)
    
    def get_contenedor(self):
        return self.__contenedor
    def set_contenedor(self,cont):
        self.__contenedor = cont
    contenedor = property(get_contenedor,set_contenedor)
    
    # El metodo de la interfaz
    def viajar(self):
        print("El camion entrego el pedido")
        self.set_disponible(True)
        self.set_contenedor(None)