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

"""
CLASE QUE VERIFICA QUE SE PUEDAN CARGAR LOS CONTENEDORES EN LOS BARCOS 
O CAMIONES PARA PODER ENVIARLOS AL SECTOR DE DISTRIBUCION  
"""

class EmpresaDeposito():
    def __init__(self, empresa_data: EmpresaData):
        self.__empresa_data = empresa_data
    
    'Getters y Setters'
    def get_empresa_data(self):
        return self.__empresa_data
    
    def set_empresa_data(self, empresa_data):
        self.__empresa_data = empresa_data
    empresa_data = property(get_empresa_data,set_empresa_data)
    'Fin Getters y Setters'
    
    def ordenar_por_categoria(cargas: List[Carga]):
        cargas.sort(key=lambda carga: carga.get_categoria().value)

    def llenar_contenedores(self, pedido: Pedidos):
        # llena contenedores con cargas, y mete contenedores usados en el pedido
        # capaz podriamos meter solo el id del contenedor para no guardar tanta info
        cargas_pedido = pedido.get_cargas()
        self.ordenar_por_categoria(cargas_pedido)
        
        manejador_de_cargas = ManejadorDeCargas(SelectoraEstrategiaPorCarga())
        data = self.get_empresa_data()
        for carga in cargas_pedido:
            asignada = False
            
            if pedido.get_cant_contenedores() != 0:
                for contenedor in pedido.get_contenedores():
                    if manejador_de_cargas.puede_cargar(carga, contenedor):
                        manejador_de_cargas.cargar(carga, contenedor)
                        cargas_pedido.remove(carga)
                        asignada = True
                        break
            
            if asignada:
                continue
            
            for contenedor in data.get_contenedores_disponibles():
                if manejador_de_cargas.puede_cargar(carga, contenedor):
                    manejador_de_cargas.cargar(carga, contenedor)
                    cargas_pedido.remove(carga)
                    pedido.agregar_contenedor(contenedor) # aca se guardan los contenedores en el pedido
                    break
        
        if len(cargas_pedido) is not 0:
            # excepcion catcheada en procesar_pedido de Oficina
            raise Hay_cargas_que_no_entraron_en_contenedores("Sus cargas no entran en nuestros contenedores")
        
        
    