from typing import List
from BarcosDirectorio.Barcos import Barco
from BarcosDirectorio.ManejadorDeContenedoresDirectorio.ManejadorDeContenedores import ManejadorDeContenedores
from Camion import Camion
from Cargas.Carga import Carga
from ContenedoresDirectorio.Contenedores import Contenedor
from EmpresaDirectorio.EmpresaData import EmpresaData
from Excepciones.exceptions import Hay_cargas_que_no_entraron_en_contenedores, No_hay_barcos_disponibles, No_hay_camiones_disponibles
from ContenedoresDirectorio.ManejadorDeCargas import ManejadorDeCargas
from Pedidos import Pedidos
from ContenedoresDirectorio.SelectoraEstrategiaPorCarga import SelectoraEstrategiaPorCarga


class EmpresaDeposito():
    def __init__(self, empresa_data: EmpresaData, manejador_cargas: ManejadorDeCargas, manejador_contenedores: ManejadorDeContenedores):
        self.__empresa_data = empresa_data
        self.__manejador_cargas = manejador_cargas
        self.__manejador_contenedores = manejador_contenedores
        
    
    'Getters y Setters'
    def get_empresa_data(self):
        return self.__empresa_data
    def set_empresa_data(self, empresa_data):
        self.__empresa_data = empresa_data
    empresa_data = property(get_empresa_data,set_empresa_data)
    
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
    
    def ordenar_por_categoria(self, cargas: List[Carga]):
        cargas.sort(key=lambda carga: carga.get_categoria().value)

    def obtener_contenedores_pedido(self, pedido: Pedidos):
        contenedores_completos = self.get_empresa_data().get_contenedores()
        ids_deseados = pedido.get_contenedores_ids()

        contenedores_deseados = [contenedor for contenedor in contenedores_completos if contenedor.get_id() in ids_deseados]
        return contenedores_deseados

    def cargar_contenedor(self, manejador_de_cargas: ManejadorDeCargas, carga: Carga, contenedor: Contenedor, pedido: Pedidos):
        if manejador_de_cargas.puede_cargar(carga, contenedor):
            manejador_de_cargas.cargar(carga, contenedor)
            pedido.agregar_contenedor(contenedor.get_id())
            return True
        return False

    
    def llenar_contenedores_y_llenar_barcos(self, pedido: Pedidos):
        cargas_pedido = pedido.get_cargas()
        self.ordenar_por_categoria(cargas_pedido)

        
        data = self.get_empresa_data()
        barcos_misma_distancia = self.get_empresa_data().get_barcos_disponible_misma_distancia(pedido.get_distancia())
        cargas_asignadas = []
        
        for carga in cargas_pedido:
            asignada = False
            
            # primero analizo los contenedores ya usados por el pedido
            if pedido.get_cant_contenedores() != 0:
                for contenedor in self.obtener_contenedores_pedido(pedido):
                    if self.cargar_contenedor(self.get_manejador_cargas(), carga, contenedor, pedido):
                        asignada = True
                        break

            if asignada:
                cargas_asignadas.append(carga)
                continue
            
            # despues analizo los barcos con contenedores que vayan al mismo lugar
            for barco in barcos_misma_distancia:
                # primero sus contenedores
                for contenedor in barco.get_contenedores():
                    if self.cargar_contenedor(self.get_manejador_cargas(), carga, contenedor, pedido):
                        asignada = True
                        break
                if asignada:
                    continue
                # luego trato de insertarle mas contenedores
                if len(barco.get_contenedores()) < barco.get_cant_contenedores_max():
                    for contenedor in data.get_contenedores_disponibles():
                        if self.get_manejador_contenedores().cargar(barco, contenedor):
                            if self.cargar_contenedor(self.get_manejador_cargas(), carga, contenedor, pedido):
                                asignada = True
                                break

            if asignada:
                cargas_asignadas.append(carga)
                continue
            
            barco_distancia_cero = self.get_empresa_data().get_barco_disponible_distancia_cero()
            
            # si todavia quedan cargas agarro un barco disponible con distancia no asignada todavia
            if barco_distancia_cero is None or len(barcos_misma_distancia) == 0:
                raise No_hay_barcos_disponibles("En este momento no hay barcos disponibles")

            for contenedor in data.get_contenedores_disponibles():
                if self.get_manejador_contenedores().cargar(barco_distancia_cero, contenedor):
                    if self.cargar_contenedor(self.get_manejador_cargas(), carga, contenedor, pedido):
                        cargas_asignadas.append(carga)
                        barco_distancia_cero.cargar(contenedor)
                        barco_distancia_cero.set_distancia(pedido.get_distancia())
                        barcos_misma_distancia.append(barco_distancia_cero)
                        break

        # si la carga sigue estando en la lista de pedidos quiere decir que no fue asignada
        if set(cargas_pedido).difference(set(cargas_asignadas)):
            raise Hay_cargas_que_no_entraron_en_contenedores("Sus cargas no entran en nuestros contenedores")


        
        # si llega aca es porque se cargaron correctamente