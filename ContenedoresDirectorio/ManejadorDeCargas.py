from ContenedoresDirectorio.Estrategy import Estrategia
from Excepciones.exceptions import contenedor_no_puede_llevar_carga, el_contenedor_basico_no_puede_mat_especial, medidas_incorrectas, no_existe_carga, distancia_incorrecta
from Cargas.Carga import Carga
from ContenedoresDirectorio.Contenedores import Contenedor
from Cargas.Categorias import Categoria
from ContenedoresDirectorio.EstrategiaCargaAlimenticia import CargaAlimenticiaEstrategy
from ContenedoresDirectorio.EstrategiaCargaMaquinaria import CargaMaquinariaEstrategy
from ContenedoresDirectorio.EstrategiaCargaQuimica import CargaQuimicaEstrategy
from ContenedoresDirectorio.SelectoraEstrategiaPorCarga import SelectoraEstrategiaPorCarga

class ManejadorDeCargas():
    def __init__(self, selectora: SelectoraEstrategiaPorCarga) -> None:
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
    
    
    def cargar(self, carga :Carga, contenedor :Contenedor):
        if self.puede_cargar(carga, contenedor):
            contenedor.cargas.append(carga)
        return False
    
    def puede_cargar(self, carga:Carga, contenedor :Contenedor):
        self.settear_estrategia(carga)
        return self.__estrategia.verificar_carga(carga,contenedor)
    
    def settear_estrategia(self,carga :Carga):
        self.set_estrategia(self.__selectora.estrategia_por_categoria(carga.get_categoria()))
        
    def verificar_carga(self, carga : Carga, contenedor):
        self.settear_estrategia(carga)
        return self.__estrategia.verificar_carga(carga,contenedor)
