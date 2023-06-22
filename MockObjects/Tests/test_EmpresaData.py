from unittest import TestCase
from unittest.mock import Mock, patch, MagicMock

from pytest import raises
from ContenedoresDirectorio.Contenedores import Contenedor
from EmpresaDirectorio.EmpresaData import EmpresaData
from Excepciones.exceptions import No_hay_camiones_disponibles
from Camion import Camion
from BarcosDirectorio.Factory.SelectorDeCreador import SelectorCreador
from BarcosDirectorio.TiposDeBarcos import TiposBarcos


class TestEmpresaData(TestCase):
    def test_empresa_trae_barco_disponible_con_distancia_cero_y_camion_disponible(self):
        selector_factory = SelectorCreador()
        factoria = selector_factory.crear_factoria_de_tipo_de_barco(TiposBarcos.BASICO)
        
        barco1 = factoria.crear_barco(1,100,4,500)
        barco2 = factoria.crear_barco(2,100,4,500)
        barco3 = factoria.crear_barco(3,100,4,500) 
        #Cuando los instanciamos están disponibles. 
        barco1.set_disponible(False)
        barco3.set_disponible(False)
        barcos = [barco1,barco2,barco3]
        
        camion1 = Camion(154)
        camion2 = Camion(237)
        camion7 = Camion (999)
        #Cuando los instanciamos están disponibles.
        camion1.set_disponible(False)
        camion2.set_disponible(False)
        
        camiones = [camion1,camion2,camion7]
        
        mock_camiones = Mock()
        mock_contenedores = Mock()
        empresa_data = EmpresaData(barcos, camiones, [mock_contenedores])
        barco_disponible = empresa_data.get_barco_disponible_distancia_cero()
        assert barco_disponible == barco2
        assert barco_disponible.get_id() == 2
        assert barco_disponible.get_distancia() == 0
        
        camion_disponible = empresa_data.devolver_camiones_disponibles()
        assert camion_disponible[0] == camion7
        assert camion_disponible[0].get_id() == 999
    
    def test_empresa_tira_exception_si_no_hay_barcos_disponibles(self):
        
        selector_factory = SelectorCreador()
        factoria = selector_factory.crear_factoria_de_tipo_de_barco(TiposBarcos.BASICO)
        
        barco1 = factoria.crear_barco(1,100,4,500)
        barco2 = factoria.crear_barco(2,100,4,500)
        barco3 = factoria.crear_barco(3,100,4,500)  
        #Cuando los instanciamos están disponibles. 
        barco1.set_disponible(False)
        barco3.set_disponible(False)
        barco2.set_disponible(False)

        barcos = [barco1,barco2,barco3]
        
        mock_camiones = Mock()
        mock_contenedores = Mock()
        empresa_data = EmpresaData(barcos, [mock_camiones], [mock_contenedores])
        assert empresa_data.get_barcos_disponible_misma_distancia(1) == []
        assert empresa_data.get_barco_disponible_distancia_cero() == None
    
    def test_empresa_tira_lista_vacia_si_no_hay_camiones_disponibles(self):
        mock_contenedores = Mock()
        mock_barcos = Mock()

        camion1 = Camion(154)
        camion2 = Camion(237)
        camion7 = Camion (999)
        #Cuando los instanciamos están disponibles.
        camion1.set_disponible(False)
        camion2.set_disponible(False)
        camion7.set_disponible(False)
        
        camiones = [camion1,camion2,camion7]
        
        empresa_data = EmpresaData([mock_barcos], camiones, [mock_contenedores])
        
        
        assert  empresa_data.devolver_camiones_disponibles() == []
    
    def test_empresa_trae_contenedores_disponibles(self):
        mock_barcos = Mock()
        mock_camiones = Mock()
        cont1 = Contenedor(1,True)
        cont2 = Contenedor(100,False)
        cont3 = Contenedor(99, False)
        cont9 = Contenedor(87, True)
        #Cuando los instanciamos están disponibles.
        cont1.set_disponible(False)
        cont9.set_disponible(False)
        contenedores = [cont1,cont2,cont3,cont9]
        
        
        empresa_data = EmpresaData([mock_barcos], mock_camiones, contenedores)
        
        contenedores_disponibles = empresa_data.get_contenedores_disponibles()
        
        assert contenedores_disponibles == [cont2,cont3]
    
    def test_empresa_trae_barco_con_mayores_y_menores_KMS_recorridos(self):
        selector_factory = SelectorCreador()
        factoria = selector_factory.crear_factoria_de_tipo_de_barco(TiposBarcos.BASICO)
        
        mock_camiones = Mock()
        mock_contenedores = Mock()
        
        barco1 = factoria.crear_barco(1,100,4,500)
        barco2 = factoria.crear_barco(2,100,4,500)
        barco3 = factoria.crear_barco(3,100,4,500) 
        barco9 = factoria.crear_barco(3,100,4,500) 
        barco15 = factoria.crear_barco(3,100,4,500) 
        barco10 = factoria.crear_barco(3,100,4,500) 
        
        barco1.set_km_recorridos(500)
        barco2.set_km_recorridos(2.7)
        barco9.set_km_recorridos(1750)
        barco3.set_km_recorridos(999)
        barco15.set_km_recorridos(700)
        barco10.set_km_recorridos(7)
        
        barcos = [barco1,barco2,barco3,barco9,barco15,barco10]
        empresa_data = EmpresaData(barcos, mock_camiones, mock_contenedores)
        
        empresa_data.actualizar_barco_con_mas_y_con_menos_km()
        assert empresa_data.barco_con_mas_km == barco9
        assert empresa_data.barco_con_menos_km == barco2

    def test_empresa_data_devuelve_contenedor_que_viajo_con_una_sola_carga_y_completo_mas_veces(self):
        mock_camiones = Mock()
        mock_barcos = Mock()
        cont1 = Contenedor(1,True)
        cont2 = Contenedor(100,False)
        cont3 = Contenedor(99, False)
        cont9 = Contenedor(87, True)
        
        cont1.set_cant_de_veces_comple_y_carga_unica(3)
        cont2.set_cant_de_veces_comple_y_carga_unica(1)
        cont3.set_cant_de_veces_comple_y_carga_unica(9)
        cont9.set_cant_de_veces_comple_y_carga_unica(7)
        contenedores = [cont1,cont2,cont3,cont9]
        
        empresa_data = EmpresaData(mock_barcos, mock_camiones, contenedores)
        
        contenedos_mas_viajes_con_carga_unica = empresa_data.container_con_mas_viajes_con_una_carga()
        
        assert contenedos_mas_viajes_con_carga_unica == cont3
