from ContenedoresDirectorio.Estrategy import Estrategia
from Excepciones.exceptions import contenedor_no_puede_llevar_carga, el_contenedor_basico_no_puede_mat_especial, medidas_incorrectas, no_existe_carga, distancia_incorrecta
from Cargas.Carga import Carga
from ContenedoresDirectorio.Contenedores import Contenedor
from Cargas.Categorias import Categoria
from ContenedoresDirectorio.EstrategiaCargaAlimenticia import CargaAlimenticiaEstrategy
from ContenedoresDirectorio.EstrategiaCargaMaquinaria import CargaMaquinariaEstrategy
from ContenedoresDirectorio.EstrategiaCargaQuimica import CargaQuimicaEstrategy

class ManejadorDeCargas():
    def __init__(self) -> None:
        self.__estrategia = None

    
    def cargar(self, carga :Carga, contenedor :Contenedor):
        if self.puede_cargar(carga, contenedor):
            contenedor.cargas.append(carga)
        return False
    
    def puede_cargar(self, carga:Carga, contenedor :Contenedor):
        self.settear_estrategia(carga)
        return self.__estrategia.verificar_carga(carga,contenedor) 
    
    #Idea: 
    #Hacer un strategy que se defina según el tipo de carga que sea y se verifique en el contenedor que pasamos
    #Si el tipo de carga es alimenticia que solo pueda meterse en un contenedor ventilado si no hay materiales químicos dentro.
    #Si la carga es quimica que pueda cargarse si el contenedor es capaz de llevar material especial y si es Ventilado que no tenga alguna carga alimenticia dentro.
    #Si la carga es maquinaria solo se fija que entre en el contenedor. 
    
    def settear_estrategia(self,carga :Carga):
        self.set_estrategia( self.estrategia_por_categoria(carga.get_categoria()))
    
    #Si se mete una nueva estrategia la agregaríamos acá! ;)
    def estrategia_por_categoria(self, categoria):
        estrategias = {
        Categoria.MAQUINARIA: CargaMaquinariaEstrategy(),
        Categoria.ALIMENTICIA: CargaAlimenticiaEstrategy(),
        Categoria.QUIMICA: CargaQuimicaEstrategy()
    }
        return estrategias.get(categoria)
    
    def get_estrategia(self):
        return self.__estrategia
    def set_estrategia(self,estrategia):
        self.__estrategia = estrategia
        
        
    def verificar_carga(self, carga : Carga, contenedor):
        self.settear_estrategia(carga)
        return self.__estrategia.verificar_carga(carga,contenedor)
