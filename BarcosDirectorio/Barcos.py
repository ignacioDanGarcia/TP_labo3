from BarcosDirectorio.Cargable import Cargable
from abc import ABC, abstractmethod
from GenerarId import GenerarId
from Interfaces.ViajeraInterfaz import ViajeraInterfaz
from BarcosDirectorio.SistemasNavegacion.AMotor import AMotor
from Excepciones.exceptions import CombustibleInsuficienteException, tiempo_incorrecto
from ModuloGPS import ModuloGPS

class Barco(Cargable, ABC):

    def __init__(self, id, peso_max, cant_contenedores_max, combustible_maximo, tipo_barco = None, sensor_viento = None ):
        self.__id = id # GenerarId.generar_numeros_distintos()
        self.__disponible = True
        self.__peso_max = peso_max
        self.__cant_contenedores_max = cant_contenedores_max
        self.__tipo_barco = tipo_barco
        self.__sensor_viento = sensor_viento
        
        self.__kmRecorridos = 0
        self.__contenedores = []        
        self.__combustible_maximo = combustible_maximo 
        self.__combustible_actual = combustible_maximo
        self.__sistema_navegacion = AMotor(self)
        self.__gasto_por_hora = 6
        self.__combustible_gastado = 0
        self.__distancia = 0

    
    'Getters y setters'
    def get_id(self):
        return self.__id
    def set_id(self, id):
        self.__id = id
    id = property(get_id, set_id)
    
    def get_disponible(self):
        return self.__disponible
    def set_disponible(self,dispo):
        self.__disponible = dispo
    disponible = property(get_disponible,set_disponible)
    
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
    
    def get_tipo_barco(self):
        return self.__tipo_barco
    def set_tipo_barco(self,tipo_barco):
        self.__tipo_barco = tipo_barco
    tipo_barco = property(get_tipo_barco,set_tipo_barco)    
    
    def get_sensor_viento(self):
        return self.__sensor_viento
    def set_sensor_viento(self,sensor_viento):
        self.__sensor_viento = sensor_viento
    sensor_viento = property(get_sensor_viento,set_sensor_viento)
    
    
    
    def get_km_recorridos(self):
        return self.__kmRecorridos
    def set_km_recorridos(self, kms):
        self.__kmRecorridos = kms
    km_recorridos = property(get_km_recorridos,set_km_recorridos)
    
    def get_contenedores(self):
        return self.__contenedores
    def set_contenedores(self,contenedor):
        self.__contenedores = contenedor
    contenedores = property(get_contenedores,set_contenedores)
    
    def get_combustible_maximo(self):
        return self.__combustible_maximo
    def set_combustible_maximo(self,c):
        self.__combustible_maximo = c
    combustible_maximo = property(get_combustible_maximo,set_combustible_maximo)
    
    def get_combustible_actual(self):
        return self.__combustible_actual
    def set_combustible_actual(self,c):
        self.__combustible_actual = c
    combustible_actual = property(get_combustible_actual,set_combustible_actual)
    
    def get_sistema_navegacion(self):
        return self.__sistema_navegacion
    def set_sistema_navegacion(self,sistema):
        self.__sistema_navegacion = sistema
    sistema_navegacion = property(get_sistema_navegacion,set_sistema_navegacion) 
    
    def get_gasto_por_hora(self):
        return self.__gasto_por_hora
    def set_gasto_por_hora(self, g):
        self.__gasto_por_hora = g
    gasto_por_hora = property(get_gasto_por_hora,set_gasto_por_hora)
    
    def get_combustible_gastado(self):
        return self.__combustible_gastado
    def set_combustible_gastado(self,combustible):
        self.__combustible_gastado = combustible
    combustible_gastado = property(get_combustible_gastado,set_combustible_gastado)
    
    def get_distancia(self):
        return self.__distancia
    def set_distancia(self,distancia):
        self.__distancia = distancia
    distancia = property(get_distancia,set_distancia)
    'Fin getters y Setters'
    
    
    def obtener_peso_actual(self):
        peso = 0
        for contenedor in self.contenedores:
            peso += contenedor.peso_contenedor()
        return peso
    
    def navegar(self, modulo_gps :ModuloGPS): #Modulo gps
        
        modulo_gps.check_valores()
        horas = modulo_gps.calcular_tiempo()
        for hora in range(horas):
            if self.sensor_viento != None:
                self.sensor_viento.medir_viento_favorable(self)
            self.sistema_navegacion.navegar(1)
        self.set_km_recorridos(self.get_km_recorridos() + modulo_gps.calcular_distancia())
        
    def puede_navegar(self, modulo_gps :ModuloGPS):
        modulo_gps.check_valores()
        horas = modulo_gps.calcular_tiempo()
        gastonafta = self.get_gasto_por_hora() * horas
        
        if gastonafta > self.get_combustible_actual():
           raise CombustibleInsuficienteException("No alcanza el combustible. No es recomendado hacer este viaje.")
        return True
    
    
    #Estos dos métodos se usarían juntos, primero el puede_navegar para que levante alguna exception y luego el navegar. Si no podemos meterlo adentro de navegar pero estaría
    #revisando muchas veces los gastos.