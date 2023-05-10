from Vehiculos import Barcos, Camion
from Contenedores import Contenedores
from Pedidos import Pedidos
from MetodosViajes import MetodosViajes

import random

"""
Esta clase es la que deberia controlar todo calculo. En el diagrama no la habiamos hecho.
Pero para definir precios de viajes, calcular kilometros, aceptar y gestionar pedidos, creo
que de eso se deberia encargar esta clase.
"""
    

class Empresa:
    def __init__(self):
        self.cantCamiones = 5
        self.camiones = [1, 2, 3, 4, 5]
        #barcos ilimitados
        
        
    def moduloGPS():
        """
        para "calcular" distancias
        segun la tabla de precios las distancias minimas estan abajo de 100, y las maximas arriba de 10 mil
        por eso puse que me devuelva una distancia en km del 1 al 20 mil y fue
        
        Tratemos de ignorar las sedes como tal porque si tenemos que guardar las sedes y la cantidad que tiene
        cada una sobre la otra vamos a estar mil años
        """
        
        return random.randint(1, 20000)
    
    def definirPrecioViaje(Camion, contenedor):
        #implementacion
        pass
    def definirPrecioViaje(Barco, listaContenedores):
        #implementacion
        pass

    def prueba2(self):
        #otra prueba
        pass