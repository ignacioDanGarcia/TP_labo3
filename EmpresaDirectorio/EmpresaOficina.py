from EmpresaDirectorio.EmpresaCotizaciones import EmpresaCotizaciones
from EmpresaDirectorio.EmpresaDeposito import EmpresaDeposito
from Pedidos import Pedidos
from Excepciones.exceptions import Hay_cargas_que_no_entraron_en_contenedores, No_hay_barcos_disponibles, No_hay_camiones_disponibles, no_existe_carga, distancia_incorrecta
from EmpresaDirectorio.EmpresaData import EmpresaData

class EmpresaOficina():
    def __init__(self, empresa_data: EmpresaData, empresa_deposito: EmpresaDeposito, empresa_cotizaciones: EmpresaCotizaciones) -> None:
        self.__empresa_data = empresa_data
        self.__empresa_deposito = empresa_deposito
        self.__empresa_cotizaciones = empresa_cotizaciones
    
    'Getters y setters'
    def get_empresa_data(self):
        return self.__empresa_data
    def set_empresa_data(self, empresa_data):
        self.__empresa_data = empresa_data
    empresa_data = property(get_empresa_data,set_empresa_data)
    
    def get_empresa_deposito(self):
        return self.__empresa_deposito
    def set_empresa_deposito(self, empresa_deposito):
        self.__empresa_deposito = empresa_deposito
    empresa_deposito = property(get_empresa_deposito,set_empresa_deposito)
    
    def get_empresa_cotizaciones(self):
        return self.__empresa_cotizaciones
    def set_empresa_cotizaciones(self, empresa_cotizaciones):
        self.__empresa_cotizaciones = empresa_cotizaciones
    empresa_cotizaciones = property(get_empresa_cotizaciones,set_empresa_cotizaciones)
    'Fin getters y setters'
    
    
    def procesar_pedido(self, pedido: Pedidos):
        try:

            self.get_empresa_deposito().llenar_contenedores_y_llenar_barcos(pedido)

            precio = self.calcular_precio_pedido(pedido, pedido.get_distancia())

            if pedido.get_puerta_a_puerta():
                cant_camiones_disponibles =len(self.get_empresa_data().devolver_camiones_disponibles())
                if cant_camiones_disponibles < pedido.get_cant_contenedores():
                    raise No_hay_camiones_disponibles("En este momento no hay camiones disponibles")
                else:
                    precio += (20000 * pedido.get_cant_contenedores())
                    
                    camiones_disponibles = self.get_empresa_data().devolver_camiones_disponibles()
                    for i, contenedor in enumerate(self.get_empresa_deposito().obtener_contenedores_pedido(pedido)):
                        camiones_disponibles[i].set_contenedor(contenedor)
            
            return precio
                
        except (Hay_cargas_que_no_entraron_en_contenedores) as e:
            print(str(e))
        except No_hay_barcos_disponibles as e:
            print(str(e))
    
    
    def calcular_precio_pedido(self, pedido: Pedidos, distancia):
        try:
            pedido_cargas = pedido.get_cargas()
            
            for contenedor in self.get_empresa_deposito().obtener_contenedores_pedido(pedido):
                # puede liberar excepcion
                precio_pedido = self.get_empresa_cotizaciones().calcular_precio_contenedor_por_pedido(contenedor, distancia, pedido_cargas)
                
            
            pedido.set_precio_final_pedido(precio_pedido)
            
        except distancia_incorrecta as e:
            print(str(e))
        except no_existe_carga as e:
            print(str(e))
        return precio_pedido