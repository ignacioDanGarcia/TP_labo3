from unittest import TestCase
from unittest.mock import Mock, patch, MagicMock
from ContenedoresDirectorio.Contenedores import Contenedor
from Cargas.Carga import Carga
from ContenedoresDirectorio.ObtenedorDeIDSDeCargas import ObtenedorIDSCargas
from Medidas import Medidas
from ContenedoresDirectorio.TiposDeContenedores.Tipo import TipoContenedor
from Cargas.Categorias import Categoria
from ContenedoresDirectorio.LocalizadorDeCargas import LocalizadorDeCargasConID

class TestObtenedorDeIDS(TestCase):
    def test_traigo_lista_de_ids_de_las_cargas_de_un_contenedor(self):
        medidas = Medidas(3,2,2)
        carga = Carga(medidas,50,Categoria.MAQUINARIA)
        carga.set_id(1)
        carga2 = Carga(medidas,50,Categoria.MAQUINARIA)
        carga2.set_id(1)
        cargas = [carga,carga2]
        
        
        mock_contenedor = Mock()
        mock_contenedor.get_tipo.return_value = TipoContenedor.BASICO
        mock_contenedor.get_cargas.return_value =cargas       #--------------------------------Esto
        mock_contenedor.get_precio_transporte_base.return_value = 500
        mock_contenedor.get_medidas_interior.return_value = Medidas(12.0,2.35,2.3)
        mock_contenedor.peso_contenedor.return_value = 100
        
        localizador = LocalizadorDeCargasConID()
        cargasid1 = localizador.traer_cargas_del_id(1, mock_contenedor)
        
        assert cargasid1 == cargas              #--------------------------Es igual a esto.  
    
    def test_traigo_lista_de_ids_de_las_cargas_de_un_contenedor_con_cargas_distintas(self):
        medidas = Medidas(3,2,2)
        carga = Carga(medidas,50,Categoria.MAQUINARIA)
        carga.set_id(1)
        carga2 = Carga(medidas,50,Categoria.MAQUINARIA)
        carga2.set_id(2)
        cargas = [carga,carga2]
        
        
        mock_contenedor = Mock()
        mock_contenedor.get_tipo.return_value = TipoContenedor.BASICO
        mock_contenedor.get_cargas.return_value =cargas       
        mock_contenedor.get_precio_transporte_base.return_value = 500
        mock_contenedor.get_medidas_interior.return_value = Medidas(12.0,2.35,2.3)
        mock_contenedor.peso_contenedor.return_value = 100
        
        localizador = LocalizadorDeCargasConID()
        cargasid1 = localizador.traer_cargas_del_id(1, mock_contenedor)
        
        assert cargasid1.pop(0) == carga
    
    def test_traigo_lista_de_ids_de_las_cargas_de_un_contenedor_con_cargas_distintas_y_mas_de_una_carga_con_el_mismo_id(self):
        medidas = Medidas(3,2,2)
        carga = Carga(medidas,50,Categoria.MAQUINARIA)
        carga.set_id(1)
        carga2 = Carga(medidas,50,Categoria.MAQUINARIA)
        carga2.set_id(9)
        carga3 = Carga(medidas,50,Categoria.MAQUINARIA)
        carga3.set_id(1)
        cargas = [carga,carga2,carga3]
        
        
        mock_contenedor = Mock()
        mock_contenedor.get_tipo.return_value = TipoContenedor.BASICO
        mock_contenedor.get_cargas.return_value =cargas       
        mock_contenedor.get_precio_transporte_base.return_value = 500
        mock_contenedor.get_medidas_interior.return_value = Medidas(12.0,2.35,2.3)
        mock_contenedor.peso_contenedor.return_value = 100
        
        localizador = LocalizadorDeCargasConID()
        cargasid1 = localizador.traer_cargas_del_id(1, mock_contenedor)
        
        cargas_primer_cliente = [carga,carga3]
        assert cargasid1 == cargas_primer_cliente