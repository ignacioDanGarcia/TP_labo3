from unittest import TestCase
from unittest.mock import Mock, patch, MagicMock
import mock
from ContenedoresDirectorio.BasicoHCContenedor import BasicoHCContenedor
from pytest import raises
from Excepciones.exceptions import *
from Medidas import Medidas

class test_empresa(TestCase):
     
    """ 5. Cualquier carga cuyas dimensiones, volumen o peso supere lo definido en el container no podrá ser trasladada en el mismo.
    6. Un contenedor sin características especiales no puede transportar material especial. """
        
    def test_verificar_carga_por_dimensiones1(self):
        barco_hc = BasicoHCContenedor(3,True)
        medidas = Medidas(3,3,5)
        mock_carga = Mock()
        mock_carga.get_medidas.return_value = medidas
        #mock_carga.get_peso.return_value = 50
        assert(barco_hc.verificar_carga(mock_carga)) == True
        # falta implementar
        pass
    #def test_verificar_carga_por_mat_especial(self):
        # falta implementar
    #    pass