from abc import ABC, abstractmethod
from Carga import Carga
from Medidas import Medidas
from Excepciones.exceptions import contenedor_no_puede_llevar_carga, el_contenedor_basico_no_puede_mat_especial, medidas_incorrectas, no_existe_carga, distancia_incorrecta
from GenerarId import GenerarId
from TasadorDeCargas import TasadorDeCargas

from .Estados.EstadoContenedorAbstracta import EstadoContenedorAbstracta
from .Estados.EstadoMenor100 import EstadoMenor100
from .Estados.EstadoMenor1000 import EstadoMenor1000
from .Estados.EstadoMenor10000 import EstadoMenor10000
from .Estados.EstadoMas10000 import EstadoMas10000
from ModuloGPS import ModuloGPS

class Contenedor():

    def __init__(self, material_especial):
        gen = GenerarId()
        self.__id = gen.generar_numeros_distintos()
        self.__tipo = ''
        tas = TasadorDeCargas()
        p = tas.setear_precio_carga()
        self.__precio_transporte_base = p
        self.__volumen_max = 0.0
        self.__peso_max = 0.0
        self.__medidas_interior = None
        self.__medidas_exterior = None
        self.__cargas = []
        self.__material_especial = material_especial
        self.__disponible = True
        self.__cant_de_veces_comple_y_carga_unica = 0
        self.__estado = None

        #algo hay que hacer con este punto:
        # Un contenedor sin características especiales no puede transportar material especial.
        #Creo que con un booleano de si es apto para material especial en el contructor podría ir este punto así 
    
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
    
    #-------------------------------ESTA RESPONSABILIDAD FUE MOVIDA AL MANEJADOR DE CARGAS -------------------------------------------------------------------
    #Cualquier carga cuyas  medidas o peso supere lo definido en el container no podrá 
    # ser trasladada en el mismo.
    '''def verificar_carga(self, carga):
        # este metodo la usa esta misma clase
        
        try:
            if "basico" in self.tipo.lower() and carga.get_material_especial() != None: #En vez de que vea si es instancia de barco_basico_abstracto lo vemos por el tipo de barco
                raise el_contenedor_basico_no_puede_mat_especial("Un contenedor basico no puede cargar un material especial")

            if self.medidas_interior.comparar_medidas(carga.get_medidas()) and \
                    carga.get_peso() <= self.get_peso_max() and \
                    carga.get_volumen() <= self.get_volumen_max():
                return True
            raise contenedor_no_puede_llevar_carga("La carga no puede ser transportada por este contenedor")
        except medidas_incorrectas as e:
            raise contenedor_no_puede_llevar_carga(str(e))'''
        

    
    def calcular_precio(self, distancia):
        # distancia se llena con un num del moduloGPS
        # este metodo la usaria la clase empresa
        try:
            if (distancia is None or isinstance(distancia, int) is False):
                # excepcion catcheada en esta misma funcion, segun lo que encontre se podia
                raise distancia_incorrecta("La distancia especificada no cumplen con ningún caso")    
            
            cargas = self.get_cargas()
            if cargas is None:
                # excepcion catcheada en esta misma funcion, segun lo que encontre se podia
                raise no_existe_carga("No existe una carga")
            
            estado = EstadoMenor100(self)
            # esto es nada mas para cambiar el precio por distancia, que si al principio es uno siempre va a ser ese
            # no importa que carga le metas, siempre va al mismo lado el contenedor
            # IMPORTANTE EN METODO VIAJAR EMPRESA SETEAR ESTADO CONTENEDOR A NONE
            precio_aux = 0
            # Ver si en este if capaz se puede poner un estado.transicion(distancia) en lugar de todo esto
            for carga in cargas:
                #if estado is None or (estado is not None and not estado.condicion(distancia)):
                #    self.set_estado(self.buscar_estado(distancia, carga))
                #estado = self.get_estado()
                precio_aux += estado.transicion(distancia, carga)
                
                # aca el contenedor ya va a estar lleno o con pedido listo
                
            
            
            
            precio_aux += self.get_precio_transporte_base()
            
            return precio_aux
            
            
            
        except contenedor_no_puede_llevar_carga as e:
            print(str(e))
        except no_existe_carga as e2:
            print(str(e2))
        except distancia_incorrecta as e:
            print(str(e))
            
            
    
    
    ''' esto creo que no sirve, osea para esto esta el set_carga
    def cargar(self, carga):
        if self.verificar_carga(carga):
            self.carga = carga
    '''
    