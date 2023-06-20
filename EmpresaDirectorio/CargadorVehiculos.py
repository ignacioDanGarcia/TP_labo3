from typing import List
from BarcosDirectorio.Barcos import Barco
from Camion import Camion
from Cargas.Carga import Carga
from Contenedores import Contenedor
from EmpresaDirectorio.EmpresaData import EmpresaData
from Excepciones.exceptions import Hay_cargas_que_no_entraron_en_contenedores, No_hay_barcos_disponibles, No_hay_camiones_disponibles
from ManejadorDeCargas import ManejadorDeCargas
from Pedidos import Pedidos
from SelectoraEstrategiaPorCarga import SelectoraEstrategiaPorCarga


class CargadorVehiculos:
    def __init__(self, empresa_data: EmpresaData):
        self.__empresa_data = empresa_data
    
    'Getters y Setters'
    def get_empresa_data(self):
        return self.__empresa_data
    def set_empresa_data(self, empresa_data):
        self.__empresa_data = empresa_data
    empresa_data = property(get_empresa_data,set_empresa_data)
    'Fin Getters y Setters'
    
    def cargar_camiones(self, contenedores: List[Contenedor]):
        try:
            for contenedor in contenedores:
                camion = self.get_empresa_data().devolver_un_camion_disponible() # este metodo libera excepcion
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