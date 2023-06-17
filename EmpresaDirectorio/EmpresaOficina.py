from Pedidos import Pedidos
from ContenedoresDirectorio.DepartamentoDeEstimacionDeCostos.CalculadoraPrecioCargas import CalculadoraPrecioCargas
from ContenedoresDirectorio.DepartamentoDeEstimacionDeCostos.SelectoraEstrategiaPrecio import SelectoraEstrategiaPrecio
from Excepciones.exceptions import contenedor_no_puede_llevar_carga, el_contenedor_basico_no_puede_mat_especial, medidas_incorrectas, no_existe_carga, distancia_incorrecta
from EmpresaData import EmpresaData
"""
CLASE QUE RECIBE PEDIDOS Y DEVUELVE PRECIO A PAGAR    
TASADORA DE PEDIDOS BASICAMENTE

USA EMPRESACOTIZACIONES PARA CALCULAR PRECIO POR CONTENEDOR
"""

class EmpresaOficina():
    def __init__(self, empresa_data: EmpresaData) -> None:
        self.__empresa_data = empresa_data
    
    def get_empresa_data(self):
        return self.__empresa_data
    
    def set_empresa_data(self, empresa_data):
        self.__empresa_data = empresa_data
    empresa_data = property(get_empresa_data,set_empresa_data)
    
    
    def calcular_precio_pedido(self, pedido, distancia):
        pass
    
    def procesar_pedido(self, pedido: Pedidos):
        pass