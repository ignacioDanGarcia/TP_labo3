from unittest import TestCase
from unittest.mock import Mock
from ContenedoresDirectorio.Builder.BuilderContenedorBasicoHc import BuilderContenedorBasicoHC
from ContenedoresDirectorio.Builder.BuilderContenedorBasico import BuilderContenedorBasico
from ContenedoresDirectorio.Builder.BuilderContenedorFlatRack import BuilderContenedorFlatRack
from ContenedoresDirectorio.Builder.BuilderContenedorVentilado import BuilderContenedorVentilado
from ContenedoresDirectorio.Builder.BuilderContenedorOpenTop import BuilderContenedorOpenTop

from ContenedoresDirectorio.Director.Contenedor_director import Contenedor_director
from ContenedoresDirectorio.Contenedores import Contenedor
from ContenedoresDirectorio.TiposDeContenedores.Tipo import TipoContenedor
from Medidas import Medidas


class ContenedorBuilderTest(TestCase):
    
    def test_crear_contenedor_basico_con_builder_chequea_sus_atributos_y_metodos(self):
        builder = BuilderContenedorBasico()
        director = Contenedor_director(builder)
        contenedor = director.crear_contenedor(1,False)
        
        assert isinstance(contenedor, Contenedor) == True
        assert contenedor.tipo == TipoContenedor.BASICO
        assert contenedor.volumen_max == 32.6
        assert contenedor.peso_max == 24000
        
        assert contenedor.get_medidas_interior().alto == 2.3
        assert contenedor.get_medidas_interior().ancho == 2.35
        assert contenedor.get_medidas_interior().largo == 6.0
        
        assert contenedor.get_medidas_exterior().alto == 2.6
        assert contenedor.get_medidas_exterior().ancho == 2.45
        assert contenedor.get_medidas_exterior().largo == 6.1
        
        
    def test_crear_contenedor_hc_con_builder_chequea_sus_atributos_y_metodos(self):
        builder = BuilderContenedorBasicoHC()
        director = Contenedor_director(builder)
        contenedor = director.crear_contenedor(1,True)
        
        assert isinstance(contenedor, Contenedor) == True
        assert contenedor.tipo == TipoContenedor.BASICOHC
        assert contenedor.volumen_max == 67.7
        assert contenedor.peso_max == 32500
        
        assert contenedor.get_medidas_interior().alto == 2.3
        assert contenedor.get_medidas_interior().ancho == 2.35
        assert contenedor.get_medidas_interior().largo == 12.0
        
        assert contenedor.get_medidas_exterior().alto == 2.6
        assert contenedor.get_medidas_exterior().ancho == 2.45
        assert contenedor.get_medidas_exterior().largo == 12.1
        
        
    def test_crear_contenedor_flatrack_con_builder_chequea_sus_atributos_y_metodos(self):
        builder = BuilderContenedorFlatRack()
        director = Contenedor_director(builder)
        contenedor = director.crear_contenedor(1,True)

        assert isinstance(contenedor, Contenedor) == True
        assert contenedor.tipo == TipoContenedor.FLATRACK
        
        assert contenedor.get_medidas_interior().alto == 2.3
        assert contenedor.get_medidas_interior().ancho == 100000
        assert contenedor.get_medidas_interior().largo == 6.0
        
        assert contenedor.get_medidas_exterior().alto == 2.3
        assert contenedor.get_medidas_exterior().ancho == 100000
        assert contenedor.get_medidas_exterior().largo == 6.1
        
    def test_cambio_de_builder_teniendo_otro_builder_previamente(self):
        builder = BuilderContenedorFlatRack()
        director = Contenedor_director(builder)
        builder2 = BuilderContenedorBasico()
        
        contenedor_FR = director.crear_contenedor(1,False)
        director.change_builder(builder2)
        contenedor_basico = director.crear_contenedor(2,False)
        assert contenedor_FR.tipo == TipoContenedor.FLATRACK
        assert contenedor_basico.tipo == TipoContenedor.BASICO
        assert isinstance(director.builder, BuilderContenedorBasico) == True
    
    def test_crear_contenedor_ventilado_con_builder_chequea_sus_atributos_y_metodos(self):
        builder = BuilderContenedorVentilado()
        director = Contenedor_director(builder)
        contenedorVentilado = director.crear_contenedor(1,True)
        assert isinstance(contenedorVentilado, Contenedor) == True
        assert contenedorVentilado.tipo == TipoContenedor.VENTILADO
        assert contenedorVentilado.volumen_max == 32.6
        assert contenedorVentilado.peso_max == 24000
        
        assert contenedorVentilado.get_medidas_interior().alto == 2.3
        assert contenedorVentilado.get_medidas_interior().ancho == 2.35
        assert contenedorVentilado.get_medidas_interior().largo == 6.0
        
        assert contenedorVentilado.get_medidas_exterior().alto == 2.6
        assert contenedorVentilado.get_medidas_exterior().ancho == 2.45
        assert contenedorVentilado.get_medidas_exterior().largo == 6.1
        
    def test_crear_contenedor_opentop_con_builder_chequea_sus_atributos_y_metodos(self):
        builder = BuilderContenedorOpenTop()
        director = Contenedor_director(builder)
        contenedorOpenTop = director.crear_contenedor(1,True)
        assert isinstance(contenedorOpenTop, Contenedor) == True
        assert contenedorOpenTop.tipo == TipoContenedor.OPENTOP
        assert contenedorOpenTop.volumen_max == 33
        assert contenedorOpenTop.peso_max == 45000
        
        assert contenedorOpenTop.get_medidas_interior().largo == 12.0
        assert contenedorOpenTop.get_medidas_interior().ancho == 2.35
        assert contenedorOpenTop.get_medidas_interior().alto == 100000
        
        assert contenedorOpenTop.get_medidas_exterior().largo == 12.1
        assert contenedorOpenTop.get_medidas_exterior().ancho == 2.45
        assert contenedorOpenTop.get_medidas_exterior().alto == 100000    