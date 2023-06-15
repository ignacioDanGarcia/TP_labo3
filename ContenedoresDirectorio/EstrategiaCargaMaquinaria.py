from ContenedoresDirectorio.Estrategy import Estrategia
from ContenedoresDirectorio.Contenedores import Contenedor
from Cargas.Categorias import Categoria
from Cargas.Carga import Carga

class CargaMaquinariaEstrategy(Estrategia):
    
    def verificar_carga(self, carga : Carga, contenedor : Contenedor):
        
        entra = False
    
        if contenedor.medidas_interior.comparar_medidas(carga.get_medidas()) and \
                    carga.get_peso() <= contenedor.get_peso_max() and \
                    carga.get_volumen() <= contenedor.get_volumen_max():
                entra = True
        
        return (entra) # Si entra en el contenedor la carga pasa. No hay conflicto con otros tipos de cargas. 
