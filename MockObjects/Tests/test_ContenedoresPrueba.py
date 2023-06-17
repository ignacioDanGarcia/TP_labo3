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
from ContenedoresDirectorio.SelectoraEstrategiaPorCarga import SelectoraEstrategiaPorCarga

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
        contenedor = director.crear_contenedor(1,False)
        
        medidas = Medidas(100,3,5)
        carga = Carga(medidas,50,Categoria.MAQUINARIA)
        manejador_de_cargas = ManejadorDeCargas(SelectoraEstrategiaPorCarga())
        
        
        assert manejador_de_cargas.puede_cargar(carga, contenedor) == False
        
    
    def test_manejador_de_cargas_puede_cargar_carga_maquinaria_en_contenedor_hc(self):
        builder = BuilderContenedorBasicoHC()
        director = Contenedor_director(builder)
        contenedor = director.crear_contenedor(1,False)
        
        medidas = Medidas(3,2,2)
        carga = Carga(medidas,50,Categoria.MAQUINARIA)
        
        manejador_de_cargas = ManejadorDeCargas(SelectoraEstrategiaPorCarga())
        
        assert manejador_de_cargas.puede_cargar(carga, contenedor) == True
        
        manejador_de_cargas.cargar(carga, contenedor)
        assert len(contenedor.get_cargas()) == 1
        manejador_de_cargas.cargar(carga, contenedor)
        assert len(contenedor.get_cargas()) == 2

    
    
    def test_manejador_de_cargas_puede_cargar_carga_quimica_en_contenedor_hc(self):
        builder = BuilderContenedorBasicoHC()
        director = Contenedor_director(builder)
        contenedor = director.crear_contenedor(1,True)
        medidas = Medidas(3,2,2)
        carga = Carga(medidas,50,Categoria.QUIMICA)
        
        manejador_de_cargas = ManejadorDeCargas(SelectoraEstrategiaPorCarga())

        assert manejador_de_cargas.puede_cargar(carga, contenedor) == True
    
    
    def test_manejador_de_cargas_puede_cargar_carga_quimica_en_contenedor_flatrack(self):
        builder = BuilderContenedorFlatRack()
        director = Contenedor_director(builder)
        contenedor = director.crear_contenedor(1,True)
        medidas = Medidas(3,2,2)
        carga = Carga(medidas,50,Categoria.QUIMICA)
        
        manejador_de_cargas = ManejadorDeCargas(SelectoraEstrategiaPorCarga())

        manejador_de_cargas.cargar(carga,contenedor)
        assert len(contenedor.get_cargas()) == 1
        manejador_de_cargas.cargar(carga,contenedor)
        assert len(contenedor.get_cargas()) == 2
    
    
    def test_manejador_de_cargas_puede_cargar_carga_maquinaria_en_contenedor_flatrack(self):
        builder = BuilderContenedorFlatRack()
        director = Contenedor_director(builder)
        contenedor = director.crear_contenedor(1,True)
        medidas = Medidas(3,2,2)
        carga = Carga(medidas,50,Categoria.MAQUINARIA)
        
        manejador_de_cargas = ManejadorDeCargas(SelectoraEstrategiaPorCarga())

        assert len(contenedor.get_cargas()) == 0
        
        assert(manejador_de_cargas.verificar_carga(carga, contenedor)) == True
        manejador_de_cargas.cargar(carga,contenedor)
        assert len(contenedor.get_cargas()) == 1
    
    
    def test_manejador_de_cargas_no_puede_cargar_carga_maquinaria_en_contenedor_flatrack_por_medidas_superiores(self):
        builder = BuilderContenedorFlatRack()
        director = Contenedor_director(builder)
        contenedor = director.crear_contenedor(1,False)
        medidas = Medidas(100,3,5)
        carga = Carga(medidas,50,Categoria.MAQUINARIA)
        
        manejador_de_cargas = ManejadorDeCargas(SelectoraEstrategiaPorCarga())
        
        assert manejador_de_cargas.verificar_carga(carga, contenedor) == False
            
        assert manejador_de_cargas.cargar(carga,contenedor) == False
        
    
    def test_manejador_de_cargas_no_puede_cargar_carga_quimica_en_contenedor_flatrack_porque_ya_habia_carga_maquinaria(self):
        builder = BuilderContenedorBasico()
        director = Contenedor_director(builder)
        contenedor = director.crear_contenedor(1,False)
        medidas = Medidas(3,2,2)
        carga = Carga(medidas,50,Categoria.MAQUINARIA)
        manejador_de_cargas = ManejadorDeCargas(SelectoraEstrategiaPorCarga())

        assert(manejador_de_cargas.verificar_carga(carga, contenedor)) == True

        manejador_de_cargas.cargar(carga, contenedor)
        assert len(contenedor.get_cargas()) == 1
        manejador_de_cargas.cargar(carga, contenedor)
        assert len(contenedor.get_cargas()) == 2

        carga_especial = Carga(medidas,50,Categoria.QUIMICA)
        assert manejador_de_cargas.cargar(carga_especial, contenedor) == False

        assert len(contenedor.get_cargas()) == 2

    
    def test_manejador_de_cargas_no_puede_cargar_carga_quimica_en_contenedor_ventilado_porque_ya_habia_carga_alimenticia(self):
        builder = BuilderContenedorVentilado()
        director = Contenedor_director(builder)
        contenedor_ventilado = director.crear_contenedor(1,True)
        
        medidas = Medidas(3,2,2)
        carga = Carga(medidas,50,Categoria.ALIMENTICIA)
        manejador_de_cargas = ManejadorDeCargas(SelectoraEstrategiaPorCarga())
        
        assert(manejador_de_cargas.verificar_carga(carga,contenedor_ventilado)) == True
        manejador_de_cargas.cargar(carga, contenedor_ventilado)
        
        carga_quimica = Carga(medidas,1,Categoria.QUIMICA)
        assert(manejador_de_cargas.verificar_carga(carga_quimica,contenedor_ventilado)) == False 
        assert manejador_de_cargas.cargar(carga_quimica, contenedor_ventilado) == False

    
    def test_manejador_de_cargas_no_puede_cargar_carga_alimenticia_en_contenedor_hc_porque_ya_habia_carga_quimica(self):
        builder = BuilderContenedorBasicoHC()
        director = Contenedor_director(builder)
        contenedorhc = director.crear_contenedor(1,True)
        
        medidas = Medidas(3,2,2)
        carga = Carga(medidas,50,Categoria.QUIMICA)
        manejador_de_cargas = ManejadorDeCargas(SelectoraEstrategiaPorCarga())
        
        assert(manejador_de_cargas.verificar_carga(carga,contenedorhc)) == True
        manejador_de_cargas.cargar(carga, contenedorhc)
        
        carga_quimica = Carga(medidas,1,Categoria.ALIMENTICIA)
        assert(manejador_de_cargas.verificar_carga(carga_quimica,contenedorhc)) == False
        
