from abc import ABC, abstractmethod
from Medidas import Medidas
from Excepciones.exceptions import contenedor_no_puede_llevar_carga, medidas_incorrectas, no_existe_carga, distancia_incorrecta
from generar_id import generar_id

class Contenedor(ABC):
    gen = generar_id()

    def __init__(self, mat_especial):
        
        self.__id = Contenedor.gen.generar_numeros_distintos()
        self.__precio_adicional = 0 #Cada contenedor define un precio base que se debe pagar para transportar carga
        self.__volumen_max = 0.0
        self.__peso_max = 0.0
        self.__medidas_interior = None
        self.__medidas_exterior = None
        self.__cargas = []
        self.__mat_especial = mat_especial
        self.__disponible = True
        self.__cant_de_veces_comple_y_carga_unica = 0

        #algo hay que hacer con este punto:
        # Un contenedor sin características especiales no puede transportar material especial.
        #Creo que con un booleano de si es apto para material especial en el contructor podría ir este punto así 
    
    'Getters y Setters:'
    
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
    
    def get_precio_adicional(self):
        return self.__precio_adicional
    def set_precio_adicional(self, p):
        self.__precio_adicional = p
    precio_adicional = property(get_precio_adicional,set_precio_adicional)
    
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
        return self.__cargas
    def set_carga(self, c):
        self.__cargas.append(c)
    cargas = property(get_carga,set_carga)
    'Fin Getters y Setters'
    
    #Cualquier carga cuyas  medidas o peso supere lo definido en el container no podrá 
    # ser trasladada en el mismo.
    def verificar_carga(self, carga):
        # este metodo la usa esta misma clase
        
        no_supera_medidas = False
        no_supera_peso_max = False
        no_supera_vol_max = False
        try:            
            if self.medidas_interior.comparar_medidas(carga.get_medidas()):
                no_supera_medidas = True

            if carga.get_peso() < self.get_peso_max():
                no_supera_peso_max = True

            if carga.get_volumen() < self.get_volumen_max():
                no_supera_vol_max = True
            
            if (no_supera_peso_max and no_supera_medidas and no_supera_vol_max):
                return True
        except medidas_incorrectas as e:
            print(str(e))
        
            #excepcion catcheada en calcular_precio_adicional de esta misma clase
        raise contenedor_no_puede_llevar_carga("La carga no puede ser transportada por este contenedor")

    def calcular_precio_adicional(self, distancia):
        # distancia se llena con un num del moduloGPS
        # este metodo la usaria la clase empresa
        try:
            carga = self.get_carga()
            if carga is None:
                # excepcion catcheada en esta misma funcion, segun lo que encontre se podia
                raise no_existe_carga("No existe una carga")
            
            if distancia < 100 and self.verificar_carga() and self.medidas.comparar_medidas(carga.medidas):
                self.set_precio_adicional(200000)
            elif distancia < 100 and self.verificar_carga() and not self.medidas.comparar_medidas(carga.medidas):
                self.set_precio_adicional(1000 * (carga.peso // 100))
            elif distancia < 1000 and self.verificar_carga() and self.medidas.comparar_medidas(carga.medidas):
                self.set_precio_adicional(210000)
            elif distancia < 1000 and self.verificar_carga() and not self.medidas.comparar_medidas(carga.medidas):
                self.set_precio_adicional(1100 * (carga.peso // 100))
            elif distancia < 10000 and self.verificar_carga() and self.medidas.comparar_medidas(carga.medidas):
                self.set_precio_adicional(230000)
            elif distancia < 10000 and self.verificar_carga() and not self.medidas.comparar_medidas(carga.medidas):
                self.set_precio_adicional(1150 * (carga.peso // 100))
            elif distancia > 10000 and self.verificar_carga() and self.medidas.comparar_medidas(carga.medidas):
                self.set_precio_adicional(250000)
            elif distancia > 10000 and self.verificar_carga() and not self.medidas.comparar_medidas(carga.medidas):
                self.set_precio_adicional(1500 * (carga.peso // 100))
            
        except contenedor_no_puede_llevar_carga as e:
            print(str(e))
        except no_existe_carga as e2:
            print(str(e2))
        else:
            if (distancia is None or isinstance(distancia, int)):
                # falta ver donde se catchea esta excepcion (sacar este comentario cuando ya este)
                raise distancia_incorrecta("La distancia especificada no cumplen con ningún caso")    
            
            precio = (self.get_precio_adicional() + self.carga.get_precio()) 

            return precio
    
    """
    esto creo que no sirve, osea para esto esta el set_carga
    def cargar(self, carga):
        if self.verificar_carga(carga):
            self.carga = carga
    """
    def peso_contenedor(self):
        return self.carga.get_peso()