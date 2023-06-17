from ContenedoresDirectorio.DepartamentoDeEstimacionDeCostos.CalculadoraPrecioCargas import CalculadoraPrecioCargas
from ContenedoresDirectorio.DepartamentoDeEstimacionDeCostos.SelectoraEstrategiaPrecio import SelectoraEstrategiaPrecio
from Excepciones.exceptions import contenedor_no_puede_llevar_carga, el_contenedor_basico_no_puede_mat_especial, medidas_incorrectas, no_existe_carga, distancia_incorrecta

"""
CLASE QUE RECIBE CONTENEDORES CARGADOS Y DEVUELVE PRECIO A PAGAR
DE ESE CONTENEDOR
"""

class EmpresaCotizaciones():
    def __init__(self) -> None:
        pass
    
    def calcular_precio(self, contenedor, distancia, cargas_adicionales=None):
        if distancia is None or not isinstance(distancia, int):
            raise distancia_incorrecta("La distancia especificada no cumple con ningún caso")
        
        cargas_cliente = []
        cargas_totales = contenedor.get_cargas()

        if cargas_totales is None:
            raise no_existe_carga("No existe una carga en el contenedor")

        if cargas_adicionales is not None:
            # Filtrar las cargas adicionales que pertenecen al cliente correspondiente
            # que se encuentran en este contenedor
            cargas_cliente = [carga for carga in cargas_adicionales if carga in cargas_totales]
        else: 
            raise no_existe_carga("No existen cargas del cliente")
        
        la_calcu = CalculadoraPrecioCargas(contenedor)
        selectora = SelectoraEstrategiaPrecio()
        
        
        (precio_cont_lleno, precio_cont_no_lleno) = selectora.estrategia_por_categoria(distancia)
        la_calcu.set_cant_por_contenedor_no_lleno(precio_cont_no_lleno)
        la_calcu.set_cant_por_contenedor_lleno(precio_cont_lleno)

        
        precio_aux = 0
        for carga in cargas_cliente:
            
            precio_aux += la_calcu.calcular_precio_adicional_estado(carga)
        

        
        precio_aux += contenedor.get_precio_transporte_base()
        # suma de todas las cargas de un cliente en este contenedor + precio base del contenedor
        # si un contenedor lo usan dos clientes, ambos clientes alquilan el contenedor
        # entonces el precio base se paga dos veces
        return precio_aux

    