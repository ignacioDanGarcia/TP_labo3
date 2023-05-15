from unittest import TestCase
from unittest.mock import Mock, patch, MagicMock

from pytest import raises
from BarcosDirectorio.Barco_especial import Barco_especial
from BarcosDirectorio.Excepciones.exceptions import Peso_excedido_exception
class test_barcos(TestCase):
    def test_peso_y_mat_aceptado(self):
        barco = Barco_especial(1,100,3,False)
        mock_contenedor = Mock()
        mock_contenedor.get_peso.return_value =80
        mock_contenedor.get_mat_especial.return_value = False
        assert barco.puede_cargar_esta_carga(mock_contenedor) == True
        
class test_barcos(TestCase):
    def test_peso_excedido(self):
        barco = Barco_especial(1,100,3,False)
        mock_contenedor = Mock()
        mock_contenedor.get_peso.return_value =101
        mock_contenedor.get_mat_especial.return_value = False

        with self.assertRaises(Peso_excedido_exception):
            barco.tiene_lugar(mock_contenedor)

    