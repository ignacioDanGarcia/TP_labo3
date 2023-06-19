from EmpresaDirectorio.EmpresaDeposito import EmpresaDeposito
from EmpresaDirectorio.TipoVehiculo import TipoVehiculo
from Pedidos import Pedidos
from ContenedoresDirectorio.DepartamentoDeEstimacionDeCostos.CalculadoraPrecioCargas import CalculadoraPrecioCargas
from ContenedoresDirectorio.DepartamentoDeEstimacionDeCostos.SelectoraEstrategiaPrecio import SelectoraEstrategiaPrecio
from Excepciones.exceptions import Hay_cargas_que_no_entraron_en_contenedores, contenedor_no_puede_llevar_carga, el_contenedor_basico_no_puede_mat_especial, medidas_incorrectas, no_existe_carga, distancia_incorrecta
from EmpresaData import EmpresaData
"""
CLASE QUE RECIBE PEDIDOS Y DEVUELVE PRECIO A PAGAR    
TASADORA DE PEDIDOS BASICAMENTE

USA EMPRESACOTIZACIONES PARA CALCULAR PRECIO POR CONTENEDOR
"""

class EmpresaOficina():
    def __init__(self, empresa_data: EmpresaData, empresa_deposito: EmpresaDeposito) -> None:
        self.__empresa_data = empresa_data
        self.__empresa_deposito = empresa_deposito
    
    def get_empresa_deposito(self):
        return self.__empresa_deposito
    
    def set_empresa_deposito(self, empresa_deposito):
        self.__empresa_deposito = empresa_deposito
    empresa_deposito = property(get_empresa_deposito,set_empresa_deposito)
    
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
        try:
            # se llenan los contenedores y se guardan en el pedido de paso
            contenedores_usados = self.get_empresa_deposito().llenar_contenedores(pedido)
            pedido.set_contenedores(contenedores_usados)
            
            tipos_transportes = pedido.get_tipo_vehiculos() 
            # es una lista que puede tener CAMION, BARCO, O AMBOS
            
            carga_funciones = {
                TipoVehiculo.CAMION: self.get_empresa_deposito().cargar_camion,
                TipoVehiculo.BARCO: self.get_empresa_deposito().cargar_barco
            }

            
            if tipos_transportes not in carga_funciones:
                # falta ver donde se catchea esto y crear bien una excepcion, calculo que será en pedido o algo asi
                raise ValueError("Tipo de transporte no válido.")
            
            for tipo in tipos_transportes:
                funcion_carga = carga_funciones[tipo]
                funcion_carga(contenedores_usados)
            
            
            # si sale todo bien, ejecutas self.calcular_precio_pedido que es el metodo de abajo
            return self.calcular_precio_pedido(pedido, pedido.get_distancias())
                
        except Hay_cargas_que_no_entraron_en_contenedores as e:
            print(str(e))
        
    
    
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