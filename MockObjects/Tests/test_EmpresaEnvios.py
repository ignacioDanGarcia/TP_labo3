from unittest import TestCase
from unittest.mock import Mock, patch, MagicMock
from pytest import raises
from EmpresaDirectorio.EmpresaData import EmpresaData
from EmpresaDirectorio.EmpresaEnvios import EmpresaEnvios
from Camion import Camion
from Cargas.Carga import Carga
from Cargas.Categorias import Categoria
from ContenedoresDirectorio.Builder.BuilderContenedorOpenTop import BuilderContenedorOpenTop
from ContenedoresDirectorio.Builder.BuilderContenedorBasico import BuilderContenedorBasico
from ContenedoresDirectorio.Director.Contenedor_director import Contenedor_director
from Medidas import Medidas
from EmpresaDirectorio.EmpresaData import EmpresaData
from Cargas.Carga import Carga
from Medidas import Medidas
from BarcosDirectorio.Factory.SelectorDeCreador import SelectorCreador
from BarcosDirectorio.TiposDeBarcos import TiposBarcos

class TestEmpresaEnvios(TestCase):

    def test_hacer_viajar_camiones(self):
       
     
        camion1 = Camion(154)
        camion2 = Camion(237)

        camion1.set_disponible(False)#ponerlos en disponibles false simula que ya tiene una carga
        camion2.set_disponible(False)
        
        camiones = [camion1,camion2]
        mock_contenedores = Mock()
        mock_barcos = Mock()
        empresa_data = EmpresaData([mock_barcos], camiones, [mock_contenedores])

        empresa_envios = EmpresaEnvios(empresa_data)

        empresa_envios.hacer_viajar_camiones(camiones) #cuendo el camion viaja se setea en disponible 

        assert camion1.get_disponible() == True
        assert camion2.get_disponible() == True
        assert empresa_data.get_camiones() == camiones

    def test_descargar_cargas_contenedores_camiones(self):
        camion1 = Camion(111)
        camion2 = Camion(222)

        builder = BuilderContenedorBasico()
        director = Contenedor_director(builder)
        cont = director.crear_contenedor(1,False)
        cont.set_cant_de_veces_comple_y_carga_unica(5)
        
        m = Medidas(1,1,1)
        cargas = [Carga(m,10,Categoria.MAQUINARIA)]

        cont.set_cargas(cargas)

        camion1.set_contenedor(cont)
        camion2.set_contenedor(cont) #aca disponible se seta en False ya que tiene una carga para transportar

        camiones = [camion1, camion2]

        mock_contenedores = Mock()
        mock_barcos = Mock()
        empresa_data = EmpresaData([mock_barcos], camiones, [mock_contenedores])

        empresa_envios = EmpresaEnvios(empresa_data)

        empresa_envios.descargar_contenedor_camiones(camiones)

        assert camion1.get_contenedor() == None
        assert camion2.get_contenedor() == None
        assert camion1.get_disponible() == True
        assert camion2.get_disponible() == True
        assert empresa_data.get_camiones() == camiones


    def test_hacer_viajar_barcos(self):
        selector_factory = SelectorCreador()
        creador = selector_factory.crear_factoria(TiposBarcos.BASICO)
        
        barco = creador.crear_barco(1,100,4,500)  
        barco2 = creador.crear_barco(1,100,4,500) # se inicializa el barco on 0km recorridos

        barco.set_combustible_actual(200)
        barco2.set_combustible_actual(200)
        barco.set_disponible(True)
        barco2.set_disponible(True)

        barcos = [barco, barco2]

        mock_contenedores = Mock()
        mock_camiones = Mock()
        empresa_data = EmpresaData(barcos, [mock_camiones], [mock_contenedores])

        empresa_envios = EmpresaEnvios(empresa_data)

        gps = Mock()
        gps.calcular_tiempo.return_value = 0
        gps.calcular_distancia.return_value = 10
        empresa_envios.hacer_viajar_barcos(barcos,gps)

        assert barco.get_disponible() == False
        assert barco2.get_disponible() == False
        assert barco.get_km_recorridos() > 0
        assert barco2.get_km_recorridos() > 0
        assert empresa_data.get_barcos() == barcos

    def test_descargar_contenedores_barcos(self):
        builder = BuilderContenedorBasico()
        director = Contenedor_director(builder)
        contenedor1 = director.crear_contenedor(1,False)
        contenedor2 = director.crear_contenedor(1,False)
        contenedor1.set_cant_de_veces_comple_y_carga_unica(5)
        contenedor2.set_cant_de_veces_comple_y_carga_unica(5)
        
        m = Medidas(1,1,1)
        cargas = [Carga(m,10,Categoria.MAQUINARIA), Carga(m,10,Categoria.MAQUINARIA)]

        contenedor1.set_cargas(cargas)
        contenedor2.set_cargas(cargas)
        contenedores = [contenedor1,contenedor2]

        selector_factory = SelectorCreador()
        creador = selector_factory.crear_factoria(TiposBarcos.BASICO)
        
        barco = creador.crear_barco(1,100,4,500)  
        barco2 = creador.crear_barco(1,100,4,500)
        barco.set_contenedores(contenedores)
        barco2.set_contenedores(contenedores)

        mock_camiones = Mock()
        barcos = [barco, barco2]
        empresa_data = EmpresaData(barcos, [mock_camiones], contenedores)

        empresa_envios = EmpresaEnvios(empresa_data)

        empresa_envios.descargar_contenedores_barcos(barcos)

        assert barco2.get_disponible() == True
        assert barco2.get_disponible() == True
        assert barco.get_contenedores()== None
        assert barco2.get_contenedores() == None
        assert barco.get_combustible_gastado() == 0
        assert barco2.get_combustible_gastado() == 0
        assert barco.get_km_recorridos() == 0
        assert barco.get_km_recorridos() == 0



        