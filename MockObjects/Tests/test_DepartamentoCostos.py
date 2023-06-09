from unittest import TestCase
from unittest.mock import Mock, patch, MagicMock

from pytest import raises

from Cargas.Carga import Carga
from Cargas.Categorias import Categoria
from Medidas import Medidas

from EmpresaDirectorio.EmpresaCotizaciones import EmpresaCotizaciones

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
        cotizaciones = EmpresaCotizaciones()
        

        assert cotizaciones.calcular_precio_contenedor_por_pedido(mock_contenedor, distancia, cargas) == 1500



        
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
        cotizaciones = EmpresaCotizaciones()
        
        assert cotizaciones.calcular_precio_contenedor_por_pedido(mock_contenedor, distancia, cargas) == 200500
    
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
        cotizaciones = EmpresaCotizaciones()
        

        assert cotizaciones.calcular_precio_contenedor_por_pedido(mock_contenedor, distancia, cargas) == 1600

    
    
    def test_distancia_menor_1000_contenedor_completo_calcular_precio(self):
        medidas = Medidas(12.0,2.35,2.3)
        carga = Carga(medidas,50,Categoria.MAQUINARIA)
        
        cargas = [carga]
        
        
        mock_contenedor = Mock()
        mock_contenedor.get_cargas.return_value = cargas
        mock_contenedor.get_precio_transporte_base.return_value = 500
        mock_contenedor.get_medidas_interior.return_value = medidas
        
        distancia = 999
        cotizaciones = EmpresaCotizaciones()
        
        assert cotizaciones.calcular_precio_contenedor_por_pedido(mock_contenedor, distancia, cargas) == 210500

    #---------------------------------------------------------------------
    #---------------------------------------------------------------------
    #---------------------------------------------------------------------
    #---------------------------------------------------------------------
    #---------------------------------------------------------------------
    
    """MENOR A DIEZ MIL"""
    
    def test_distancia_menor_10000_por_peso_calcular_precio(self):
        medidas = Medidas(3,2,2)
        carga = Carga(medidas,50,Categoria.MAQUINARIA)
        cargas = [carga]
        mock_contenedor = Mock()
        mock_contenedor.get_cargas.return_value = cargas
        mock_contenedor.get_precio_transporte_base.return_value = 500
        mock_contenedor.get_medidas_interior.return_value = Medidas(12.0,2.35,2.3)
        
        distancia = 9999
        cotizaciones = EmpresaCotizaciones()
        

        assert cotizaciones.calcular_precio_contenedor_por_pedido(mock_contenedor, distancia, cargas) == 1650


    
    def test_distancia_menor_10000_contenedor_completo_calcular_precio(self):
        medidas = Medidas(12.0,2.35,2.3)
        carga = Carga(medidas,50,Categoria.MAQUINARIA)
        
        cargas = [carga]
        
        
        mock_contenedor = Mock()
        mock_contenedor.get_cargas.return_value = cargas
        mock_contenedor.get_precio_transporte_base.return_value = 500
        mock_contenedor.get_medidas_interior.return_value = medidas
        
        distancia = 9999
        cotizaciones = EmpresaCotizaciones()
        
        assert cotizaciones.calcular_precio_contenedor_por_pedido(mock_contenedor, distancia, cargas) == 230500
    
    #---------------------------------------------------------------------
    #---------------------------------------------------------------------
    #---------------------------------------------------------------------
    #---------------------------------------------------------------------
    #---------------------------------------------------------------------
    
    """MAYOR A DIEZ MIL"""
    '''
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
        cotizaciones = EmpresaCotizaciones()
        
        assert cotizaciones.calcular_precio_contenedor_por_pedido(mock_contenedor, distancia, cargas) == 1250
    
    
    def test_distancia_mas_10000_contenedor_completo_calcular_precio(self):
        medidas = Medidas(12.0,2.35,2.3)
        carga = Carga(medidas,50,Categoria.MAQUINARIA)
        
        cargas = [carga]
        
        
        mock_contenedor = Mock()
        mock_contenedor.get_cargas.return_value = cargas
        mock_contenedor.get_precio_transporte_base.return_value = 500
        mock_contenedor.get_medidas_interior.return_value = medidas
        
        distancia = 99999
        cotizaciones = EmpresaCotizaciones()
        
        assert cotizaciones.calcular_precio_contenedor_por_pedido(mock_contenedor, distancia, cargas) == 250500
        
    #---------------------------------------------------------------------
    #---------------------------------------------------------------------
    #---------------------------------------------------------------------
    #---------------------------------------------------------------------
    #---------------------------------------------------------------------
    """EXCEPCION DISTANCIA 0 o MENOR A 0"""
    def test_distancia_es_0_por_peso_calcular_precio(self):
        medidas = Medidas(3,2,2)
        carga = Carga(medidas,50,Categoria.MAQUINARIA)
        
        cargas = [carga]
        
        
        mock_contenedor = Mock()
        mock_contenedor.get_cargas.return_value = cargas
        mock_contenedor.get_precio_transporte_base.return_value = 500
        mock_contenedor.get_medidas_interior.return_value = Medidas(12.0,2.35,2.3)
    
        distancia = 0
        cotizaciones = EmpresaCotizaciones()
        
        
        with self.assertRaises(distancia_incorrecta):
            cotizaciones.calcular_precio_contenedor_por_pedido(mock_contenedor, distancia, cargas)
    
    
    def test_distancia_es_menor_a_0_por_peso_calcular_precio(self):
        medidas = Medidas(3,2,2)
        carga = Carga(medidas,50,Categoria.MAQUINARIA)
        
        cargas = [carga]
        
        
        mock_contenedor = Mock()
        mock_contenedor.get_cargas.return_value = cargas
        mock_contenedor.get_precio_transporte_base.return_value = 500
        mock_contenedor.get_medidas_interior.return_value = Medidas(12.0,2.35,2.3)
    
        distancia = -100
        cotizaciones = EmpresaCotizaciones()
        
        
        with self.assertRaises(distancia_incorrecta):
            cotizaciones.calcular_precio_contenedor_por_pedido(mock_contenedor, distancia, cargas)
        
        '''