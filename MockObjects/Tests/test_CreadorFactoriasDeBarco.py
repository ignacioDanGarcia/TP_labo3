from unittest import TestCase
from unittest.mock import Mock, patch, MagicMock
from BarcosDirectorio.Factory.CreadorDeBarcosBasicos import CreadorBarcosBasicos
from BarcosDirectorio.Factory.CreadorDeBarcosEspeciales import CreadorBarcosEspeciales
from BarcosDirectorio.Factory.SelectorDeCreador import SelectorCreador
from BarcosDirectorio.TiposDeBarcos import TiposBarcos
class test_creacion_de_barcos_con_factory_method(TestCase):
    
    def test_creacion_de_factoria_de_barcos_basicos(self):
        selector = SelectorCreador()
        factoria = selector.crear_factoria(TiposBarcos.BASICO)
        assert isinstance(factoria, CreadorBarcosBasicos)
    
    def test_creacion_de_factoria_de_barcos_especiales(self):
        selector = SelectorCreador()
        factoria = selector.crear_factoria(TiposBarcos.ESPECIAL)
        assert isinstance(factoria, CreadorBarcosEspeciales)
    
    def test_creacion_de_factoria_errors(self):
        selector = SelectorCreador()
        with self.assertRaises(AttributeError):
            factoria = selector.crear_factoria(TiposBarcos.Inexistente)
        
        