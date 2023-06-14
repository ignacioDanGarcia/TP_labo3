from unittest import TestCase
from unittest.mock import Mock
from ContenedoresDirectorio.Builder.BuilderContenedorBasicoHc import BuilderContenedorBasicoHC
from ContenedoresDirectorio.Builder.BuilderContenedorBasico import BuilderContenedorBasico
from ContenedoresDirectorio.Builder.BuilderContenedorFlatRack import BuilderContenedorFlatRack
from ContenedoresDirectorio.Director.Contenedor_director import Contenedor_director
from ContenedoresDirectorio.Contenedores import Contenedor
from Medidas import Medidas


class ContenedorBuilderTest(TestCase):
    
    def test_crear_contenedor_simple(self):
        builder = BuilderContenedorBasico()
        director = Contenedor_director(builder)
        contenedor = director.crear_contenedor(None)
        
        assert isinstance(contenedor, Contenedor) == True
        assert contenedor.tipo == "Basico estandar"
        assert contenedor.volumen_max == 32.6
        assert contenedor.peso_max == 24000
        
        assert contenedor.get_medidas_interior().alto == 2.3
        assert contenedor.get_medidas_interior().ancho == 2.35
        assert contenedor.get_medidas_interior().largo == 6.0
        
        assert contenedor.get_medidas_exterior().alto == 2.6
        assert contenedor.get_medidas_exterior().ancho == 2.45
        assert contenedor.get_medidas_exterior().largo == 6.1
        

        
        
        
    def test_crear_contenedor_hc(self):
        builder = BuilderContenedorBasicoHC()
        director = Contenedor_director(builder)
        contenedor = director.crear_contenedor(None)
        
        assert isinstance(contenedor, Contenedor) == True
        assert contenedor.tipo == "Basico HC"
        assert contenedor.volumen_max == 67.7
        assert contenedor.peso_max == 32500
        
        assert contenedor.get_medidas_interior().alto == 2.3
        assert contenedor.get_medidas_interior().ancho == 2.35
        assert contenedor.get_medidas_interior().largo == 12.0
        
        assert contenedor.get_medidas_exterior().alto == 2.6
        assert contenedor.get_medidas_exterior().ancho == 2.45
        assert contenedor.get_medidas_exterior().largo == 12.1
        
        
    def test_crear_contenedor_flatrack(self):
        builder = BuilderContenedorFlatRack()
        director = Contenedor_director(builder)
        contenedor = director.crear_contenedor(None)

        assert isinstance(contenedor, Contenedor) == True
        assert contenedor.tipo == "Flat Rack"
        
        assert contenedor.get_medidas_interior().alto == 2.3
        assert contenedor.get_medidas_interior().ancho == 100000
        assert contenedor.get_medidas_interior().largo == 6.0
        
        assert contenedor.get_medidas_exterior().alto == 2.3
        assert contenedor.get_medidas_exterior().ancho == 100000
        assert contenedor.get_medidas_exterior().largo == 6.1
        
    def test_change_builder(self):
        builder = BuilderContenedorFlatRack()
        director = Contenedor_director(builder)
        builder2 = BuilderContenedorBasico()
        director.change_builder(builder2)
        
        assert isinstance(director.builder, BuilderContenedorBasico) == True