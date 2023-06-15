from unittest import TestCase
from unittest.mock import Mock, patch, MagicMock
import mock

from pytest import raises
from Cargas.Carga import Carga
from Excepciones.exceptions import medidas_incorrectas
from Medidas import Medidas

class TestMedidas(TestCase):
    def test_volumen_simple(self):
        medidas = Medidas(3,3,3)
        carga = Carga(medidas,3,100)
        assert(carga.get_volumen()) == 27
        
    def test_volumen_random(self):
        medidas = Medidas(8,5,2)
        carga = Carga(medidas,3,100)
        assert(carga.get_volumen()) == 80
    
    
    def test_comparar_medidas_exception(self):
         #devuelve FAlSE si las medidas pasadas por parametro son mayores a las de la instancia
        #devuelve TRUE si las medidas pasadas x parametro son menores o iguales a las de la instancia
        medidas_1 = Medidas(3,3,3)
        medidas_2 = Medidas(4,4,3)
        
        assert  medidas_1.comparar_medidas(medidas_2) == False

    def test_comparar_medidas_correcto(self):
         #devuelve FAlSE si las medidas pasadas por parametro son mayores a las de la instancia
        #devuelve TRUE si las medidas pasadas x parametro son menores o iguales a las de la instancia
        medidas_2 = Medidas(3,3,3)
        medidas_1 = Medidas(4,4,3)
        
        assert(medidas_1.comparar_medidas(medidas_2)) == True
        