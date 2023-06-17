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
    
    
    # lo que me falta para escribir el metodo es:
    # ver si el cliente quiere camion o no,
    # si quiere barco, o las dos cosas
    # y si todo sale bien, mandarle vehiculos a EmpresaEnvios para que ejecute viajar
    
    def procesar_pedido(self, pedido: Pedidos):
        # pedirle a empresa deposito que traten de llenar los contenedores
        # chequeando las cargas con los contenedores que tiene la empresa, en empresa data
        
        # guardas los contenedores usados en pedido.contenedores
        
        # si sale bien chequear si tenemos los vehiculos del tipo de viaje que quiere
        
        # si sale bien los contenedores en los barcos o camiones, con los que estan en empresa data
        
        # si sale bien, ejecutas self.calcular_precio_pedido que es el metodo de abajo
        
        
        pass
    
    
    def calcular_precio_pedido(self, pedido, distancia):
        # vas a empresa cotizaciones y haces lo siguiente:
        
        # pedido_cargas = pedido.get_cargas()
        """
        for contenedor in pedido.contenedores: # que son los contenedores que va a utilizar ese pedido
            # le pasamos todas las cargas del cliente y calcula solo con las que estan en el contenedor
            precio_pedido = empresa_cotizaciones.calcular_precio(contenedor, pedido.get_distancia(), pedido_cargas)
            
            # aca habria que buscar la forma de remover de pedido_cargas las cargas que se van usando
            # asi al final le devolvemos el precio solo si esa lista de pedido_cargas esta vacia
            # como para liberar una excepcion porque algo salio mal, y no le dimos el precio de todas las cargas
            # creo que nunca pasaria pero bueno es una idea
        
        pedido.set_precio_final_pedido(precio_pedido)
        
        return # nada porque ya se guarda en pedido
        """
        
        pass
    
        # HABRIA QUE VER COMO HACEMOS PARA MANDARLE LOS BARCOS Y CAMIONES CARGADOS A EMPRESA ENVIOS PARA QUE LOS HAGA VIAJAR