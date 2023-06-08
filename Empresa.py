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

class Empresa(MetodosViajes):
    def __init__(self, barcos):
        self.__camiones = []
        for i in range(5):
            camion = Camion(i)
            self.__camiones.append(camion)
        for barco in barcos:
            self.__barcos.append(barco)
        
        # para puntos 3 y 4 de SE PIDE
        self.__barco_con_mas_km = None
        self.__barco_con_menos_km = None
        
        """
        Para punto 2 de se pide podriamos hacer esto:
        self.__contenedores = []
        
        si usamos esto para resolver el punto 2 podriamos hacer un metodo que recorra esta,
        y guarde y devuelva la que mas alto tenga el counter de su variable: 
        self.__cant_de_veces_comple_y_carga_unica
        
        Pero si usamos una lista de contenedores, para realizar o efectuar un viaje de un pedido
        habria que recorrer esta lista de contenedores a ver si esta disponible o no, y si tiene
        las caracteristicas necesarias como para llevarlo, y si ese no es el caso, pasar al
        siguiente de la lista.
        El problema con esto es que habria que reflexionar sobre el uso de excepciones en
        por ejemplo, cuando un contenedor basico no puede llevar una carga porque. Dado que, entiendo
        que si una de esas excepciones es catcheada, el programa finaliza ahi, por lo cual nunca llegaria
        a analizar el siguiente contenedor de la lista.
        
        Si no queremos usar esta opcion, habria que ver como hacer para resolver el punto 2 de SE PIDE.
        Y si usamos esta opcion, podriamos considerar raisear una excepcion cuando se termina de
        recorrer la lista el problema es que ahi no sabremos porque no podemos usar los contenedores.
        Aunque eso no esta tan mal, porque si pudiesemos, o si lo hariamos, tendriamos que ponernos a
        explicar el porque no podemos usar un contenedor para cada contenedor de la lista de contenedores. Y
        si tenemos mil contenedores puede llegar a ser algo tedioso e innecesario.
        """

    'Getters y Setters'
    def get_id(self):
        return self.__id
    
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

    
    def get_barco_con_mas_km(self):
        
        return self.__barco_con_mas_km
    
    def set_barco_con_mas_km(self, barcos):
        self.__barco_con_mas_km = barcos
    barco_con_mas_km = property(get_barco_con_mas_km,set_barco_con_mas_km)


    
    def get_barco_con_menos_km(self):
      
        return self.__barco_con_menos_km
    
    def set_barco_con_menos_km(self, barcos):
        self.__barco_con_menos_km = barcos
    __barco_con_menos_km = property(get_barco_con_menos_km,set_barco_con_menos_km)
    
    
    
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
    
    
    def actualizar_barco_trotamundo_o_sedentario(self):
        
        bmenos = self.get_barco_con_menos_km()
        bmas = self.get_barco_con_mas_km()
        
        for barco in self.get_barcos():
            # actualizo barco sedentario
            if barco.get_km_recorridos() < bmenos or bmenos.get_km_recorridos() == 0:
                self.set_barco_con_menos_km(barco)
            
            # actualizo barco trotamundo
            if barco.get_km_recorridos() > bmas:
                self.set_barco_con_mas_km(barco)
        
        return
    
                
           
    #El container que mayor cantidad de veces viajó completo con una única carga.
    def container_con_mas_viajes_con_una_carga(self):
        container_mas_viajes = Contenedor()
        aux = 0

        for barco in self.__barcos:

            for container in barco.get_contenedores():

                if container.get_cant_de_veces_comple_y_carga_unica() > aux:
                    aux = container.get_cant_de_veces_comple_y_carga_unica()
                    container_mas_viajes = container
        
        return container_mas_viajes