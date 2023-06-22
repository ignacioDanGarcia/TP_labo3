from ContenedoresDirectorio.Estrategy import Estrategia
from ContenedoresDirectorio.Contenedores import Contenedor
from Cargas.Categorias import Categoria
from Cargas.Carga import Carga
from ContenedoresDirectorio.TiposDeContenedores.TipoContenedor import TipoContenedor

class CargaAlimenticiaEstrategy(Estrategia):
    
    def verificar_carga(self, carga : Carga, contenedor : Contenedor):
        puede_llevarla = True
        entra = False
        if contenedor.get_tipo() != TipoContenedor.VENTILADO:
            puede_llevarla = False
        
        if(self.hay_carga_quimica(contenedor)):
            puede_llevarla = False 
        
        if contenedor.medidas_interior.comparar_medidas(carga.get_medidas()) and \
                    carga.get_peso() <= contenedor.get_peso_max() and \
                    carga.get_volumen() <= contenedor.get_volumen_max():
                entra = True
        
        return puede_llevarla and entra 



    def hay_carga_quimica(self, contenedor :Contenedor):
        for carga in contenedor.get_cargas():
            if carga.get_categoria() == Categoria.QUIMICA:
                return True
        return False