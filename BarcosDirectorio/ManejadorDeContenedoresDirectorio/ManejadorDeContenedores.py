from BarcosDirectorio.Barcos import Barco
from BarcosDirectorio.ManejadorDeContenedoresDirectorio.SelectoraEstrategiaPorBarco import SelectoraEstrategiaPorBarco
from ContenedoresDirectorio.Contenedores import Contenedor

class ManejadorDeContenedores():
    def __init__(self, selectora: SelectoraEstrategiaPorBarco) -> None:
        self.__estrategia = None
        self.__selectora = selectora

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
            barco.get_contenedores().append(contenedor)
        else : return False
    
    def puede_cargar(self, barco :Barco, contenedor :Contenedor):
        self.settear_estrategia(barco)
        return self.__estrategia.verificar_contenedor(barco,contenedor)
    
    def settear_estrategia(self,barco: Barco):
        self.set_estrategia(self.__selectora.estrategia_por_categoria(barco.get_tipo_barco()))
    
    
    '''
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
    '''