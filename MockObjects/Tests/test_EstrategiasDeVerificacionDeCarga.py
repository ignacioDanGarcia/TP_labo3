from unittest import TestCase
from unittest.mock import Mock, patch, MagicMock
from Cargas.Carga import Carga
from ContenedoresDirectorio.ManejadorDeCargas import ManejadorDeCargas
from Cargas.Categorias import Categoria
from ContenedoresDirectorio.EstrategiaCargaAlimenticia import CargaAlimenticiaEstrategy
from ContenedoresDirectorio.EstrategiaCargaQuimica import CargaQuimicaEstrategy
from ContenedoresDirectorio.EstrategiaCargaMaquinaria import CargaMaquinariaEstrategy
from Medidas import Medidas
class TestEstrategiaDeCargas(TestCase):
    
    def test_estrategia_alimenticia(self):
        manejador_de_cargas = ManejadorDeCargas()
        carga_mock = Mock()
        
        carga_mock.get_categoria.return_value = Categoria.ALIMENTICIA
        assert carga_mock.get_categoria() == Categoria.ALIMENTICIA
        
        estrategia_alimenticia = CargaAlimenticiaEstrategy()
        assert isinstance(estrategia_alimenticia ,CargaAlimenticiaEstrategy)
        manejador_de_cargas.settear_estrategia(carga_mock)
        
        assert isinstance(manejador_de_cargas.get_estrategia(), CargaAlimenticiaEstrategy)
        #assert manejador_de_cargas.estrategia_por_categoria(carga.get_categoria()) == estrategia_alimenticia
    
    def test_estrategia_quimica(self):
        manejador_de_cargas = ManejadorDeCargas()
        carga_mock = Mock()
        
        carga_mock.get_categoria.return_value = Categoria.QUIMICA
        assert carga_mock.get_categoria() == Categoria.QUIMICA
        
        estrategia_alimenticia = CargaQuimicaEstrategy()
        assert isinstance(estrategia_alimenticia ,CargaQuimicaEstrategy)
        manejador_de_cargas.settear_estrategia(carga_mock)
        
        assert isinstance(manejador_de_cargas.get_estrategia(), CargaQuimicaEstrategy)
        
    def test_estrategia_maquinaria(self):
        manejador_de_cargas = ManejadorDeCargas()
        carga_mock = Mock()
        
        carga_mock.get_categoria.return_value = Categoria.MAQUINARIA
        assert carga_mock.get_categoria() == Categoria.MAQUINARIA
        
        estrategia_alimenticia = CargaMaquinariaEstrategy()
        assert isinstance(estrategia_alimenticia ,CargaMaquinariaEstrategy)
        manejador_de_cargas.settear_estrategia(carga_mock)
        
        assert isinstance(manejador_de_cargas.get_estrategia(), CargaMaquinariaEstrategy)
        
        
        