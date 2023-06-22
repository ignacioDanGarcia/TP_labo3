from unittest import TestCase
from BarcosDirectorio.Factory.SelectorDeCreador import SelectorCreador
from BarcosDirectorio.TiposDeBarcos import TiposBarcos
from BarcosDirectorio.Factory.CreadorBarcos import CreadorDeBarcos
from BarcosDirectorio.Factory.SelectorDeCreador import SelectorCreador

class test_creacion_de_barcos_con_factory_method(TestCase):
    
    def test_creacion_de_factoria_de_barcos_basicos(self):
        selector = SelectorCreador()
        factoria = selector.crear_factoria_de_tipo_de_barco(TiposBarcos.BASICO)
        assert isinstance(factoria, CreadorDeBarcos)
        assert factoria.get_tipoBarco() == TiposBarcos.BASICO
    
    def test_creacion_de_factoria_de_barcos_especiales(self):
        selector = SelectorCreador()
        
        factoria = selector.crear_factoria_de_tipo_de_barco(TiposBarcos.ESPECIAL)
        assert isinstance(factoria, CreadorDeBarcos)
        assert factoria.get_tipoBarco() == TiposBarcos.ESPECIAL

    def test_creacion_de_factoria_errors(self):
        selector = SelectorCreador()
        with self.assertRaises(AttributeError):
            factoria = selector.crear_factoria_de_tipo_de_barco(TiposBarcos.Inexistente)
        
        