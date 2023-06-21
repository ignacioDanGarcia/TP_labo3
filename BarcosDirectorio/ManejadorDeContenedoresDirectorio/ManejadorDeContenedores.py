from BarcosDirectorio.Barcos import Barco
from BarcosDirectorio.ManejadorDeContenedoresDirectorio.SelectoraEstrategiaPorBarco import SelectoraEstrategiaPorContenedor
from ContenedoresDirectorio.Contenedores import Contenedor
from Excepciones.exceptions import no_existe_carga

class ManejadorDeContenedores():
    def __init__(self, selectora: SelectoraEstrategiaPorContenedor) -> None:
        self.__estrategia = None
        self.__selectora = selectora
    """
    def agregar_contenedores(self,contenedor):
        self.__contenedores.append(contenedor)
    """ 
    'Getters y setters'
    def get_selectora(self):
        return self.__selectora
    def set_selectora(self,selectora):
        self.__selectora = selectora
    selectora = property(get_selectora,set_selectora)
    
    def get_estrategia(self):
        return self.__estrategia
    def set_estrategia(self,estrategia):
        self.__estrategia = estrategia
    estrategia = property(get_estrategia,set_estrategia)
    'Fin getters y setters'
    
    def cargar(self, barco :Barco, contenedor :Contenedor):
        if self.puede_cargar(barco, contenedor):
            barco.contenedores.append(contenedor)
        return False
    
    def puede_cargar(self, barco :Barco, contenedor :Contenedor):
        self.settear_estrategia(contenedor)
        return self.__estrategia.verificar_carga(barco,contenedor)
    
    def settear_estrategia(self,contenedor: Contenedor):
        self.set_estrategia(self.__selectora.estrategia_por_categoria(contenedor.get_tipo()))
    
    def vaciar_contenedor(self, barco :Barco):
        contenedores = []
        for contenedor in barco.get_cargas():
            barco.append(contenedor)
        barco.get_contenedores().clear()
        return contenedores
    
    def traer_carga(self, barco: Barco, contenedor: Contenedor):
        contenedores = barco.get_contenedores()
        if contenedor in contenedores:
            contenedores.remove(contenedor)
            return contenedor
        raise(no_existe_carga("No existe el contenedor buscado."))
    