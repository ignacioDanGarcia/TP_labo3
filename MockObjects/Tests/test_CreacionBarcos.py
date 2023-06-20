from unittest import TestCase
from unittest.mock import Mock, patch, MagicMock
from BarcosDirectorio.BarcoBasico import BarcoBasico
from BarcosDirectorio.BarcoEspecial import BarcoEspecial
from BarcosDirectorio.Factory.CreadorDeBarcosBasicos import CreadorBarcosBasicos
from BarcosDirectorio.Factory.CreadorDeBarcosEspeciales import CreadorBarcosEspeciales
from BarcosDirectorio.Factory.SelectorDeCreador import SelectorCreador
from BarcosDirectorio.TiposDeBarcos import TiposBarcos

class test_creacion_de_barcos_con_factory_method(TestCase):
    def test_creacion_de_barco_basico(self):
        selector_de_factoria = SelectorCreador()
        
        creador_barcos_basicos = selector_de_factoria.crear_factoria(TiposBarcos.BASICO)
        
        barco = creador_barcos_basicos.crear_barco(1,500,3,500)
        assert isinstance(barco,BarcoBasico)
        assert barco.get_peso_max() == 500
        assert barco.get_cant_contenedores_max() == 3
    
    def test_creacion_de_barco_especial(self):
        selector_de_factoria = SelectorCreador()
        creador_barcos_especiales = selector_de_factoria.crear_factoria(TiposBarcos.ESPECIAL)
        
        barco = creador_barcos_especiales.crear_barco(1,500,3,500)
        assert isinstance(barco,BarcoEspecial)
        assert barco.get_peso_max() == 500
        assert barco.get_cant_contenedores_max() == 3
        