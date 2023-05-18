from unittest import TestCase
from unittest.mock import Mock, patch, MagicMock
import mock

from pytest import raises
from Carga import Carga
from Medidas import Medidas

class test_Carga(TestCase):
    def test_volumen_simple(self):
        medidas = Medidas(3,3,3)
        carga = Carga(medidas,3,100)
        assert(carga.get_volumen()) == 27
    def test_volumen_random(self):
        medidas = Medidas(8,5,2)
        carga = Carga(medidas,3,100)
        assert(carga.get_volumen()) == 80