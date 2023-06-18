from BarcosDirectorio.Barcos import Barco
from Camion import Camion
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
    def __init__(self, empresa_data: EmpresaData) -> None:
        self.__empresa_data = empresa_data
    
    def get_empresa_data(self):
        return self.__empresa_data
    
    def set_empresa_data(self, empresa_data):
        self.__empresa_data = empresa_data
    empresa_data = property(get_empresa_data,set_empresa_data)
    
    
    # este algoritmo esta abierto a sugerencias y cambios
    # como por ejemplo, primero seleccionar las cargas mas grandes o asi
    # esto ya es un algoritmo que habria que pensar que convendria
    def llenar_contenedores(self, pedido: Pedidos):
        contenedores_usados = set()
        
        cargas_pedido = pedido.get_cargas()
        manejador_de_cargas = ManejadorDeCargas(SelectoraEstrategiaPorCarga())
        data = self.get_empresa_data()
        for carga in cargas_pedido:
            asignada = False
            
            if pedido.get_cant_contenedores() != 0:
                for contenedor in pedido.get_contenedores():
                    if manejador_de_cargas.puede_cargar(carga, contenedor):
                        contenedor.agregar_carga(carga)
                        cargas_pedido.remove(carga)
                        contenedores_usados.add(contenedor) # un add en una set no permite elementos duplicados
                        asignada = True
                        break
            
            if asignada:
                continue
            
            for contenedor in data.get_contenedores_disponibles():
                if manejador_de_cargas.puede_cargar(carga, contenedor):
                    contenedor.agregar_carga(carga)
                    cargas_pedido.remove(carga)
                    contenedores_usados.add(contenedor) # un add en una set no permite elementos duplicados
                    break
        
        if len(cargas_pedido) is not 0:
            # excepcion catcheada en procesar_pedido de Oficina
            raise Hay_cargas_que_no_entraron_en_contenedores("Sus cargas no entran en nuestros contenedores")
        
        lista_contenedores_usados = list(contenedores_usados)
        return lista_contenedores_usados
        
    def cargar_camion(self, contenedores):
        try:
            for contenedor in contenedores:
                camion = self.get_empresa_data().devolver_un_camion_disponible() # este metodo libera excepcion
                camion.set_contenedor(contenedor)
            # si no libera excepcion termina de 10
            return
        except No_hay_camiones_disponibles as e:
            print(str(e))
            
    # el de camiones no porque son 5, pero este algoritmo esta abierto a sugerencias y cambios
    def cargar_barco(self, contenedores):
        try:
            barco = self.get_empresa_data().devolver_un_barco_disponible() # este metodo libera excepcion
            for contenedor in contenedores:
                if len(barco.get_contenedores()) < barco.get_cant_contenedores_max():
                
                    barco.set_contenedores(contenedor)
                else:
                    barco = self.get_empresa_data().devolver_un_barco_disponible() # este metodo libera excepcion
            # si no libera excepcion termina de 10
            return
        except No_hay_barcos_disponibles as e:
            print(str(e))
            
    
    """
    usa metodos de EmpresaData como devolver_un_camion_disponible o devolver_un_barco_disponible
    y le catchea las excepciones
    """