from unittest import TestCase
from unittest.mock import Mock, patch, MagicMock

from pytest import raises
from Cargas.Carga import Carga
from Cargas.Categorias import Categoria
from Medidas import Medidas
from EmpresaDirectorio.EmpresaCotizaciones import EmpresaCotizaciones

class TestEmpresaCotizaciones(TestCase):
    
    def test_calcular_precio_contenedor_por_pedido_con_dos_cargas_medidas_minimas_y_distancia_corta(self):
        empresa_cotizaciones = EmpresaCotizaciones()
        
        cont1 = Mock()
        distancia = 1
        
        medidas = Medidas(1,3,5)
        carga = Carga(medidas,50,Categoria.MAQUINARIA)
        carga1 = Carga(medidas,50,Categoria.MAQUINARIA)
        carga2 = Carga(medidas,50,Categoria.MAQUINARIA)
        
        cargas_cliente = [carga, carga1, carga2]
        cont1.get_cargas.return_value = [carga, carga1]
        cont1.get_precio_transporte_base.return_value = 10
        cont1.get_medidas_interior.return_value = Medidas(20,20,20)
        # (1000 * 2) + 10
        assert 2010 == empresa_cotizaciones.calcular_precio_contenedor_por_pedido(cont1, distancia, cargas_cliente)
        
    def test_calcular_precio_contenedor_por_pedido_con_dos_cargas_medidas_minimas_y_distancia_alta(self):
        empresa_cotizaciones = EmpresaCotizaciones()
        
        cont1 = Mock()
        distancia = 10001
        
        medidas = Medidas(1,3,5)
        carga = Carga(medidas,50,Categoria.MAQUINARIA)
        carga1 = Carga(medidas,50,Categoria.MAQUINARIA)
        carga2 = Carga(medidas,50,Categoria.MAQUINARIA)
        
        cargas_cliente = [carga, carga1, carga2]
        cont1.get_cargas.return_value = [carga, carga1]
        cont1.get_precio_transporte_base.return_value = 10
        cont1.get_medidas_interior.return_value = Medidas(20,20,20)
        # (1500 * 2) + 10
        assert 3010 == empresa_cotizaciones.calcular_precio_contenedor_por_pedido(cont1, distancia, cargas_cliente)
        
    def test_calcular_precio_contenedor_por_pedido_con_dos_cargas_distancias_maximas_y_distancia_corta(self):
        empresa_cotizaciones = EmpresaCotizaciones()
        
        cont1 = Mock()
        distancia = 1
        
        medidas = Medidas(1,3,5)
        carga = Carga(medidas,50,Categoria.MAQUINARIA)
        carga1 = Carga(medidas,50,Categoria.MAQUINARIA)
        carga2 = Carga(medidas,50,Categoria.MAQUINARIA)
        
        cargas_cliente = [carga, carga1, carga2]
        cont1.get_cargas.return_value = [carga]
        cont1.get_precio_transporte_base.return_value = 10
        cont1.get_medidas_interior.return_value = medidas
        # 200000 + 10
        assert 200010 == empresa_cotizaciones.calcular_precio_contenedor_por_pedido(cont1, distancia, cargas_cliente)
        
    def test_calcular_precio_contenedor_por_pedido_con_dos_cargas_distancias_maximas_y_distancia_alta(self):
        empresa_cotizaciones = EmpresaCotizaciones()
        
        cont1 = Mock()
        distancia = 10001
        
        medidas = Medidas(1,3,5)
        carga = Carga(medidas,50,Categoria.MAQUINARIA)
        carga1 = Carga(medidas,50,Categoria.MAQUINARIA)
        carga2 = Carga(medidas,50,Categoria.MAQUINARIA)
        
        cargas_cliente = [carga, carga1, carga2]
        cont1.get_cargas.return_value = [carga]
        cont1.get_precio_transporte_base.return_value = 10
        cont1.get_medidas_interior.return_value = medidas
        # 250000 + 10
        assert 250010 == empresa_cotizaciones.calcular_precio_contenedor_por_pedido(cont1, distancia, cargas_cliente)
        
    
        