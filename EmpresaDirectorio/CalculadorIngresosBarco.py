from ContenedoresDirectorio.Contenedores import Contenedor
from ContenedoresDirectorio.DepartamentoDeEstimacionDeCostos.CalculadoraPrecioCargas import CalculadoraPrecioCargas
from ContenedoresDirectorio.DepartamentoDeEstimacionDeCostos.SelectoraEstrategiaPrecio import SelectoraEstrategiaPrecio
from Excepciones.exceptions import no_existe_carga, distancia_incorrecta
from ContenedoresDirectorio.ObtenedorDeIDSDeCargas import ObtenedorIDSCargas
from ContenedoresDirectorio.LocalizadorDeCargas import LocalizadorDeCargasConID
"""
CLASE QUE RECIBE CONTENEDORES CARGADOS Y DEVUELVE PRECIO A PAGAR
DE ESE CONTENEDOR
"""

class CalculadorIngresosBarco():
    def __init__(self):
        self.__la_calcu = None
    
    'Getters y Setters'
    def get_la_calcu(self):
        return self.__la_calcu
    def set_la_calcu(self, c):
        self.__la_calcu = c
    la_calcu = property(get_la_calcu,set_la_calcu)
    'Fin Getters y Setters'
    
    def llenar_la_calculadora_precio_cargas(self, contenedor, distancia):
        self.set_la_calcu(CalculadoraPrecioCargas(contenedor))
        selectora = SelectoraEstrategiaPrecio()
        
        
        (precio_cont_lleno, precio_cont_no_lleno) = selectora.estrategia_por_categoria(distancia)
        self.get_la_calcu().set_cant_por_contenedor_no_lleno(precio_cont_no_lleno)
        self.get_la_calcu().set_cant_por_contenedor_lleno(precio_cont_lleno)
    
    def calcular_precio(self, contenedor: Contenedor, distancia):
        if distancia is None or not isinstance(distancia, int):
            # falta ver donde se catchea esto
            raise distancia_incorrecta("La distancia especificada no cumple con ningún caso")
        
        
        cargas_contenedor = contenedor.get_cargas()

        if cargas_contenedor is None:
            # falta ver donde se catchea esto
            raise no_existe_carga("No existe una carga en el contenedor")

        precio_aux = 0
        obtensor_de_ids = ObtenedorIDSCargas()
        ids_cargas = obtensor_de_ids.obtener_ids_cargas(contenedor)
        localizador = LocalizadorDeCargasConID()
        
        for id in ids_cargas:
            cargas_id =localizador.traer_cargas_del_id(id, contenedor)
            for carga in cargas_id:
                precio_aux += self.get_la_calcu().calcular_precio_adicional_estado(carga)
                print(f"ID: {id}")
                print(f"Sumo {self.get_la_calcu().calcular_precio_adicional_estado(carga)}")
            precio_aux += contenedor.get_precio_transporte_base()
            print(f"Sumo: {contenedor.get_precio_transporte_base()}")
        

        
         #- Si cobramos una vz por usar el contenedor
        
        return precio_aux