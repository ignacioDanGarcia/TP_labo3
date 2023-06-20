from typing import List
from BarcosDirectorio.Barcos import Barco
from Camion import Camion
from Cargas.Carga import Carga
from ContenedoresDirectorio.Contenedores import Contenedor
from EmpresaDirectorio.EmpresaData import EmpresaData
from Excepciones.exceptions import Hay_cargas_que_no_entraron_en_contenedores, No_hay_barcos_disponibles, No_hay_camiones_disponibles
from ContenedoresDirectorio.ManejadorDeCargas import ManejadorDeCargas
from Pedidos import Pedidos
from ContenedoresDirectorio.SelectoraEstrategiaPorCarga import SelectoraEstrategiaPorCarga


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
    
    def ordenar_por_categoria(self, cargas: List[Carga]):
        cargas.sort(key=lambda carga: carga.get_categoria().value)

    def obtener_contenedores_pedido(self, pedido: Pedidos):
        contenedores_completos = self.get_empresa_data().get_contenedores()
        ids_deseados = pedido.get_contenedores_ids()

        contenedores_deseados = [contenedor for contenedor in contenedores_completos if contenedor.get_id() in ids_deseados]
        return contenedores_deseados

    def cargar_contenedor(self, manejador_de_cargas: ManejadorDeCargas, carga: Carga, contenedor: Contenedor, cargas_pedido, pedido: Pedidos, barco=None):
        if manejador_de_cargas.puede_cargar(carga, contenedor):
            manejador_de_cargas.cargar(carga, contenedor)
            cargas_pedido.remove(carga)
            pedido.agregar_contenedor(contenedor.get_id())
            if barco:
                barco.agregar_contenedores(contenedor)
            return True
        return False

    
    def llenar_contenedores_y_llenar_barcos(self, pedido: Pedidos):
        cargas_pedido = pedido.get_cargas()
        self.ordenar_por_categoria(cargas_pedido)

        manejador_de_cargas = ManejadorDeCargas(SelectoraEstrategiaPorCarga())
        data = self.get_empresa_data()
        barcos_misma_distancia = self.get_empresa_data().get_barcos_disponible_misma_distancia(pedido.get_distancia())
        
        for carga in cargas_pedido:
            asignada = False
            barco_distancia_cero = self.get_empresa_data().get_barco_disponible_distancia_cero()
            
            # primero analizo los contenedores ya usados por el pedido
            if pedido.get_cant_contenedores() != 0:
                for contenedor in self.obtener_contenedores_pedido(pedido):
                    if self.cargar_contenedor(manejador_de_cargas, carga, contenedor, cargas_pedido, pedido):
                        asignada = True
                        break

            if asignada:
                continue
            
            # despues analizo los barcos con contenedores que vayan al mismo lugar
            for barco in barcos_misma_distancia:
                # primero sus contenedores
                for contenedor in barco.get_contenedores():
                    if self.cargar_contenedor(manejador_de_cargas, carga, contenedor, cargas_pedido, pedido):
                        asignada = True
                        break
                # luego trato de insertarle mas contenedores
                if len(barco.get_contenedores()) < barco.get_cant_contenedores_max():
                    for contenedor in data.get_contenedores_disponibles():
                        if self.cargar_contenedor(manejador_de_cargas, carga, contenedor, cargas_pedido, pedido, barco):
                            asignada = True
                            break

            if asignada:
                continue
            
            # si todavia quedan cargas agarro un barco disponible con distancia no asignada todavia
            if barco_distancia_cero is None and len(barcos_misma_distancia) == 0:
                raise No_hay_barcos_disponibles("En este momento no hay barcos disponibles")

            for contenedor in data.get_contenedores_disponibles():
                if self.cargar_contenedor(manejador_de_cargas, carga, contenedor, cargas_pedido, pedido, barco_distancia_cero):
                    barco_distancia_cero.set_distancia(pedido.get_distancia())
                    barcos_misma_distancia.append(barco_distancia_cero)
                    break
            
            # si la carga sigue estando en la lista de pedidos quiere decir que no fue asignada
        if carga in cargas_pedido:
            # falta ver donde se catchea
            raise Hay_cargas_que_no_entraron_en_contenedores("Sus cargas no entran en nuestros contenedores")
        
        # si llega aca es porque se cargaron correctamente 