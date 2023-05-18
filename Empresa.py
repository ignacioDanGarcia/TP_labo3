from BarcosDirectorio.Barcos import Barco
from Camion import Camion
from Contenedores import Contenedor
from Pedidos import Pedidos
from MetodosViajes import MetodosViajes
# corregir directorio de estas dos
from Excepciones.exceptions import *

import random

"""
Esta clase es la que deberia controlar todo calculo. En el diagrama no la habiamos hecho.
Pero para definir precios de viajes, calcular kilometros, aceptar y gestionar pedidos, creo
que de eso se deberia encargar esta clase.
"""

class Empresa:
    def __init__(self, barcos):
        self.__camiones = []
        for i in range(5):
            camion = Camion(i)
            self.__camiones.append(camion)
        self.__barcos = barcos
        # barcos seria una lista
        # para instanciar la empresa le paso como parametro la lista de barcos y camiones
        
    def get_barcos(self):
        return self.__barcos
    def set_barcos(self, barcos):
        self.__barcos = barcos
    barcos = property(get_barcos,set_barcos)
    
    def get_camiones(self):
        return self.__camiones
    def set_camiones(self, camiones):
        self.__camiones = camiones
    camiones = property(get_camiones,set_camiones)
    
    def moduloGPS(self):
        """
        para "calcular" distancias
        segun la tabla de precios las distancias minimas estan abajo de 100, y las maximas arriba de 10 mil
        por eso puse que me devuelva una distancia en km del 1 al 20 mil y fue
        
        Tratemos de ignorar las sedes como tal porque si tenemos que guardar las sedes y la cantidad que tiene
        cada una sobre la otra vamos a estar mil años
        """
        
        return random.randint(1, 20000)
    
    def camion_disponible(self):          
        for camion in self.camiones:
            if (camion.disponible):
                #segun la teoria, esto afecta a la lista de empresa de self.camiones en cualquier parte del codigo
                camion.disponible = False
                return camion
        # falta ver donde se catchea esta excepcion (sacar este comentario cuando ya este)
        raise No_hay_camiones_disponibles("En este momento no hay camiones disponibles")
    
    
        
    
    
    def definirPrecioViaje(Camion, contenedor):
        #peso por transportar de cada contenedor dentro de un barco + el precio de la carga
        pass
    def definirPrecioViaje(Barco, listaContenedores):
        #implementacion
        pass

    def misma_carga_mas_veces(self):
        # falta implementar
        pass