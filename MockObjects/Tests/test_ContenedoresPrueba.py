from types import NoneType
from unittest import TestCase
from unittest.mock import Mock, patch, MagicMock

from Cargas.Carga import Carga
from Cargas.Categorias import Categoria
from ContenedoresDirectorio.Contenedores import Contenedor
from ContenedoresDirectorio.Builder.Builder_contenedor import Contenedor_builder
from ContenedoresDirectorio.Builder.BuilderContenedorBasico import BuilderContenedorBasico
from ContenedoresDirectorio.Builder.BuilderContenedorBasicoHc import BuilderContenedorBasicoHC
from ContenedoresDirectorio.Builder.BuilderContenedorFlatRack import BuilderContenedorFlatRack
from ContenedoresDirectorio.Builder.BuilderContenedorVentilado import BuilderContenedorVentilado

from ContenedoresDirectorio.Director.Contenedor_director import Contenedor_director
from ContenedoresDirectorio.ManejadorDeCargas import ManejadorDeCargas

from pytest import raises
from Excepciones.exceptions import *
from Medidas import Medidas

class TestContenedoresPrueba(TestCase):
     
    """ 
    5. Cualquier carga cuyas dimensiones, volumen o peso supere lo definido en el container no podrá ser trasladada en el mismo.
    6. Un contenedor sin características especiales no puede transportar material especial.
    """
        
    def test_manejador_de_cargas_no_puede_cargar_carga_maquinaria_en_contenedor_hc_por_medidas_superiores(self):
        builder = BuilderContenedorBasicoHC()
        director = Contenedor_director(builder)
        contenedor = director.crear_contenedor(False)
        
        medidas = Medidas(100,3,5)
        carga = Carga(medidas,50,Categoria.MAQUINARIA)
        manejadorDeCarga = ManejadorDeCargas()
        
        
        assert manejadorDeCarga.puede_cargar(carga, contenedor) == False
        
    
    def test_manejador_de_cargas_puede_cargar_carga_maquinaria_en_contenedor_hc(self):
        builder = BuilderContenedorBasicoHC()
        director = Contenedor_director(builder)
        contenedor = director.crear_contenedor(False)
        
        medidas = Medidas(3,2,2)
        carga = Carga(medidas,50,Categoria.MAQUINARIA)
        
        manejadorDeCarga = ManejadorDeCargas()
        
        assert manejadorDeCarga.puede_cargar(carga, contenedor) == True
        
        manejadorDeCarga.cargar(carga, contenedor)
        assert len(contenedor.get_cargas()) == 1
        manejadorDeCarga.cargar(carga, contenedor)
        assert len(contenedor.get_cargas()) == 2

    
    
    def test_manejador_de_cargas_puede_cargar_carga_quimica_en_contenedor_hc(self):
        builder = BuilderContenedorBasicoHC()
        director = Contenedor_director(builder)
        contenedor = director.crear_contenedor(True)
        medidas = Medidas(3,2,2)
        carga = Carga(medidas,50,Categoria.QUIMICA)
        
        manejadorDeCarga = ManejadorDeCargas()

        assert manejadorDeCarga.puede_cargar(carga, contenedor) == True
    
    
    def test_manejador_de_cargas_puede_cargar_carga_quimica_en_contenedor_flatrack(self):
        builder = BuilderContenedorFlatRack()
        director = Contenedor_director(builder)
        contenedor = director.crear_contenedor(True)
        medidas = Medidas(3,2,2)
        carga = Carga(medidas,50,Categoria.QUIMICA)
        
        manejadorDeCarga = ManejadorDeCargas()

        manejadorDeCarga.cargar(carga,contenedor)
        assert len(contenedor.get_cargas()) == 1
        manejadorDeCarga.cargar(carga,contenedor)
        assert len(contenedor.get_cargas()) == 2
    
    
    def test_manejador_de_cargas_puede_cargar_carga_maquinaria_en_contenedor_flatrack(self):
        builder = BuilderContenedorFlatRack()
        director = Contenedor_director(builder)
        contenedor = director.crear_contenedor(True)
        medidas = Medidas(3,2,2)
        carga = Carga(medidas,50,Categoria.MAQUINARIA)
        
        manejadorDeCarga = ManejadorDeCargas()

        assert len(contenedor.get_cargas()) == 0
        
        assert(manejadorDeCarga.verificar_carga(carga, contenedor)) == True
        manejadorDeCarga.cargar(carga,contenedor)
        assert len(contenedor.get_cargas()) == 1
    
    
    def test_manejador_de_cargas_no_puede_cargar_carga_maquinaria_en_contenedor_flatrack_por_medidas_superiores(self):
        builder = BuilderContenedorFlatRack()
        director = Contenedor_director(builder)
        contenedor = director.crear_contenedor(False)
        medidas = Medidas(100,3,5)
        carga = Carga(medidas,50,Categoria.MAQUINARIA)
        
        manejadorDeCarga = ManejadorDeCargas()
        
        assert manejadorDeCarga.verificar_carga(carga, contenedor) == False
            
        assert manejadorDeCarga.cargar(carga,contenedor) == False
        
    
    def test_manejador_de_cargas_no_puede_cargar_carga_quimica_en_contenedor_flatrack_porque_ya_habia_carga_maquinaria(self):
        builder = BuilderContenedorBasico()
        director = Contenedor_director(builder)
        contenedor = director.crear_contenedor(False)
        medidas = Medidas(3,2,2)
        carga = Carga(medidas,50,Categoria.MAQUINARIA)
        manejadorDeCarga = ManejadorDeCargas()

        assert(manejadorDeCarga.verificar_carga(carga, contenedor)) == True

        manejadorDeCarga.cargar(carga, contenedor)
        assert len(contenedor.get_cargas()) == 1
        manejadorDeCarga.cargar(carga, contenedor)
        assert len(contenedor.get_cargas()) == 2

        carga_especial = Carga(medidas,50,Categoria.QUIMICA)
        assert manejadorDeCarga.cargar(carga_especial, contenedor) == False

        assert len(contenedor.get_cargas()) == 2

    
    def test_manejador_de_cargas_no_puede_cargar_carga_quimica_en_contenedor_ventilado_porque_ya_habia_carga_alimenticia(self):
        builder = BuilderContenedorVentilado()
        director = Contenedor_director(builder)
        contenedorVentilado = director.crear_contenedor(True)
        
        medidas = Medidas(3,2,2)
        carga = Carga(medidas,50,Categoria.ALIMENTICIA)
        manejadorDeCarga = ManejadorDeCargas()
        
        assert(manejadorDeCarga.verificar_carga(carga,contenedorVentilado)) == True
        manejadorDeCarga.cargar(carga, contenedorVentilado)
        
        carga_quimica = Carga(medidas,1,Categoria.QUIMICA)
        assert(manejadorDeCarga.verificar_carga(carga_quimica,contenedorVentilado)) == False 
        assert manejadorDeCarga.cargar(carga_quimica, contenedorVentilado) == False

    
    def test_manejador_de_cargas_no_puede_cargar_carga_alimenticia_en_contenedor_hc_porque_ya_habia_carga_quimica(self):
        builder = BuilderContenedorBasicoHC()
        director = Contenedor_director(builder)
        contenedorhc = director.crear_contenedor(True)
        
        medidas = Medidas(3,2,2)
        carga = Carga(medidas,50,Categoria.QUIMICA)
        manejadorDeCarga = ManejadorDeCargas()
        
        assert(manejadorDeCarga.verificar_carga(carga,contenedorhc)) == True
        manejadorDeCarga.cargar(carga, contenedorhc)
        
        carga_quimica = Carga(medidas,1,Categoria.ALIMENTICIA)
        assert(manejadorDeCarga.verificar_carga(carga_quimica,contenedorhc)) == False
        
