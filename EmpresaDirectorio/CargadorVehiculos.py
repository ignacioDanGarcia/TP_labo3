from typing import List
from BarcosDirectorio.Barcos import Barco
from BarcosDirectorio.ManejadorDeContenedoresDirectorio.ManejadorDeContenedores import ManejadorDeContenedores
from Camion import Camion
from Cargas.Carga import Carga
from Contenedores import Contenedor
from EmpresaDirectorio.EmpresaData import EmpresaData
from Excepciones.exceptions import Hay_cargas_que_no_entraron_en_contenedores, No_hay_barcos_disponibles, No_hay_camiones_disponibles
from ManejadorDeCargas import ManejadorDeCargas
from Pedidos import Pedidos
from SelectoraEstrategiaPorCarga import SelectoraEstrategiaPorCarga


class CargadorVehiculos:
    def __init__(self, manejador_cargas: ManejadorDeCargas, manejador_contenedores: ManejadorDeContenedores):
        self.__manejador_cargas = manejador_cargas
        self.__manejador_contenedores = manejador_contenedores
    
    'Getters y Setters'
    def get_manejador_cargas(self):
        return self.__manejador_cargas
    def set_manejador_cargas(self, manejador_cargas):
        self.__manejador_cargas = manejador_cargas
    manejador_cargas = property(get_manejador_cargas,set_manejador_cargas)
    
    def get_manejador_contenedores(self):
        return self.__manejador_contenedores
    def set_manejador_contenedores(self, manejador_contenedores):
        self.__manejador_contenedores = manejador_contenedores
    manejador_contenedores = property(get_manejador_contenedores,set_manejador_contenedores)
    'Fin Getters y Setters'
    
    def cargar_camiones(self, contenedores: List[Contenedor], data: EmpresaData):
        try:
            for contenedor in contenedores:
                camion = data.devolver_un_camion_disponible() # este metodo libera excepcion
                camion.set_contenedor(contenedor)
            # si no libera excepcion termina de 10
            return
        except No_hay_camiones_disponibles as e:
            print(str(e))
            
    # una vez que se carga un contenedor en un barco se debe setear la distancia del barco como la distancia del pedido
    def cargar_barcos(self, barco, contenedor: Contenedor):
        try:
            
            if len(barco.get_contenedores()) < barco.get_cant_contenedores_max():
               
                barco.agregar_contenedores(contenedor) # esto seria un append
            else:
                barco = self.get_empresa_data().devolver_un_barco_disponible() # este metodo libera excepcion
            # si no libera excepcion termina de 10
            return
        except No_hay_barcos_disponibles as e:
            print(str(e))