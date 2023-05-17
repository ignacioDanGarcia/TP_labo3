from abc import ABC, abstractmethod
from Medidas_contenedores import Medidas

class Contenedor(ABC):
    

    def __init__(self, id, precio_transporte, mat_especial):
        self.__id = id
        self.__precio_transporte = precio_transporte #Cada contenedor define un precio base que se debe pagar para transportar carga
        self.__volumen_max = 0.0
        self.__peso_max = 0.0
        self.__medidas_interior = None
        self.__medidas_exterior = None
        self.__carga = None
        self.__mat_especial = mat_especial

        #algo hay que hacer con este punto:
        # Un contenedor sin características especiales no puede transportar material especial.
        #Creo que con un booleano de si es apto para material especial en el contructor podría ir este punto así 
    
    'Getters y Setters:'
    def get_id(self):
        return self.__id
    def set_id(self,id):
        self.__id = id
    id = property(get_id,set_id)
    
    def get_precio_transporte(self):
        return self.__precio_transporte
    def set_precio_transporte(self, p):
        self.__precio_transporte = p
    precio_transporte = property(get_precio_transporte,set_precio_transporte)
    
    def get_mat_especial(self):
        return self.__mat_especial
    def set_mat_especial(self, mat):
        self.__mat_especial = mat
    mat_especial = property(get_mat_especial,set_mat_especial)
    'mat especial es un booleano para diferencias si el container puede llevar una carga especial como explosivos.'

    def get_medidas_interior(self):
        return self.__medidas_interior
    def set_medidas_interior(self, m):
        self.__medidas_interior = m
    medidas_interior = property(get_medidas_interior,set_medidas_interior)
    
    
    
    def get_medidas_exterior(self):
        return self.__medidas_exterior
    def set_medidas_exterior(self, me):
        self.__medidas_exterior = me
    medidas_exterior = property(get_medidas_exterior,set_medidas_exterior)
    
    
    def get_id(self):
        return self.__id
    def set_id(self, id):
        self.__id = id
    id = property(get_id,set_id)
    
    
    def get_precio_transporte(self):
        return self.__precio_transporte
    def set_precio_transporte(self, p):
        self.__precio_transporte = p
    precio_transporte = property(get_precio_transporte,set_precio_transporte)
    
    
    def get_volumen_max(self):
        return self.__volumen_max
    def set_volumen_max(self, v):
        self.__volumen_max = v
    volumen_max = property(get_volumen_max,set_volumen_max)
    
    
    def get_peso_max(self):
        return self.__peso_max
    def set_peso_max(self,p):
        self.__peso_max = p
    peso_max = property(get_peso_max,set_peso_max)
    
    def get_carga(self):
        return self.__carga
    def set_carga(self, c):
        self.__carga = c
    carga = property(get_carga,set_carga)
    'Fin Getters y Setters'
    
    #Cualquier carga cuyas  medidas o peso supere lo definido en el container no podrá 
    # ser trasladada en el mismo.
    def verificar_carga(self, carga):
        no_supera_medidas = False
        no_supera_peso_max = False
        if self.medidas_interior.comparar_medidas(carga.get_medidas()):
            no_supera_medidas = True

        if carga.get_peso() < self.peso_max:
            no_supera_peso_max = True

        return no_supera_peso_max and no_supera_medidas

    
    def cargar(self, carga):
        if self.verificar_carga(carga):
            self.carga = carga
    
    def peso_contenedor(self):
        return self.carga.get_peso()