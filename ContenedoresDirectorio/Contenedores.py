
from Cargas.Carga import Carga
from Medidas import Medidas


class Contenedor():

    def __init__(self, id, material_especial):
        #Si el container True el material_especial es que va a poder cargar contenidos con caracteristicas especiales, es decir, químicos.
        
        self.__id = id # GenerarId.generar_numeros_distintos()
        self.__tipo = ''
        self.__precio_transporte_base = 0 
        self.__volumen_max = 0.0
        self.__peso_max = 0.0
        self.__medidas_interior = None
        self.__medidas_exterior = None
        self.__cargas = [] 
        self.__material_especial = material_especial
        self.__disponible = True
        self.__cant_de_veces_comple_y_carga_unica = 0
        self.__estado = None
 
    
    'Getters y Setters:'
    def set_estado(self, estado):
        self.__estado = estado
    def get_estado(self):
        return self.__estado
    estado = property(get_estado,set_estado)

    def set_tipo(self, tipo):
        self.__tipo = tipo
    def get_tipo(self):
        return self.__tipo
    tipo = property(get_tipo,set_tipo)
    
    def get_id(self):
        return self.__id
    
    def get_cant_de_veces_comple_y_carga_unica(self):
        return self.__cant_de_veces_comple_y_carga_unica
    
    def COUNTER_cant_de_veces_comple_y_carga_unica(self):
        # en otra funcion habria que hacer preguntar si el contenedor esta lleno en medidas, y tiene una sola carga, y ahi ejecutar este
        self.__cant_de_veces_comple_y_carga_unica += 1
    cant_de_veces_comple_y_carga_unica = property(get_cant_de_veces_comple_y_carga_unica,COUNTER_cant_de_veces_comple_y_carga_unica)
    
    def get_disponible(self):
        return self.__disponible
    def set_disponible(self,dispo):
        self.__disponible = dispo
    disponible = property(get_disponible,set_disponible)
    
    def get_precio_transporte_base(self):
        return self.__precio_transporte_base
    def set_precio_transporte_base(self, precio):
        self.__precio_transporte_base = precio
    precio_transporte_base = property(get_precio_transporte_base,set_precio_transporte_base)
    
    def get_material_especial(self):
        return self.__material_especial
    def set_material_especial(self, mat):
        self.__material_especial = mat
    material_especial = property(get_material_especial,set_material_especial)

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
    
    def get_cargas(self):
        return self.__cargas
    cargas = property(get_cargas)
    'Fin Getters y Setters'
    
    def peso_contenedor(self):
        peso = 0
        for carga in self.cargas: 
            peso+= carga.get_peso()
        return peso
    
