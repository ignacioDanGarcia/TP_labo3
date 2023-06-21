from unittest import TestCase
from unittest.mock import Mock, patch, MagicMock

from pytest import raises
from BarcosDirectorio.Factory.SelectorDeCreador import SelectorCreador
from BarcosDirectorio.TiposDeBarcos import TiposBarcos
from ContenedoresDirectorio.Builder.Builder_contenedor import Contenedor_builder
from ContenedoresDirectorio.Director.Contenedor_director import Contenedor_director
from ContenedoresDirectorio.Contenedores import Contenedor
from ContenedoresDirectorio.Builder.BuilderContenedorBasico import BuilderContenedorBasico
from ContenedoresDirectorio.Builder.BuilderContenedorVentilado import BuilderContenedorVentilado
from ContenedoresDirectorio.Builder.BuilderContenedorFlatRack import BuilderContenedorFlatRack
from ContenedoresDirectorio.ManejadorDeCargas import ManejadorDeCargas
from EmpresaDirectorio.EmpresaData import EmpresaData
from EmpresaDirectorio.EmpresaDeposito import EmpresaDeposito
from Pedidos import Pedidos
from Cargas.Carga import Carga
from Cargas.Categorias import Categoria
from Medidas import Medidas
from BarcosDirectorio.BarcoBasico import BarcoBasico
from EmpresaDirectorio.EmpresaCotizaciones import EmpresaCotizaciones
from Camion import Camion
from ContenedoresDirectorio.SelectoraEstrategiaPorCarga import SelectoraEstrategiaPorCarga
class TestEmpresaDeposito(TestCase):
    
    def test_obtener_contenedores_pedido(self):
        pedido = Mock()
        pedido.get_contenedores_ids.return_value = [1, 100, 99, 87]
        
        mock_barcos = Mock()
        mock_camiones = Mock()
        cont1 = Contenedor(1,True)
        cont2 = Contenedor(100,False)
        cont3 = Contenedor(99, False)
        cont9 = Contenedor(87, True)
        contenedores = [cont1,cont2,cont3,cont9]
        empresa_data = EmpresaData([mock_barcos], [mock_camiones], contenedores)
        
        empresa_deposito = EmpresaDeposito(empresa_data)
        
        
        assert contenedores == empresa_deposito.obtener_contenedores_pedido(pedido)
        
    def test_ordenar_por_categoria(self):
        mock_barcos = Mock()
        mock_camiones = Mock()
        mock_contenedores = Mock()
        empresa_data = EmpresaData([mock_barcos], [mock_camiones], [mock_contenedores])
        
        empresa_deposito = EmpresaDeposito(empresa_data)
        
        medidas = Medidas(3,2,2)
        carga = Carga(medidas,50,Categoria.MAQUINARIA)
        carga1 = Carga(medidas,50,Categoria.ALIMENTICIA)
        carga2 = Carga(medidas,50,Categoria.QUIMICA)
        carga3 = Carga(medidas,50,Categoria.QUIMICA)
        
        cargas = [carga, carga1, carga2, carga3]
        cargas_ordenadas = [carga1, carga2, carga3, carga]
        empresa_deposito.ordenar_por_categoria(cargas)
        assert cargas_ordenadas == cargas
        
    def test_cargar_contenedor(self):
        mock_barcos = Mock()
        mock_camiones = Mock()
        mock_contenedores = Mock()
        empresa_data = EmpresaData([mock_barcos], [mock_camiones], [mock_contenedores])
        
        empresa_deposito = EmpresaDeposito(empresa_data)
        
        manejador_de_cargas = ManejadorDeCargas(SelectoraEstrategiaPorCarga())
        
        medidas = Medidas(3,2,2)
        carga = Carga(medidas,50,Categoria.MAQUINARIA)
        carga1 = Carga(medidas,50,Categoria.ALIMENTICIA)
        carga2 = Carga(medidas,50,Categoria.QUIMICA)
        carga3 = Carga(medidas,50,Categoria.QUIMICA)
        
        cargas = [carga, carga1, carga2, carga3]
        pedido = Pedidos(1, cargas, 3, False)
        
        builder = BuilderContenedorBasico()
        director = Contenedor_director(builder)
        contenedor = director.crear_contenedor(1,False)
        
        assert True == empresa_deposito.cargar_contenedor(manejador_de_cargas, carga, contenedor, pedido)
    
    
    def test_llenar_contenedores_y_llenar_barcos_con_solo_contenedores_flatrack_y_cargas_maquinarias_y_quimica(self):
        medidas = Medidas(1,1,1)
        carga = Carga(medidas,5,Categoria.MAQUINARIA)
        carga1 = Carga(medidas,5,Categoria.MAQUINARIA)
        carga2 = Carga(medidas,5,Categoria.QUIMICA)
        
        
        cargas = [carga, carga1, carga2]
        pedido = Pedidos(1, cargas, 3, False)
        pedido.set_contenedores_ids([])
        
        builder = BuilderContenedorFlatRack()
        director = Contenedor_director(builder)
        contenedor = director.crear_contenedor(1, False)
        contenedor2 = director.crear_contenedor(1,False)
        contenedor3 = director.crear_contenedor(1,False)
        
        contenedores = [contenedor, contenedor2, contenedor3]
        
        mock_camiones = Mock()

        
        selector_factory = SelectorCreador()
        creador = selector_factory.crear_factoria(TiposBarcos.BASICO)
        
        barco = creador.crear_barco(1,100,3,500)
        barco2 = creador.crear_barco(2,100,3,500)
        barco3 = creador.crear_barco(3,100,3,500)
        barco4 = creador.crear_barco(3,100,3,500)
        barco5 = creador.crear_barco(3,100,3,500)
        
        barco3.set_distancia(3)
        barco2.set_distancia(2)
        
        barcos = [barco, barco2, barco3, barco4, barco5]
        empresa_data = EmpresaData(barcos, [mock_camiones], contenedores)
        
        empresa_deposito = EmpresaDeposito(empresa_data)
        
        
        barco3.agregar_contenedores(contenedor)
        
        assert barco.get_distancia() == 0
        print(contenedor)
        empresa_deposito.llenar_contenedores_y_llenar_barcos(pedido)
        
        assert barco3.get_contenedores() == [contenedor]
        assert contenedor.get_cargas() == cargas
    
    def test_llenar_contenedores_y_llenar_barcos_con_solo_contenedores_flatrack_y_cargas_maquinarias_y_quimica(self):
        medidas = Medidas(1,1,1)
        carga = Carga(medidas,5,Categoria.MAQUINARIA)
        carga1 = Carga(medidas,5,Categoria.ALIMENTICIA)
        carga2 = Carga(medidas,5,Categoria.QUIMICA)
        
        
        cargas = [carga, carga1, carga2]
        pedido = Pedidos(1, cargas, 3, False)
        pedido.set_contenedores_ids([])
        
        builder = BuilderContenedorFlatRack()
        director = Contenedor_director(builder)
        contenedor = director.crear_contenedor(1, True)
        contenedor2 = director.crear_contenedor(1,False)
        builder2 = BuilderContenedorVentilado()
        director.change_builder(builder2)
        contenedor3 = director.crear_contenedor(1,True)
        
        contenedores = [contenedor, contenedor2, contenedor3]
        
        mock_camiones = Mock()

        
        selector_factory = SelectorCreador()
        creador = selector_factory.crear_factoria(TiposBarcos.ESPECIAL)
        
        barco = creador.crear_barco(1,100,3,500)
        barco2 = creador.crear_barco(2,100,3,500)
        barco3 = creador.crear_barco(3,100,3,500)
        barco4 = creador.crear_barco(3,100,3,500)
        barco5 = creador.crear_barco(3,100,3,500)
        
        barco3.set_distancia(3)
        barco2.set_distancia(2)
        barco4.set_distancia(0)
        barco5.set_distancia(0)
        barcos = [barco, barco2, barco3, barco4, barco5]
        empresa_data = EmpresaData(barcos, [mock_camiones], contenedores)
        
        empresa_deposito = EmpresaDeposito(empresa_data)
        
        
        barco3.agregar_contenedores(contenedor)
        
        assert barco.get_distancia() == 0
        
        empresa_deposito.llenar_contenedores_y_llenar_barcos(pedido)
        
        assert contenedor3.get_cargas() == [carga1]
        assert contenedor.get_cargas() == [carga1]
    