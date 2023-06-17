from ContenedoresDirectorio.Estrategy import Estrategia
from ContenedoresDirectorio.Contenedores import Contenedor
from Cargas.Categorias import Categoria
from Cargas.Carga import Carga
from ContenedoresDirectorio.TiposDeContenedores.Tipo import TipoContenedor

class CargaAlimenticiaEstrategy(Estrategia):
    
    def verificar_carga(self, carga : Carga, contenedor : Contenedor):
        puede_llevarla = True
        entra = False
        #V1: if contenedor.get_tipo().lower() != "ventilado": #Si el contenedor no es ventilado no puede llevar una carga alimenticia
        if contenedor.get_tipo() != TipoContenedor.VENTILADO:
            puede_llevarla = False
        
        if(self.hay_carga_quimica(contenedor)):
            puede_llevarla = False # Una carga alimenticia no puede viajar con una carga química
        
        if contenedor.medidas_interior.comparar_medidas(carga.get_medidas()) and \
                    carga.get_peso() <= contenedor.get_peso_max() and \
                    carga.get_volumen() <= contenedor.get_volumen_max():
                entra = True
        
        return (puede_llevarla and entra) # Si puede llevarla por el tipo y entra en el contenedor la carga pasa.



    def hay_carga_quimica(self, contenedor :Contenedor):
        for carga in contenedor.get_cargas():
            if carga.get_categoria() == Categoria.QUIMICA:
                return True
        return False