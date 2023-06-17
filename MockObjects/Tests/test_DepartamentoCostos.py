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
from Excepciones.exceptions import distancia_incorrecta
from Pedidos import Pedidos
from Cargas.Carga import Carga
from Cargas.Categorias import Categoria
from Medidas import Medidas

from EmpresaDirectorio.EmpresaOficina import EmpresaOficina

class TestDepartamentoCostos(TestCase):
    """MENOR A MIL"""
    def test_distancia_menor_100_por_peso_calcular_precio(self):
        medidas = Medidas(3,2,2)
        carga = Carga(medidas,50,Categoria.MAQUINARIA)
        
        cargas = [carga]
        
        
        mock_contenedor = Mock()
        mock_contenedor.get_cargas.return_value = cargas
        mock_contenedor.get_precio_transporte_base.return_value = 500
        mock_contenedor.get_medidas_interior.return_value = Medidas(12.0,2.35,2.3)
    
        distancia = 99
        oficina = EmpresaOficina()
        
        assert oficina.calcular_precio(mock_contenedor, distancia) == 1000
    
        
    def test_distancia_menor_100_contenedor_completo_calcular_precio(self):
        medidas = Medidas(12.0,2.35,2.3)
        carga = Carga(medidas,50,Categoria.MAQUINARIA)
        
        cargas = [carga]
        
        mock_contenedor = Mock()
        
        # aca podria ir un tasador_contenedor = TasadorDeContenedores()
        # tasador_contenedor(contenedor)
        
        mock_contenedor.get_cargas.return_value = cargas
        mock_contenedor.get_precio_transporte_base.return_value = 500
        mock_contenedor.get_medidas_interior.return_value = medidas
        distancia = 99
        oficina = EmpresaOficina()
        
        assert oficina.calcular_precio(mock_contenedor, distancia) == 200500
    
    #---------------------------------------------------------------------
    #---------------------------------------------------------------------
    #---------------------------------------------------------------------
    #---------------------------------------------------------------------
    #---------------------------------------------------------------------
    
    """MENOR A MIL"""
    
    def test_distancia_menor_1000_por_peso_calcular_precio(self):
        medidas = Medidas(3,2,2)
        carga = Carga(medidas,50,Categoria.MAQUINARIA)
        
        cargas = [carga]
        
        
        mock_contenedor = Mock()
        mock_contenedor.get_cargas.return_value = cargas
        mock_contenedor.get_precio_transporte_base.return_value = 500
        mock_contenedor.get_medidas_interior.return_value = Medidas(12.0,2.35,2.3)
        
        # 550 + 500
        distancia = 999
        oficina = EmpresaOficina()
        
        assert oficina.calcular_precio(mock_contenedor, distancia) == 1050
    
    
    def test_distancia_menor_1000_contenedor_completo_calcular_precio(self):
        medidas = Medidas(12.0,2.35,2.3)
        carga = Carga(medidas,50,Categoria.MAQUINARIA)
        
        cargas = [carga]
        
        
        mock_contenedor = Mock()
        mock_contenedor.get_cargas.return_value = cargas
        mock_contenedor.get_precio_transporte_base.return_value = 500
        mock_contenedor.get_medidas_interior.return_value = medidas
        
        distancia = 999
        oficina = EmpresaOficina()
        
        assert oficina.calcular_precio(mock_contenedor, distancia) == 210500

    
    def test_distancia_menor_10000_por_peso_calcular_precio(self):
        medidas = Medidas(3,2,2)
        carga = Carga(medidas,50,Categoria.MAQUINARIA)
        cargas = [carga]
        mock_contenedor = Mock()
        mock_contenedor.get_cargas.return_value = cargas
        mock_contenedor.get_precio_transporte_base.return_value = 500
        mock_contenedor.get_medidas_interior.return_value = Medidas(12.0,2.35,2.3)
        
        distancia = 9999
        oficina = EmpresaOficina()
        
        assert oficina.calcular_precio(mock_contenedor, distancia) == 1075
    
    def test_distancia_menor_10000_contenedor_completo_calcular_precio(self):
        medidas = Medidas(12.0,2.35,2.3)
        carga = Carga(medidas,50,Categoria.MAQUINARIA)
        
        cargas = [carga]
        
        
        mock_contenedor = Mock()
        mock_contenedor.get_cargas.return_value = cargas
        mock_contenedor.get_precio_transporte_base.return_value = 500
        mock_contenedor.get_medidas_interior.return_value = medidas
        
        distancia = 9999
        oficina = EmpresaOficina()
        
        assert oficina.calcular_precio(mock_contenedor, distancia) == 230500
    
    
    def test_distancia_mas_10000_por_peso_calcular_precio(self):
        medidas = Medidas(3,2,2)
        carga = Carga(medidas,50,Categoria.MAQUINARIA)
        
        cargas = [carga]
        mock_contenedor = Mock()
        mock_contenedor.get_cargas.return_value = cargas
        mock_contenedor.get_precio_transporte_base.return_value = 500
        mock_contenedor.get_medidas_interior.return_value = Medidas(12.0,2.35,2.3)
        
        # 750 + 500 = 1250
        distancia = 99999
        oficina = EmpresaOficina()
        
        assert oficina.calcular_precio(mock_contenedor, distancia) == 1250
    
    
    def test_distancia_mas_10000_contenedor_completo_calcular_precio(self):
        medidas = Medidas(12.0,2.35,2.3)
        carga = Carga(medidas,50,Categoria.MAQUINARIA)
        
        cargas = [carga]
        
        
        mock_contenedor = Mock()
        mock_contenedor.get_cargas.return_value = cargas
        mock_contenedor.get_precio_transporte_base.return_value = 500
        mock_contenedor.get_medidas_interior.return_value = medidas
        
        distancia = 99999
        oficina = EmpresaOficina()
        
        assert oficina.calcular_precio(mock_contenedor, distancia) == 250500
        
        """Distancia 0"""
    def test_distancia_es_0_por_peso_calcular_precio(self):
        medidas = Medidas(3,2,2)
        carga = Carga(medidas,50,Categoria.MAQUINARIA)
        
        cargas = [carga]
        
        
        mock_contenedor = Mock()
        mock_contenedor.get_cargas.return_value = cargas
        mock_contenedor.get_precio_transporte_base.return_value = 500
        mock_contenedor.get_medidas_interior.return_value = Medidas(12.0,2.35,2.3)
    
        distancia = 0
        oficina = EmpresaOficina()
        
        
        with self.assertRaises(distancia_incorrecta):
            oficina.calcular_precio(mock_contenedor, distancia)
    
    """Distancia es menor a 0"""
    def test_distancia_es_menor_a_0_por_peso_calcular_precio(self):
        medidas = Medidas(3,2,2)
        carga = Carga(medidas,50,Categoria.MAQUINARIA)
        
        cargas = [carga]
        
        
        mock_contenedor = Mock()
        mock_contenedor.get_cargas.return_value = cargas
        mock_contenedor.get_precio_transporte_base.return_value = 500
        mock_contenedor.get_medidas_interior.return_value = Medidas(12.0,2.35,2.3)
    
        distancia = -100
        oficina = EmpresaOficina()
        
        
        with self.assertRaises(distancia_incorrecta):
            oficina.calcular_precio(mock_contenedor, distancia)
        
        