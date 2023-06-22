from unittest import TestCase
from unittest.mock import Mock, patch, MagicMock

from pytest import raises
from BarcosDirectorio.Factory.SelectorDeCreador import SelectorCreador
from BarcosDirectorio.ManejadorDeContenedoresDirectorio.ManejadorDeContenedores import ManejadorDeContenedores
from BarcosDirectorio.ManejadorDeContenedoresDirectorio.SelectoraEstrategiaPorBarco import SelectoraEstrategiaPorBarco
from BarcosDirectorio.TiposDeBarcos import TiposBarcos
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
from ContenedoresDirectorio.SelectoraEstrategiaPorCarga import SelectoraEstrategiaPorCarga
from EmpresaDirectorio.EmpresaOficina import EmpresaOficina
from ContenedoresDirectorio.ManejadorDeCargas import ManejadorDeCargas
from BarcosDirectorio.ManejadorDeContenedoresDirectorio.ManejadorDeContenedores import ManejadorDeContenedores
from EmpresaDirectorio.EmpresaCotizaciones import EmpresaCotizaciones
from ContenedoresDirectorio.Builder.BuilderContenedorVentilado import BuilderContenedorVentilado
from ContenedoresDirectorio.Director.Contenedor_director import Contenedor_director
from Excepciones.exceptions import No_hay_barcos_disponibles,No_hay_camiones_disponibles

class TestEmpresaDeposito(TestCase):
    
    def test_procesar_pedido_retira_en_puerto(self):
        builder = BuilderContenedorVentilado()
        director = Contenedor_director(builder)
        contenedor = director.crear_contenedor(5, True)
        contenedor.set_precio_transporte_base(500)
        medidas = Medidas(1,1,1)
        carga = Carga(medidas,1,Categoria.MAQUINARIA)
        carga1 = Carga(medidas,1,Categoria.ALIMENTICIA)
        
        cargas = [carga, carga1]
        pedido = Pedidos(1, cargas, 3, False)
        
        selector_factory = SelectorCreador()
        creador = selector_factory.crear_factoria_de_tipo_de_barco(TiposBarcos.BASICO)
        
        barco = creador.crear_barco(1,100,0,500)
        barco2 = creador.crear_barco(2,100,0,500)
        
        barcos = [barco, barco2]
        
        mock_camiones = Mock()
        
        empresa_data = EmpresaData(barcos, [mock_camiones], [contenedor])
        
        manejador_cargas = ManejadorDeCargas(SelectoraEstrategiaPorCarga())
        manejador_contenedores = ManejadorDeContenedores(SelectoraEstrategiaPorBarco())
        
        empresa_deposito = EmpresaDeposito(empresa_data, manejador_cargas, manejador_contenedores)
        empresa_cotizaciones = EmpresaCotizaciones()
        
        oficina = EmpresaOficina(empresa_data,empresa_deposito,empresa_cotizaciones)
        
        
        assert oficina.procesar_pedido(pedido) == 2500
        #El pedido tiene dos cargas que van al mismo contenedor. $1000 por carga y paga el precio base una sola vez. $2500. Lo retira en puerto. 
    
    def test_procesar_pedido_puerta_a_puerta(self):
        builder = BuilderContenedorVentilado()
        director = Contenedor_director(builder)
        contenedor = director.crear_contenedor(5, True)
        contenedor.set_precio_transporte_base(500)
        medidas = Medidas(1,1,1)
        carga = Carga(medidas,1,Categoria.MAQUINARIA)
        carga1 = Carga(medidas,1,Categoria.ALIMENTICIA)
        
        cargas = [carga, carga1]
        pedido = Pedidos(1, cargas, 3, True)
        
        selector_factory = SelectorCreador()
        creador = selector_factory.crear_factoria_de_tipo_de_barco(TiposBarcos.BASICO)
        
        barco = creador.crear_barco(1,100,0,500)
        barco2 = creador.crear_barco(2,100,0,500)
        
        barcos = [barco, barco2]
        
        mock_camion1 = Mock()
        mock_camion1.get_disponible.return_value = True
        
        mock_camion2 = Mock()
        mock_camion2.get_disponible.return_value = True
        
        camiones = [mock_camion1,mock_camion2]
        empresa_data = EmpresaData(barcos, camiones, [contenedor])
        
        manejador_cargas = ManejadorDeCargas(SelectoraEstrategiaPorCarga())
        manejador_contenedores = ManejadorDeContenedores(SelectoraEstrategiaPorBarco())
        
        empresa_deposito = EmpresaDeposito(empresa_data, manejador_cargas, manejador_contenedores)
        empresa_cotizaciones = EmpresaCotizaciones()
        
        oficina = EmpresaOficina(empresa_data,empresa_deposito,empresa_cotizaciones)
        
        
        assert oficina.procesar_pedido(pedido) == 42500
        #El pedido tiene dos cargas que van al mismo contenedor. $1000 por carga y paga el precio base una sola vez. $2500. Envío puerta a puerta así que sumamos $20.000 por contenedor
        #Resultado $40.000 + 2500 = $42.500
        
        
    def test_procesar_pedido_puerta_a_puerta_sin_camiones_disponibles(self):
        builder = BuilderContenedorVentilado()
        director = Contenedor_director(builder)
        contenedor = director.crear_contenedor(5, True)
        contenedor.set_precio_transporte_base(500)
        medidas = Medidas(1,1,1)
        carga = Carga(medidas,1,Categoria.MAQUINARIA)
        carga1 = Carga(medidas,1,Categoria.ALIMENTICIA)
        
        cargas = [carga, carga1]
        pedido = Pedidos(1, cargas, 3, True)
        
        selector_factory = SelectorCreador()
        creador = selector_factory.crear_factoria_de_tipo_de_barco(TiposBarcos.BASICO)
        
        barco = creador.crear_barco(1,100,0,500)
        barco2 = creador.crear_barco(2,100,0,500)
        
        barcos = [barco, barco2]
        
        mock_camion1 = Mock()
        mock_camion1.get_disponible.return_value = True
        
    
        
        camiones = [mock_camion1]
        empresa_data = EmpresaData(barcos, camiones, [contenedor])
        
        manejador_cargas = ManejadorDeCargas(SelectoraEstrategiaPorCarga())
        manejador_contenedores = ManejadorDeContenedores(SelectoraEstrategiaPorBarco())
        
        empresa_deposito = EmpresaDeposito(empresa_data, manejador_cargas, manejador_contenedores)
        empresa_cotizaciones = EmpresaCotizaciones()
        
        oficina = EmpresaOficina(empresa_data,empresa_deposito,empresa_cotizaciones)
        
        with self.assertRaises(No_hay_camiones_disponibles):
            assert oficina.procesar_pedido(pedido) == 42500