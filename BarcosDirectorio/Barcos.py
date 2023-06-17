from BarcosDirectorio.Cargable import Cargable
from abc import ABC, abstractmethod
from GenerarId import GenerarId
from Interfaces.ViajeraInterfaz import ViajeraInterfaz

class Barco(Cargable, ABC):

    def __init__(self, peso_max, cant_contenedores_max, nombre):
        self.__id = GenerarId.generar_numeros_distintos()
        self.__disponible = True
        self.__peso_max = peso_max
        self.__cant_contenedores_max = cant_contenedores_max
        self.__kmRecorridos = 0
        self.__contenedores = []
        self.__nombre = nombre
        
        
        #CONTAINER MATERIAL ESPECIAL (explosivos, desechos químicos o radioactivos) 
        # sólo puede ser transportado por un barco diseñado para tal fin.
        #los barcos de tipo básico, soportan contenedores con medidas del tipo basico
        # los barcos soportan cualquier contenedor cuyas medidas sean mayores a las de un contenedor básico. 
    
    'Getters y setters'
    def get_id(self):
        return self.__id
    
    def get_nombre(self):
        return self.__nombre
    def set_nombre(self,nombre):
        self.__nombre = nombre
    nombre = property(get_nombre,set_nombre)
    
    def get_peso_max(self):
        return self.__peso_max
    def set_peso_max(self,peso):
        self.__peso_max = peso
    peso_max = property(get_peso_max,set_peso_max)
    
    def get_cant_contenedores_max(self):
        return self.__cant_contenedores_max 
    def set_cant_contenedores_max(self, cant):
        self.__cant_contenedores_max = cant
    cant_contenedores_max = property(get_cant_contenedores_max,set_cant_contenedores_max)
    
    def get_disponible(self):
        return self.__disponible
    def set_disponible(self,dispo):
        self.__disponible = dispo
    disponible = property(get_disponible,set_disponible)
    
    def get_km_recorridos(self):
        return self.__kmRecorridos
    def set_km_recorridos(self, kms):
        self.__kmRecorridos = kms
    km_recorridos = property(get_km_recorridos,set_km_recorridos)
    
    def get_contenedores(self):
        return self.__contenedores
    def set_contenedores(self,contenedor):
        self.contenedores.append(contenedor)
    contenedores = property(get_contenedores,set_contenedores)
    'Fin getters y Setters'
    
    
    def obtener_peso_actual(self):
        peso = 0
        for contenedor in self.contenedores:
            peso += contenedor.peso_contenedor()
        return peso
    