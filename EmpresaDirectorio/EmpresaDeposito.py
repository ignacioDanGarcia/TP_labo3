from typing import List
from BarcosDirectorio.Barcos import Barco
from BarcosDirectorio.ManejadorDeContenedoresDirectorio.ManejadorDeContenedores import ManejadorDeContenedores
from Cargas.Carga import Carga
from ContenedoresDirectorio.Contenedores import Contenedor
from EmpresaDirectorio.EmpresaData import EmpresaData
from Excepciones.exceptions import Hay_cargas_que_no_entraron_en_contenedores, No_hay_barcos_disponibles
from ContenedoresDirectorio.ManejadorDeCargas import ManejadorDeCargas
from Pedidos import Pedidos


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

    def asignar_carga_a_contenedor_existente(self, pedido: Pedidos, carga: Carga):
        if pedido.get_cant_contenedores() == 0:
            return None
        
        for contenedor in self.obtener_contenedores_pedido(pedido):
            
            if self.cargar_contenedor(self.get_manejador_cargas(), carga, contenedor, pedido):
                
                return contenedor

        return None


    def asignar_carga_a_contenedor_barco(self, pedido: Pedidos, carga: Carga, barcos: List[Barco]):
        for barco in barcos:
            if len(barco.get_contenedores()) <= barco.get_cant_contenedores_max():
                contenedores_disponibles = barco.get_contenedores() + self.get_empresa_data().get_contenedores_disponibles()
                for contenedor in contenedores_disponibles:
                    if self.cargar_contenedor(self.get_manejador_cargas(), carga, contenedor, pedido):
                        if contenedor not in barco.get_contenedores():
                            self.get_manejador_contenedores().cargar(barco, contenedor)
                        self.actualizar_contenedor_en_empresa_data(contenedor)
                        self.actualizar_barco_en_empresa_data(barco)
                        return barco
        return None
    
    def actualizar_barco_en_empresa_data(self, barco_actualizado):
        barcos = self.get_empresa_data().get_barcos()
        for i in range(len(barcos)):
            barco = barcos[i]
            if barco.get_id() == barco_actualizado.get_id():
                barcos[i] = barco_actualizado
                break


    def actualizar_contenedor_en_empresa_data(self, contenedor_actualizado):
        for i, contenedor in enumerate(self.get_empresa_data().get_contenedores()):
            if contenedor.get_id() == contenedor_actualizado.get_id():
                self.get_empresa_data().get_contenedores()[i] = contenedor_actualizado
                break

    def verificar_cargas_asignadas(self, cargas_pedido: List[Carga], cargas_asignadas: List[Carga]):
        if set(cargas_pedido) != set(cargas_asignadas):
            raise Hay_cargas_que_no_entraron_en_contenedores("Sus cargas no entran en nuestros contenedores")

        # si llega aca es porque se cargaron correctamente
    
    def llenar_contenedores_y_llenar_barcos(self, pedido: Pedidos):
        cargas_pedido = pedido.get_cargas()
        self.ordenar_por_categoria(cargas_pedido)

        data = self.get_empresa_data()
        barcos_misma_distancia = data.get_barcos_disponible_misma_distancia(pedido.get_distancia())
        cargas_asignadas = []

        for carga in cargas_pedido:
            contenedor_actualizado = self.asignar_carga_a_contenedor_existente(pedido, carga)
            if contenedor_actualizado is not None:
                cargas_asignadas.append(carga)
                self.actualizar_contenedor_en_empresa_data(contenedor_actualizado)
                continue

            barco_actualizado = self.asignar_carga_a_contenedor_barco(pedido, carga, barcos_misma_distancia)
            if barco_actualizado is not None:
                self.actualizar_barco_en_empresa_data(barco_actualizado)
                cargas_asignadas.append(carga)
                continue

            barco_actualizado = self.asignar_carga_a_contenedor_barco(pedido, carga, [data.get_barco_disponible_distancia_cero()])
            if barco_actualizado is not None:
                cargas_asignadas.append(carga)
                self.actualizar_barco_en_empresa_data(barco_actualizado)
                continue

            raise No_hay_barcos_disponibles("En este momento no hay barcos disponibles")

        self.verificar_cargas_asignadas(cargas_pedido, cargas_asignadas)