from types import NoneType
from unittest import TestCase
from unittest.mock import Mock, patch, MagicMock
import mock
from Carga import Carga
from ContenedoresDirectorio.Contenedores import Contenedor
from ContenedoresDirectorio.Builder.Builder_contenedor import Contenedor_builder
from ContenedoresDirectorio.Builder.BuilderContenedorBasico import BuilderContenedorBasico
from ContenedoresDirectorio.Builder.BuilderContenedorBasicoHc import BuilderContenedorBasicoHC
from ContenedoresDirectorio.Builder.BuilderContenedorFlatRack import BuilderContenedorFlatRack
from ContenedoresDirectorio.Director.Contenedor_director import Contenedor_director
from ContenedoresDirectorio.ManejadorDeCargas import ManejadorDeCargas

from pytest import raises
from Excepciones.exceptions import *
from Medidas import Medidas

class TestContenedoresPrueba(TestCase):
     
    """ 5. Cualquier carga cuyas dimensiones, volumen o peso supere lo definido en el container no podrá ser trasladada en el mismo.
    6. Un contenedor sin características especiales no puede transportar material especial. """
        
    def test_verificar_carga_por_dimensioneshc1(self):
        builder = BuilderContenedorBasicoHC()
        director = Contenedor_director(builder)
        contenedor = director.crear_contenedor(None)
        
        medidas = Medidas(100,3,5)
        carga = Carga(medidas,50,None)
        manejadorDeCarga = ManejadorDeCargas()
        
        
        assert manejadorDeCarga.puede_cargar(carga, contenedor) == False
        'medidas superiores'
        
        
    
    def test_verificar_carga_por_dimensioneshc2(self):
        builder = BuilderContenedorBasicoHC()
        director = Contenedor_director(builder)
        contenedor = director.crear_contenedor(None)
        
        medidas = Medidas(3,2,2)
        carga = Carga(medidas,50,None)
        
        manejadorDeCarga = ManejadorDeCargas()
        
        assert manejadorDeCarga.puede_cargar(carga, contenedor) == True
        
        manejadorDeCarga.cargar(carga, contenedor)
        assert len(contenedor.get_cargas()) == 1
        manejadorDeCarga.cargar(carga, contenedor)
        assert len(contenedor.get_cargas()) == 2

        
    'Tiene medidas que si entran'
    
    
    def test_verificar_carga_por_material_especialhc1(self):
        builder = BuilderContenedorBasicoHC()
        director = Contenedor_director(builder)
        contenedor = director.crear_contenedor(None)
        medidas = Medidas(3,2,2)
        carga = Carga(medidas,50,True)
        
        manejadorDeCarga = ManejadorDeCargas()

        assert manejadorDeCarga.puede_cargar(carga, contenedor) == False
        'Tiene medidas que entran pero el contenido es especial en un basico.'
    
    
    
    def test_verificar_carga_por_material_especial_flatrack1(self):
        builder = BuilderContenedorFlatRack()
        director = Contenedor_director(builder)
        contenedor = director.crear_contenedor(None)
        medidas = Medidas(3,2,2)
        carga = Carga(medidas,50,True)
        
        manejadorDeCarga = ManejadorDeCargas()

        manejadorDeCarga.cargar(carga,contenedor)
        assert len(contenedor.get_cargas()) == 1
        manejadorDeCarga.cargar(carga,contenedor)
        assert len(contenedor.get_cargas()) == 2
        'Tiene medidas que entran y el contenido es especial en un especial.'
    
    
    
    def test_verificar_carga_por_material_especial_flatrack2(self):
        builder = BuilderContenedorFlatRack()
        director = Contenedor_director(builder)
        contenedor = director.crear_contenedor(None)
        medidas = Medidas(3,2,2)
        carga = Carga(medidas,50,False)
        
        manejadorDeCarga = ManejadorDeCargas()

        assert len(contenedor.get_cargas()) == 0
        
        assert(manejadorDeCarga.verificar_carga(carga, contenedor)) == True
        manejadorDeCarga.cargar(carga,contenedor)
        assert len(contenedor.get_cargas()) == 1
        'Tiene medidas que entran y el contenido no es especial en un especial.'
    
    
    
    def test_verificar_carga_por_dimensiones_flatrack(self):
        builder = BuilderContenedorFlatRack()
        director = Contenedor_director(builder)
        contenedor = director.crear_contenedor(None)
        medidas = Medidas(100,3,5)
        carga = Carga(medidas,50,None)
        
        manejadorDeCarga = ManejadorDeCargas()
        
        assert manejadorDeCarga.verificar_carga(carga, contenedor) == False
            
        assert manejadorDeCarga.cargar(carga,contenedor) == False
        'medidas superiores'
        
    
    def test_verificar_carga_por_dimensiones_basico_y_carga_con_material_especial(self):
        builder = BuilderContenedorBasico()
        director = Contenedor_director(builder)
        contenedor = director.crear_contenedor(None)
        medidas = Medidas(3,2,2)
        carga = Carga(medidas,50,None)
        manejadorDeCarga = ManejadorDeCargas()

        assert(manejadorDeCarga.verificar_carga(carga, contenedor)) == True

        manejadorDeCarga.cargar(carga, contenedor)
        assert len(contenedor.get_cargas()) == 1
        manejadorDeCarga.cargar(carga, contenedor)
        assert len(contenedor.get_cargas()) == 2

        carga_especial = Carga(medidas,50,True)
        assert manejadorDeCarga.cargar(carga_especial, contenedor) == False

        assert len(contenedor.get_cargas()) == 2

        
    'Tiene medidas que si entran'