from unittest import TestCase
from unittest.mock import Mock, patch, MagicMock
from ContenedoresDirectorio.Contenedores import Contenedor
from Cargas.Carga import Carga
from ContenedoresDirectorio.ObtenedorDeIDSDeCargas import ObtenedorIDSCargas
from Medidas import Medidas
from ContenedoresDirectorio.TiposDeContenedores.Tipo import TipoContenedor
from Cargas.Categorias import Categoria


class TestObtenedorDeIDS(TestCase):
    def test_traigo_lista_de_ids_de_las_cargas_de_un_contenedor(self):
        medidas = Medidas(3,2,2)
        carga = Carga(medidas,50,Categoria.MAQUINARIA)
        carga.set_id(1)
        carga2 = Carga(medidas,50,Categoria.MAQUINARIA)
        carga2.set_id(6)
        cargas = [carga,carga2]
        
        
        mock_contenedor = Mock()
        mock_contenedor.get_tipo.return_value = TipoContenedor.BASICO
        mock_contenedor.get_cargas.return_value = cargas
        mock_contenedor.get_precio_transporte_base.return_value = 500
        mock_contenedor.get_medidas_interior.return_value = Medidas(12.0,2.35,2.3)
        mock_contenedor.peso_contenedor.return_value = 100
        obtenedor_ids = ObtenedorIDSCargas()
        ids = obtenedor_ids.obtener_ids_cargas(mock_contenedor)
        assert ids == [1,6]
        assert ids.pop(1) == 6
    
    def test_traigo_lista_de_ids_de_las_cargas_de_un_contenedor_con_ids_repetidos(self):
        medidas = Medidas(3,2,2)
        carga = Carga(medidas,50,Categoria.MAQUINARIA)
        carga.set_id(8)
        carga2 = Carga(medidas,50,Categoria.MAQUINARIA)
        carga2.set_id(8)
        cargas = [carga,carga2]
        
        
        mock_contenedor = Mock()
        mock_contenedor.get_tipo.return_value = TipoContenedor.BASICO
        mock_contenedor.get_cargas.return_value = cargas
        mock_contenedor.get_precio_transporte_base.return_value = 500
        mock_contenedor.get_medidas_interior.return_value = Medidas(12.0,2.35,2.3)
        mock_contenedor.peso_contenedor.return_value = 100
        obtenedor_ids = ObtenedorIDSCargas()
        ids = obtenedor_ids.obtener_ids_cargas(mock_contenedor)
        assert ids == [8]
        assert len(ids) == 1
    
    def test_traigo_lista_de_ids_de_las_cargas_de_un_contenedor_vacio(self):
        
        cargas = []
        
        
        mock_contenedor = Mock()
        mock_contenedor.get_tipo.return_value = TipoContenedor.BASICO
        mock_contenedor.get_cargas.return_value = cargas
        mock_contenedor.get_precio_transporte_base.return_value = 500
        mock_contenedor.get_medidas_interior.return_value = Medidas(12.0,2.35,2.3)
        mock_contenedor.peso_contenedor.return_value = 100
        obtenedor_ids = ObtenedorIDSCargas()
        ids = obtenedor_ids.obtener_ids_cargas(mock_contenedor)
        assert ids == []
        assert len(ids) == 0