from ContenedoresDirectorio.Estrategy import Estrategia
from Excepciones.exceptions import contenedor_no_puede_llevar_carga, el_contenedor_basico_no_puede_mat_especial, medidas_incorrectas, no_existe_carga, distancia_incorrecta
from Cargas.Carga import Carga
from ContenedoresDirectorio.Contenedores import Contenedor
from Cargas.Categorias import Categoria
from ContenedoresDirectorio.EstrategiaCargaAlimenticia import CargaAlimenticiaEstrategy
from ContenedoresDirectorio.EstrategiaCargaMaquinaria import CargaMaquinariaEstrategy
from ContenedoresDirectorio.EstrategiaCargaQuimica import CargaQuimicaEstrategy

class SelectoraEstrategiaPorCarga():
    def __init__(self) -> None:
        pass
    # Si se mete una nueva estrategia la agregaríamos acá! ;)
    def estrategia_por_categoria(self, categoria):
        estrategias = {
        Categoria.MAQUINARIA: CargaMaquinariaEstrategy(),
        Categoria.ALIMENTICIA: CargaAlimenticiaEstrategy(),
        Categoria.QUIMICA: CargaQuimicaEstrategy()
    }
        return estrategias.get(categoria)