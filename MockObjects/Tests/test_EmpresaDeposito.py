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
        
        manejador_cargas = Mock()
        manejador_contenedores = Mock()
        
        empresa_deposito = EmpresaDeposito(empresa_data, manejador_cargas, manejador_contenedores)
        
        
        assert contenedores == empresa_deposito.obtener_contenedores_pedido(pedido)
        
    def test_ordenar_por_categoria(self):
        mock_barcos = Mock()
        mock_camiones = Mock()
        mock_contenedores = Mock()
        empresa_data = EmpresaData([mock_barcos], [mock_camiones], [mock_contenedores])
        
        manejador_cargas = Mock()
        manejador_contenedores = Mock()
        
        empresa_deposito = EmpresaDeposito(empresa_data, manejador_cargas, manejador_contenedores)
        
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
        
        manejador_cargas = ManejadorDeCargas(SelectoraEstrategiaPorCarga())
        manejador_contenedores = Mock()
        
        empresa_deposito = EmpresaDeposito(empresa_data, manejador_cargas, manejador_contenedores)
        
        
        
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
        
        assert True == empresa_deposito.cargar_contenedor(empresa_deposito.get_manejador_cargas(), carga, contenedor, pedido)
        assert False == empresa_deposito.cargar_contenedor(empresa_deposito.get_manejador_cargas(), carga2, contenedor, pedido)
    
    def test_asignar_carga_a_contenedor_existente(self):
        mock_barcos = Mock()
        mock_camiones = Mock()
        builder = BuilderContenedorBasico()
        director = Contenedor_director(builder)
        contenedor = director.crear_contenedor(1,False)
        empresa_data = EmpresaData([mock_barcos], [mock_camiones], [contenedor])
        
        manejador_cargas = ManejadorDeCargas(SelectoraEstrategiaPorCarga())
        manejador_contenedores = ManejadorDeContenedores(SelectoraEstrategiaPorBarco())
        
        empresa_deposito = EmpresaDeposito(empresa_data, manejador_cargas, manejador_contenedores)
        
        medidas = Medidas(1,1,1)
        carga = Carga(medidas,1,Categoria.MAQUINARIA)
        carga1 = Carga(medidas,1,Categoria.ALIMENTICIA)
        
        cargas = [carga, carga1]
        pedido = Pedidos(1, cargas, 3, False)
        
        
        pedido.set_contenedores_ids([])
        assert empresa_deposito.asignar_carga_a_contenedor_existente(pedido, carga) == None
        
        

        ids = [1, 2, 3]
        
        pedido.set_contenedores_ids(ids)

        assert empresa_deposito.asignar_carga_a_contenedor_existente(pedido, carga) == contenedor
    

        
        assert empresa_deposito.asignar_carga_a_contenedor_existente(pedido, carga1) == None
    
    
    def test_asignar_carga_a_contenedor_barco(self):
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
        
        mock_barcos = Mock()
        mock_camiones = Mock()
        mock_contenedor = Mock()
        empresa_data = EmpresaData([mock_barcos], [mock_camiones], [mock_contenedor])
        
        manejador_cargas = ManejadorDeCargas(SelectoraEstrategiaPorCarga())
        manejador_contenedores = ManejadorDeContenedores(SelectoraEstrategiaPorBarco())
        
        empresa_deposito = EmpresaDeposito(empresa_data, manejador_cargas, manejador_contenedores)
        
        assert empresa_deposito.asignar_carga_a_contenedor_barco(pedido, carga, barcos) == None
        
        
    
    def test_asignar_carga_a_contenedor_barco(self):
        medidas = Medidas(1, 1, 1)
        carga = Carga(medidas, 1, Categoria.MAQUINARIA)
        carga1 = Carga(medidas, 1, Categoria.ALIMENTICIA)

        cargas = [carga, carga1]
        pedido = Pedidos(1, cargas, 3, False)

        selector_factory = SelectorCreador()
        creador = selector_factory.crear_factoria_de_tipo_de_barco(TiposBarcos.BASICO)

        barco = creador.crear_barco(1, 100, 1, 500)
        barco2 = creador.crear_barco(2, 100, 1, 500)

        builder = BuilderContenedorBasico()
        director = Contenedor_director(builder)
        contenedor = director.crear_contenedor(1, False)

        mock_barcos = Mock()
        mock_camiones = Mock()
        manejador_cargas = ManejadorDeCargas(SelectoraEstrategiaPorCarga())
        manejador_contenedores = ManejadorDeContenedores(SelectoraEstrategiaPorBarco())
        empresa_data = EmpresaData([mock_barcos], [mock_camiones], [contenedor])

        manejador_contenedores.cargar(barco, contenedor)

        empresa_deposito = EmpresaDeposito(empresa_data, manejador_cargas, manejador_contenedores)
        barcos = [barco, barco2]

        assert empresa_deposito.asignar_carga_a_contenedor_barco(pedido, carga, barcos) == barco

    def test_actualizar_contenedor_en_empresa_data(self):
        builder = BuilderContenedorBasico()
        director = Contenedor_director(builder)
        contenedor = director.crear_contenedor(1, False)
        
        mock_barcos = Mock()
        mock_camiones = Mock()
        manejador_cargas = ManejadorDeCargas(SelectoraEstrategiaPorCarga())
        manejador_contenedores = ManejadorDeContenedores(SelectoraEstrategiaPorBarco())
        empresa_data = EmpresaData([mock_barcos], [mock_camiones], [contenedor])
    
        empresa_deposito = EmpresaDeposito(empresa_data, manejador_cargas, manejador_contenedores)
        
        assert empresa_data.get_contenedores()[0].get_cargas() == []
        
        medidas = Medidas(1, 1, 1)
        carga = Carga(medidas, 1, Categoria.MAQUINARIA)
        manejador_cargas.cargar(carga, contenedor)
        
        empresa_deposito.actualizar_contenedor_en_empresa_data(contenedor)
        
        assert empresa_data.get_contenedores()[0].get_cargas() == [carga]
    
    def test_actualizar_barco_en_empresa_data(self):
        medidas = Medidas(1, 1, 1)
        carga = Carga(medidas, 1, Categoria.MAQUINARIA)
        carga1 = Carga(medidas, 1, Categoria.ALIMENTICIA)

        cargas = [carga, carga1]
        pedido = Pedidos(1, cargas, 3, False)

        selector_factory = SelectorCreador()
        creador = selector_factory.crear_factoria_de_tipo_de_barco(TiposBarcos.BASICO)

        barco = creador.crear_barco(1, 100, 1, 500)
        barco2 = creador.crear_barco(2, 100, 1, 500)

        builder = BuilderContenedorBasico()
        director = Contenedor_director(builder)
        contenedor = director.crear_contenedor(1, False)

        barcos = [barco, barco2]
        mock_camiones = Mock()
        manejador_cargas = ManejadorDeCargas(SelectoraEstrategiaPorCarga())
        manejador_contenedores = ManejadorDeContenedores(SelectoraEstrategiaPorBarco())
        empresa_data = EmpresaData(barcos, [mock_camiones], [contenedor])

        manejador_cargas.cargar(carga, contenedor)
        manejador_contenedores.cargar(barco, contenedor)
        
        empresa_deposito = EmpresaDeposito(empresa_data, manejador_cargas, manejador_contenedores)
        barcos = [barco, barco2]

        empresa_deposito.asignar_carga_a_contenedor_barco(pedido, carga, barcos) # = barco
        print(empresa_data.get_barcos())
        assert empresa_data.get_contenedores()[0].get_cargas()[0] == carga
        
        assert empresa_data.get_contenedores()[0] == contenedor
        
        assert empresa_data.get_barcos()[0] == barco
        
    def test_llenar_contenedores_y_llenar_barcos_solo_cargas_maquinarias(self):
        medidas = Medidas(1, 1, 1)
        carga1 = Carga(medidas, 1, Categoria.MAQUINARIA)
        carga2 = Carga(medidas, 2, Categoria.MAQUINARIA)
        carga3 = Carga(medidas, 3, Categoria.MAQUINARIA)

        cargas = [carga1, carga2, carga3]
        pedido = Pedidos(1, cargas, 3, False)


        builder = BuilderContenedorFlatRack()
        director = Contenedor_director(builder)
        contenedor1 = director.crear_contenedor(1, False)
        contenedor2 = director.crear_contenedor(1, False)
        contenedor3 = director.crear_contenedor(1, False)

        selector_factory = SelectorCreador()
        creador = selector_factory.crear_factoria_de_tipo_de_barco(TiposBarcos.ESPECIAL)

        barco1 = creador.crear_barco(1, 100, 1, 500)
        barco2 = creador.crear_barco(2, 100, 1, 500)
        barco2.set_distancia(3)
        barcos = [barco1, barco2]
        contenedores = [contenedor1, contenedor2, contenedor3]
        
        
        mock_camiones = Mock()
        manejador_cargas = ManejadorDeCargas(SelectoraEstrategiaPorCarga())
        manejador_contenedores = ManejadorDeContenedores(SelectoraEstrategiaPorBarco())
        empresa_data = EmpresaData(barcos, [mock_camiones], contenedores)
    
        empresa_deposito = EmpresaDeposito(empresa_data, manejador_cargas, manejador_contenedores)

        empresa_deposito.llenar_contenedores_y_llenar_barcos(pedido)

        assert contenedor1.get_cargas() == [carga1, carga2, carga3]
        assert barco2.get_contenedores() == [contenedor1]

       
    def test_llenar_contenedores_y_llenar_barcos_cargas_maquinarias_y_quimica(self):
        medidas = Medidas(1, 1, 1)
        carga1 = Carga(medidas, 1, Categoria.MAQUINARIA)
        carga2 = Carga(medidas, 1, Categoria.MAQUINARIA)
        carga3 = Carga(medidas, 1, Categoria.QUIMICA)

        cargas = [carga1, carga2, carga3]
        pedido = Pedidos(1, cargas, 3, False)


        builder = BuilderContenedorFlatRack()
        director = Contenedor_director(builder)
        contenedor1 = director.crear_contenedor(1, False)
        contenedor2 = director.crear_contenedor(1, True)
        contenedor3 = director.crear_contenedor(1, False)

        selector_factory = SelectorCreador()
        creador = selector_factory.crear_factoria_de_tipo_de_barco(TiposBarcos.ESPECIAL)

        barco1 = creador.crear_barco(1, 100, 1, 500)
        barco2 = creador.crear_barco(2, 100, 1, 500)
        barco2.set_distancia(3)
        barcos = [barco1, barco2]
        contenedores = [contenedor1, contenedor2, contenedor3]
        
        
        mock_camiones = Mock()
        manejador_cargas = ManejadorDeCargas(SelectoraEstrategiaPorCarga())
        manejador_contenedores = ManejadorDeContenedores(SelectoraEstrategiaPorBarco())
        empresa_data = EmpresaData(barcos, [mock_camiones], contenedores)
    
        empresa_deposito = EmpresaDeposito(empresa_data, manejador_cargas, manejador_contenedores)

        empresa_deposito.llenar_contenedores_y_llenar_barcos(pedido)
        # ORDENA LAS CARGAS ASI QUE LA CARGA QUIMICA VA A ESTAR PRIMERO
        # POR LO CUAL NO SE VA A INSERTAR EN EL PRIMER CONTENEDOR QUE NO PUEDE LLEVAR MATERIAL ESPECIAL, SINO EN EL SEGUNDO
        # Y PARA NO USAR VARIOS CONTENEDORES, LAS CARGAS MAQUINARIAS SE GUARDAN EN EL MISMO
        
        # Y SE GUARDAN EN BARCO2, PARA NO USAR UN BARCO NUEVO, PORQUE ESE BARCO YA VA AL MISMO LUGAR QUE EL PEDIDO
        carga = contenedor2.get_cargas()[0]
        print(contenedor1.get_cargas())
        print(contenedor2.get_cargas())
        print(carga.get_categoria())
        print(contenedor3.get_cargas())

        print(barco1.get_contenedores())
        print(barco2.get_contenedores())
        
        assert contenedor2.get_cargas() == [carga3, carga1, carga2]
        assert barco2.get_contenedores() == [contenedor2]
    
    
    
        
    def test_llenar_contenedores_y_llenar_barcos_cargas_alimenticia_y_quimica(self):
        medidas = Medidas(1, 1, 1)
        carga1 = Carga(medidas, 1, Categoria.ALIMENTICIA)
        carga2 = Carga(medidas, 1, Categoria.MAQUINARIA)
        carga3 = Carga(medidas, 1, Categoria.QUIMICA)

        cargas = [carga1, carga2, carga3]
        pedido = Pedidos(1, cargas, 3, False)


        builder = BuilderContenedorFlatRack()
        director = Contenedor_director(builder)
        contenedor1 = director.crear_contenedor(1, False)
        contenedor2 = director.crear_contenedor(2, True)
        
        builder2 = BuilderContenedorVentilado()
        director.change_builder(builder2)
        contenedor3 = director.crear_contenedor(3, False)
        
        selector_factory = SelectorCreador()
        creador = selector_factory.crear_factoria_de_tipo_de_barco(TiposBarcos.ESPECIAL)

        barco1 = creador.crear_barco(1, 700, 3, 500)
        barco2 = creador.crear_barco(2, 700, 7, 500)
        print(barco2.get_cant_contenedores_max())
        barco2.set_distancia(3)
        barcos = [barco1, barco2]
        contenedores = [contenedor1, contenedor2, contenedor3]
        
        
        mock_camiones = Mock()
        manejador_cargas = ManejadorDeCargas(SelectoraEstrategiaPorCarga())
        manejador_contenedores = ManejadorDeContenedores(SelectoraEstrategiaPorBarco())
        empresa_data = EmpresaData(barcos, [mock_camiones], contenedores)
    
        empresa_deposito = EmpresaDeposito(empresa_data, manejador_cargas, manejador_contenedores)

        empresa_deposito.llenar_contenedores_y_llenar_barcos(pedido)
        # ORDENA: ALIMENTICIA (carga1), QUIMICA (carga3), MAQUINARIA (carga2)

        """
        prints para debuggear
        print(contenedor2.get_cargas()[0].get_categoria(), contenedor2.get_cargas()[1].get_categoria())
        print(contenedor3.get_cargas()[0].get_categoria())

        contenedores_barco1 = barco1.get_contenedores()
        if len(contenedores_barco1) > 0:
            print(contenedores_barco1[0].get_tipo())

        print(barco2.get_contenedores()[0].get_tipo())
        print(barco2.get_contenedores()[1].get_tipo())
        print(len(barco2.get_contenedores()))
        """
        # OBJETOS ACTUALIZADOS EN EMPRESA DATA
        assert contenedor2 in empresa_data.get_contenedores()
        assert contenedor3 in empresa_data.get_contenedores()
        assert barco1 in empresa_data.get_barcos()
        assert barco2 in empresa_data.get_barcos()
        
        assert contenedor3.get_cargas() == [carga1]
        assert contenedor2.get_cargas() == [carga3, carga2]
        assert barco2.get_contenedores() == [contenedor3, contenedor2]