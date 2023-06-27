from BarcosDirectorio.Barcos import Barco
from Camion import Camion
from ContenedoresDirectorio.Contenedores import Contenedor
from Excepciones.exceptions import *

from typing import List


class EmpresaData():
    def __init__(self, barcos: List[Barco], camiones: List[Camion], contenedores: List[Contenedor]):
        self.__camiones = camiones
        self.__barcos = barcos
        self.__contenedores = contenedores
        self.__barco_con_mas_km = None
        self.__barco_con_menos_km = None
        



    'Getters y Setters'
    def get_camiones(self):
        return self.__camiones
    def set_camiones(self, camiones):
        self.__camiones = camiones
    camiones = property(get_camiones,set_camiones)
    
    def get_barcos(self):
        return self.__barcos
    def set_barcos(self, barcos):
        self.__barcos = barcos
    barcos = property(get_barcos,set_barcos)

    def get_contenedores(self):
        return self.__contenedores
    def set_contenedores(self, contenedores):
        self.__contenedores = contenedores
    contenedores = property(get_contenedores,set_contenedores)

    def get_barco_con_mas_km(self):
        return self.__barco_con_mas_km
    def set_barco_con_mas_km(self, barcos):
        self.__barco_con_mas_km = barcos
    barco_con_mas_km = property(get_barco_con_mas_km,set_barco_con_mas_km)
    
    def get_barco_con_menos_km(self):
        return self.__barco_con_menos_km
    def set_barco_con_menos_km(self, barcos):
        self.__barco_con_menos_km = barcos
    barco_con_menos_km = property(get_barco_con_menos_km,set_barco_con_menos_km)
    'Fin Getters y Setters'
    
    
    'Vehiculos disponibles'
    # una vez que se carga un contenedor en un barco se debe setear la distancia del barco como la distancia del pedido
    
    def get_barcos_disponible_misma_distancia(self, distancia):
        barcos_con_misma_distancia = []

        for barco in self.get_barcos():
            if barco.get_disponible():
                if barco.get_distancia() == distancia:
                    barcos_con_misma_distancia.append(barco)

        return barcos_con_misma_distancia

    def get_barco_disponible_distancia_cero(self):
        for barco in self.get_barcos():
            if barco.get_disponible():
                if barco.get_distancia() == 0:
                    return barco
        return None
    
    
    def devolver_camiones_disponibles(self) -> List[Camion]:
        camiones_disponibles = []
        for camion in self.get_camiones():
            if camion.get_disponible():
                camiones_disponibles.append(camion)

        return camiones_disponibles

    
    def get_contenedores_disponibles(self):
        conts = []
        for cont in self.get_contenedores():
            if (cont.get_disponible()):
                conts.append(cont)
        return conts
    
    def actualizar_barco_con_mas_y_con_menos_km(self):
        #Podríamos cambiar este nombre no? Es raro
        bmenos = self.get_barco_con_menos_km()
        bmas = self.get_barco_con_mas_km()
        
        for barco in self.get_barcos():
            if bmenos == None:
                bmenos = barco
            if bmas == None:
                bmas = barco
            # actualizo barco sedentario
            if barco.get_km_recorridos() < (bmenos.get_km_recorridos()):
                self.set_barco_con_menos_km(barco)
                bmenos = barco
            
            # actualizo barco trotamundo
            if barco.get_km_recorridos() > bmas.get_km_recorridos():
                self.set_barco_con_mas_km(barco)
                bmas = barco
        
        return
    
                
           
    # El contenedor que mayor cantidad de veces viajó completo con una única carga
    def container_con_mas_viajes_con_una_carga(self):
        aux = 0
        for contenedor in self.get_contenedores():
            if contenedor.get_cant_de_veces_comple_y_carga_unica() > aux:
                aux = contenedor.get_cant_de_veces_comple_y_carga_unica()
                contenedor_mas_viajes = contenedor
        
        return contenedor_mas_viajes
    
    #este metodo lo usa la empresaEnvios, actualiza en array de contenedores de la empresa
    #cuando un contenedor ya se entrego este vacia la carga
