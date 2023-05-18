from types import NoneType
from unittest import TestCase
from unittest.mock import Mock, patch, MagicMock
import mock
from Carga import Carga
from ContenedoresDirectorio.BasicoHCContenedor import BasicoHCContenedor
from pytest import raises
from Excepciones.exceptions import *
from Medidas import Medidas

class test_empresa(TestCase):
     
    """ 5. Cualquier carga cuyas dimensiones, volumen o peso supere lo definido en el container no podrá ser trasladada en el mismo.
    6. Un contenedor sin características especiales no puede transportar material especial. """
        
    def test_verificar_carga_por_dimensiones1(self):
        conteiner_hc = BasicoHCContenedor(3, False)
        medidas = Medidas(100,3,5)
        carga = Carga(medidas,50,None)
        with self.assertRaises(contenedor_no_puede_llevar_carga):
            conteiner_hc.verificar_carga(carga)
        'El volumen es superior'
    
    def test_verificar_carga_por_dimensiones2(self):
        conteiner_hc = BasicoHCContenedor(3, False)
        medidas = Medidas(3,2,2)
        carga = Carga(medidas,50,None)
        assert(conteiner_hc.verificar_carga(carga)) == True
    
    
    #def test_verificar_carga_por_mat_especial(self):
        # falta implementar
    #    pass
