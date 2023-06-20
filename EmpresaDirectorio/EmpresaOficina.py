from EmpresaDirectorio.EmpresaCotizaciones import EmpresaCotizaciones
from EmpresaDirectorio.EmpresaDeposito import EmpresaDeposito
from EmpresaDirectorio.CargadorVehiculos import CargadorVehiculos
from Pedidos import Pedidos
from ContenedoresDirectorio.DepartamentoDeEstimacionDeCostos.CalculadoraPrecioCargas import CalculadoraPrecioCargas
from ContenedoresDirectorio.DepartamentoDeEstimacionDeCostos.SelectoraEstrategiaPrecio import SelectoraEstrategiaPrecio
from Excepciones.exceptions import Hay_cargas_que_no_entraron_en_contenedores, contenedor_no_puede_llevar_carga, el_contenedor_basico_no_puede_mat_especial, medidas_incorrectas, no_existe_carga, distancia_incorrecta
from EmpresaData import EmpresaData

class EmpresaOficina():
    def __init__(self, empresa_data: EmpresaData, empresa_deposito: EmpresaDeposito, cargador_vehiculos: CargadorVehiculos, empresa_cotizaciones: EmpresaCotizaciones) -> None:
        self.__empresa_data = empresa_data
        self.__empresa_deposito = empresa_deposito
        self.__cargador_vehiculos = cargador_vehiculos
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
    
    def get_cargador_vehiculos(self):
        return self.__cargador_vehiculos
    def set_cargador_vehiculos(self, cargador_vehiculos):
        self.__cargador_vehiculos = cargador_vehiculos
    cargador_vehiculos = property(get_cargador_vehiculos,set_cargador_vehiculos)
    'Fin getters y setters'
    
    
    def procesar_pedido(self, pedido: Pedidos):
        try:
            # se llenan los contenedores y se guardan en el pedido de paso
            self.get_empresa_deposito().ordenar_por_categoria(pedido.get_cargas())
            self.get_empresa_deposito().llenar_contenedores(pedido)
            # los ids de los contenedores ya se guardan en los pedidos cuando se ejecuta el llenar_contenedores
            # si sale todo bien, ejecutas self.calcular_precio_pedido que es el metodo de abajo
            precio = self.calcular_precio_pedido(pedido, pedido.get_distancia())
            
            if pedido.get_puerta_a_puerta():
                precio += 20000
            
            return precio
                
        except Hay_cargas_que_no_entraron_en_contenedores as e:
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