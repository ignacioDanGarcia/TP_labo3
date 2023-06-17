from Pedidos import Pedidos
from ContenedoresDirectorio.DepartamentoDeEstimacionDeCostos.CalculadoraPrecioCargas import CalculadoraPrecioCargas
from ContenedoresDirectorio.DepartamentoDeEstimacionDeCostos.SelectoraEstrategiaPrecio import SelectoraEstrategiaPrecio
from Excepciones.exceptions import contenedor_no_puede_llevar_carga, el_contenedor_basico_no_puede_mat_especial, medidas_incorrectas, no_existe_carga, distancia_incorrecta

"""
CLASE QUE RECIBE PEDIDOS Y DEVUELVE PRECIO A PAGAR    
TASADORA DE PEDIDOS BASICAMENTE
"""

class EmpresaOficina():
    def __init__(self) -> None:
        pass
    
    def calcular_precio(self, contenedor, distancia):
        # distancia se llena con un num del moduloGPS
        # este metodo la usaria para llenar el precio del pedido
    
        if (distancia is None or isinstance(distancia, int) is False):
            # hay que ver donde se catchea esto
            raise distancia_incorrecta("La distancia especificada no cumplen con ningún caso")    
        
        cargas = contenedor.get_cargas()
        if cargas is None:
            # hay que ver donde se catchea esto
            raise no_existe_carga("No existe una carga")
        
        la_calcu = CalculadoraPrecioCargas(contenedor)
        selectora = SelectoraEstrategiaPrecio()
        
        
        (precio_cont_lleno, precio_cont_no_lleno) = selectora.estrategia_por_categoria(distancia)
        la_calcu.set_cant_por_contenedor_no_lleno(precio_cont_no_lleno)
        la_calcu.set_cant_por_contenedor_lleno(precio_cont_lleno)

        
        precio_aux = 0
        for carga in cargas:
            
            precio_aux += la_calcu.calcular_precio_adicional_estado(carga)
            
            # aca el contenedor ya va a estar lleno o con pedido listo por eso recorre sus cargas

        
        precio_aux += contenedor.get_precio_transporte_base()
        
        return precio_aux

    