from unittest import TestCase
from unittest.mock import Mock, patch, MagicMock
import mock
from ContenedoresDirectorio import *
from pytest import raises
from Excepciones.exceptions import *

class test_empresa(TestCase):
     
    """ 5. Cualquier carga cuyas dimensiones, volumen o peso supere lo definido en el container no podrá ser trasladada en el mismo.
    6. Un contenedor sin características especiales no puede transportar material especial. """
        
    def test_verificar_carga_por_dimensiones(self):
        # falta implementar
        pass
    def test_verificar_carga_por_mat_especial(self):
        # falta implementar
        pass
