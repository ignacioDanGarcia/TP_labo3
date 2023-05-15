from unittest import TestCase
from unittest.mock import Mock, patch, MagicMock
from BarcosDirectorio.Barco_especial import Barco_especial
class test_barcos(TestCase):
    def test_peso_excedido(self):
        barco = Barco_especial(1,100,3,False)
        mock_contenedor = Mock()
        mock_contenedor.get_peso.return_value = 150
        assert barco.tiene_lugar(mock_contenedor) == False