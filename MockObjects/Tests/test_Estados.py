from unittest import TestCase
from unittest.mock import Mock, patch, MagicMock

from pytest import raises
from ContenedoresDirectorio.Builder.Builder_contenedor import Contenedor_builder
from ContenedoresDirectorio.Director.Contenedor_director import Contenedor_director
from ContenedoresDirectorio.Contenedores import Contenedor
from ContenedoresDirectorio.Builder.BuilderContenedorBasico import BuilderContenedorBasico
from ContenedoresDirectorio.Builder.BuilderContenedorBasicoHc import BuilderContenedorBasicoHC
from ContenedoresDirectorio.Builder.BuilderContenedorFlatRack import BuilderContenedorFlatRack
from ContenedoresDirectorio.ManejadorDeCargas import ManejadorDeCargas
from Pedidos import Pedidos
from Cargas.Carga import Carga
from Cargas.Categorias import Categoria
from Medidas import Medidas

class TestEstados(TestCase):
    """MENOR A MIL"""
    def test_distancia_menor_100_por_peso_calcular_precio(self):
        medidas = Medidas(3,2,2)
        carga = Carga(medidas,50,Categoria.MAQUINARIA)
        carga2 = Carga(medidas,50,Categoria.MAQUINARIA)
        
        cargas = []
        cargas.append(carga)
        cargas.append(carga2)
        
        builder = BuilderContenedorBasicoHC()
        director = Contenedor_director(builder)
        
        contenedor = director.crear_contenedor(False)
        
        
        contenedor.set_precio_transporte_base(500) # cambio lo establecido por el tasador de cargas para tener mas control
        
        manejadorDeCargas = ManejadorDeCargas()
        manejadorDeCargas.cargar(carga, contenedor)
        
        manejadorDeCargas.cargar(carga2, contenedor) # inserto a la lista de cargas dos cargas, no tengo todavia metodo que crea y recorre conts y mete cargas
        
        # esta es la parte importante
        
        # y como las medidas son cualquiera, con ese peso deberia devolver 1000
        # ((1000 * (50 / float(100)))*2) = 1000
        # a eso se le suma el 500 de peso base que puse arriba
        

        assert contenedor.calcular_precio(99) == 1500
    
        
    def test_distancia_menor_100_contenedor_completo_calcular_precio(self):
        medidas = Medidas(12.0,2.35,2.3)
        carga = Carga(medidas,50,Categoria.MAQUINARIA)
        carga2 = Carga(medidas,50,Categoria.MAQUINARIA)
        
        cargas = []
        cargas.append(carga)
        cargas.append(carga2)
        
        
        builder = BuilderContenedorBasicoHC()
        director = Contenedor_director(builder)
        
        contenedor = director.crear_contenedor(False)
        
        
        # inserto a la lista de cargas dos cargas, no tengo todavia metodo que crea y recorre conts y mete cargas
        manejadorDeCargas = ManejadorDeCargas()
        manejadorDeCargas.cargar(carga, contenedor)
        
        # esta es la parte importante
        
        # y como las medidas son iguales al interior del contenedor me devuelve 400000 el calcular precio de estados
        contenedor.set_precio_transporte_base(500) # cambio lo establecido por el tasador de cargas para tener mas control

        # esta contemplado el caso en el que haya 2 cargas con medidas iguales a las medidas del cont, cuando se insertan las cargas en el contenedor
        
        assert contenedor.calcular_precio(99) == 200500
    
    #---------------------------------------------------------------------
    #---------------------------------------------------------------------
    #---------------------------------------------------------------------
    #---------------------------------------------------------------------
    #---------------------------------------------------------------------
    
    """MENOR A MIL"""
    
    def test_distancia_menor_1000_por_peso_calcular_precio(self):
        medidas = Medidas(3,2,2)
        carga = Carga(medidas,50,Categoria.MAQUINARIA)
        carga2 = Carga(medidas,50,Categoria.MAQUINARIA)
        
        cargas = []
        cargas.append(carga)
        cargas.append(carga2)
        
        builder = BuilderContenedorBasicoHC()
        director = Contenedor_director(builder)
        
        contenedor = director.crear_contenedor(False)
        

        
        # inserto a la lista de cargas dos cargas, no tengo todavia metodo que crea y recorre conts y mete cargas
        manejadorDeCargas = ManejadorDeCargas()
        manejadorDeCargas.cargar(carga, contenedor)
        manejadorDeCargas.cargar(carga2, contenedor)

        # esta es la parte importante
        
        # y como las medidas son cualquiera, con ese peso deberia devolver 500
        
        contenedor.set_precio_transporte_base(500) # cambio lo establecido por el tasador de cargas para tener mas control
        # 1100 + 500
        
        assert contenedor.calcular_precio(999) == 1600
    
    
    def test_distancia_menor_1000_contenedor_completo_calcular_precio(self):
        medidas = Medidas(12.0,2.35,2.3)
        carga = Carga(medidas,50,Categoria.MAQUINARIA)
        carga2 = Carga(medidas,50,Categoria.MAQUINARIA)
        
        cargas = []
        cargas.append(carga)
        
        builder = BuilderContenedorBasicoHC()
        director = Contenedor_director(builder)
        
        contenedor = director.crear_contenedor(False)
        
        
        # inserto a la lista de cargas dos cargas, no tengo todavia metodo que crea y recorre conts y mete cargas
        
        manejadorDeCargas = ManejadorDeCargas()
        manejadorDeCargas.cargar(carga, contenedor)
        
        # esta es la parte importante
        
        # y como las medidas son iguales al interior del contenedor me devuelve 200000 el calcular precio de estados
        
        
        contenedor.set_precio_transporte_base(500) # cambio lo establecido por el tasador de cargas para tener mas control
        # 210000 + 500
        
        assert contenedor.calcular_precio(999) == 210500

    
    def test_distancia_menor_10000_por_peso_calcular_precio(self):
        medidas = Medidas(3,2,2)
        carga = Carga(medidas,50,Categoria.MAQUINARIA)
        carga2 = Carga(medidas,50,Categoria.MAQUINARIA)
        
        cargas = []
        cargas.append(carga)
        cargas.append(carga2)
        
        
        builder = BuilderContenedorBasicoHC()
        director = Contenedor_director(builder)
        
        contenedor = director.crear_contenedor(False)

        
         # inserto a la lista de cargas dos cargas, no tengo todavia metodo que crea y recorre conts y mete cargas
        manejadorDeCargas = ManejadorDeCargas()
        manejadorDeCargas.cargar(carga, contenedor)
        manejadorDeCargas.cargar(carga2, contenedor)
        # esta es la parte importante
        
        # y como las medidas son cualquiera, con ese peso deberia devolver 500
        
        contenedor.set_precio_transporte_base(500) # cambio lo establecido por el tasador de cargas para tener mas control
        # 1100 + 500
        
        assert contenedor.calcular_precio(9999) == 1650
    
    def test_distancia_menor_10000_contenedor_completo_calcular_precio(self):
        medidas = Medidas(12.0,2.35,2.3)
        carga = Carga(medidas,50,Categoria.MAQUINARIA)
        carga2 = Carga(medidas,50,Categoria.MAQUINARIA)
        
        cargas = []
        cargas.append(carga)
        
        builder = BuilderContenedorBasicoHC()
        director = Contenedor_director(builder)
        
        contenedor = director.crear_contenedor(False)
        
        # inserto a la lista de cargas dos cargas, no tengo todavia metodo que crea y recorre conts y mete cargas
        manejadorDeCargas = ManejadorDeCargas()
        manejadorDeCargas.cargar(carga, contenedor)
        
        # esta es la parte importante
        
        # y como las medidas son iguales al interior del contenedor me devuelve 200000 el calcular precio de estados
        
        
        contenedor.set_precio_transporte_base(500) # cambio lo establecido por el tasador de cargas para tener mas control
        # 210000 + 500
        
        assert contenedor.calcular_precio(9999) == 230500
    
    
    def test_distancia_mas_10000_por_peso_calcular_precio(self):
        medidas = Medidas(3,2,2)
        carga = Carga(medidas,50,Categoria.MAQUINARIA)
        carga2 = Carga(medidas,50,Categoria.MAQUINARIA)
        
        cargas = []
        cargas.append(carga)
        cargas.append(carga2)
        
        
        builder = BuilderContenedorBasicoHC()
        director = Contenedor_director(builder)
        
        contenedor = director.crear_contenedor(False)
        

        
       # inserto a la lista de cargas dos cargas, no tengo todavia metodo que crea y recorre conts y mete cargas
    
        manejadorDeCargas = ManejadorDeCargas()
        manejadorDeCargas.cargar(carga, contenedor)
        manejadorDeCargas.cargar(carga2, contenedor)
        # esta es la parte importante
        
        # y como las medidas son cualquiera, con ese peso deberia devolver 500
        
        contenedor.set_precio_transporte_base(500) # cambio lo establecido por el tasador de cargas para tener mas control
        # 1100 + 500
        
        assert contenedor.calcular_precio(99999) == 2000
    
    
    def test_distancia_mas_10000_contenedor_completo_calcular_precio(self):
        medidas = Medidas(12.0,2.35,2.3)
        carga = Carga(medidas,50,Categoria.MAQUINARIA)
        carga2 = Carga(medidas,50,Categoria.MAQUINARIA)
        
        cargas = []
        cargas.append(carga)
        
        
        builder = BuilderContenedorBasicoHC()
        director = Contenedor_director(builder)
        
        contenedor = director.crear_contenedor(False)
        
        
         # inserto a la lista de cargas dos cargas, no tengo todavia metodo que crea y recorre conts y mete cargas
        manejadorDeCargas = ManejadorDeCargas()
        manejadorDeCargas.cargar(carga, contenedor)
        
        # esta es la parte importante
        
        # y como las medidas son iguales al interior del contenedor me devuelve 200000 el calcular precio de estados
        
        
        contenedor.set_precio_transporte_base(500) # cambio lo establecido por el tasador de cargas para tener mas control
        # 210000 + 500
        
        assert contenedor.calcular_precio(99999) == 250500
        
    