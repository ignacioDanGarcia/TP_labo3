from unittest import TestCase

from BarcosDirectorio.Barcos import Barco
from BarcosDirectorio.Factory.SelectorDeCreador import SelectorCreador
from BarcosDirectorio.TiposDeBarcos import TiposBarcos

class test_creacion_de_barcos_con_factory_method(TestCase):
    def test_creacion_de_barco_basico(self):
        selector_de_factoria = SelectorCreador()
        
        creador_barcos_basicos = selector_de_factoria.crear_factoria_de_tipo_de_barco(TiposBarcos.BASICO)
        
        barco = creador_barcos_basicos.crear_barco(1,500,3,500)
        assert isinstance(barco,Barco)
        assert barco.get_tipo_barco() == TiposBarcos.BASICO

        assert barco.get_peso_max() == 500
        assert barco.get_cant_contenedores_max() == 3
    
    def test_creacion_de_barco_especial(self):
        selector_de_factoria = SelectorCreador()
        creador_barcos_especiales = selector_de_factoria.crear_factoria_de_tipo_de_barco(TiposBarcos.ESPECIAL)
        
        barco = creador_barcos_especiales.crear_barco(1,500,3,500)
        assert isinstance(barco,Barco)
        assert barco.get_tipo_barco() == TiposBarcos.ESPECIAL
        assert barco.get_peso_max() == 500
        assert barco.get_cant_contenedores_max() == 3
        