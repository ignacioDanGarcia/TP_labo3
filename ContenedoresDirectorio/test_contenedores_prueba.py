from types import NoneType
from unittest import TestCase
from unittest.mock import Mock, patch, MagicMock
import mock
from Carga import Carga
from ContenedoresDirectorio.BasicoHCContenedor import BasicoHCContenedor
from ContenedoresDirectorio.FlatRackContenedor import FlatRackContenedor
from pytest import raises
from Excepciones.exceptions import *
from Medidas import Medidas

class test_empresa(TestCase):
     
    """ 5. Cualquier carga cuyas dimensiones, volumen o peso supere lo definido en el container no podrá ser trasladada en el mismo.
    6. Un contenedor sin características especiales no puede transportar material especial. """
        
    def test_verificar_carga_por_dimensiones1(self):
        conteiner_hc = BasicoHCContenedor(False)
        medidas = Medidas(100,3,5)
        carga = Carga(medidas,50,None)
        with self.assertRaises(contenedor_no_puede_llevar_carga):
            conteiner_hc.verificar_carga(carga)
        'medidas superiores'
    
    def test_verificar_carga_por_dimensiones2(self):
        conteiner_hc = BasicoHCContenedor(False)
        medidas = Medidas(3,2,2)
        carga = Carga(medidas,50,None)
        assert(conteiner_hc.verificar_carga(carga)) == True
    'Tiene medidas que si entran'
    
    def test_verificar_carga_por_mat_especial1(self):
        conteiner_hc = BasicoHCContenedor(False)
        medidas = Medidas(3,2,2)
        carga = Carga(medidas,50,True)
        with self.assertRaises(el_contenedor_basico_no_puede_mat_especial):
            conteiner_hc.verificar_carga(carga)
        'Tiene medidas que entran pero el contenido es especial en un basico.'
        
    def test_verificar_carga_por_mat_especial2(self):
        conteiner_fr = FlatRackContenedor(True)
        medidas = Medidas(3,2,2)
        carga = Carga(medidas,50,True)
        assert(conteiner_fr.verificar_carga(carga)) == True
        'Tiene medidas que entran y el contenido es especial en un especial.'
    
    def test_verificar_carga_por_mat_especial3(self):
        conteiner_fr = FlatRackContenedor(True)
        medidas = Medidas(3,2,2)
        carga = Carga(medidas,50,False)
        assert(conteiner_fr.verificar_carga(carga)) == True
        'Tiene medidas que entran y el contenido no es especial en un especial.'
    
    def test_verificar_carga_por_dimensiones3(self):
        conteiner_fr = FlatRackContenedor(False)
        medidas = Medidas(100,3,5)
        carga = Carga(medidas,50,None)
        with self.assertRaises(contenedor_no_puede_llevar_carga):
            conteiner_fr.verificar_carga(carga)
        'medidas superiores'