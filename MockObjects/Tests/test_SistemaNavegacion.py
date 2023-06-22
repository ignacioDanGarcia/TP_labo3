
from unittest import TestCase
import unittest.mock as mock
from unittest.mock import Mock, patch, MagicMock

from BarcosDirectorio.SistemasNavegacion.Sensor_viento import SensorViento
from BarcosDirectorio.SistemasNavegacion.AMotor import AMotor
from BarcosDirectorio.SistemasNavegacion.AVela import AVela
from Excepciones.exceptions import CombustibleInsuficienteException, distancia_incorrecta, tiempo_incorrecto
from BarcosDirectorio.SistemasNavegacion.ControladorDeNavegacion import ControladorDeSistemaDeNavegacion
from BarcosDirectorio.TiposDeBarcos import TiposBarcos
from BarcosDirectorio.Factory.SelectorDeCreador import SelectorCreador

from ModuloGPS import ModuloGPS

class tests_sistemasNavegacion(TestCase):
    def test_prueba_instanciar_barco_y_navegar_tiempo_suficiente(self):
        selector_factory = SelectorCreador()
        factoria = selector_factory.crear_factoria_de_tipo_de_barco(TiposBarcos.ESPECIAL)
        
        barco = factoria.crear_barco(1,400,3,40)
        modulo_gps = Mock()
        modulo_gps.calcular_tiempo.return_value = 5
        modulo_gps.calcular_distancia.return_value = 200

        # #El ultimo atributo es la cantidad de litros de combustible del barco
        assert barco.get_combustible_actual() == 40
        assert isinstance(barco.get_sistema_navegacion(), AMotor)
        if barco.puede_navegar(modulo_gps):
            barco.navegar(modulo_gps) #Acá paso las horas al barco. Gasta 6L * por hora 40 - 30 == 10
        
        assert barco.get_combustible_actual() == 10
        assert barco.get_km_recorridos() == 200
        #assert isinstance(barco.get_sistema_navegacion(), AVela)
    
    def test_prueba_instanciar_barco_y_navegar_mas_tiempo_que_aguanta_su_nafta(self):
        selector_factory = SelectorCreador()
        factoria = selector_factory.crear_factoria_de_tipo_de_barco(TiposBarcos.ESPECIAL)
        barco = factoria.crear_barco(1,400,3,10)
        
        modulo_gps = Mock()
        modulo_gps.calcular_tiempo.return_value = 3
        modulo_gps.calcular_distancia.return_value = 300

        #10 - 18 no alcanza, raiseo exception
        with self.assertRaises(CombustibleInsuficienteException):   
            if barco.puede_navegar(modulo_gps):
                barco.navegar(modulo_gps)
    
    
    def test_prueba_barco_con_sensor_de_viento_puede_ahorrar_nafta(self):
        sensor_viento = SensorViento()
        selector_factory = SelectorCreador()
        factoria = selector_factory.crear_factoria_de_tipo_de_barco(TiposBarcos.BASICO)
        barco = factoria.crear_barco(1,400,3,600,sensor_viento)
        
        modulo_gps = Mock()
        modulo_gps.calcular_tiempo.return_value = 10
        modulo_gps.calcular_distancia.return_value = 300

        assert isinstance(barco.get_sistema_navegacion(), AMotor)
        barco.navegar(modulo_gps) #Tiene un algoritmos que tiene más posibilidades que el viento sea favorable
        
        print (barco.get_combustible_actual())
        #El barco tiene 600L de nafta
        assert barco.get_combustible_actual() > (barco.get_combustible_maximo() - (barco.get_gasto_por_hora() *modulo_gps.calcular_tiempo())) 
        #El combustible al final del viaje es mayor que si hubiesemos viajado todo el recorrido con nafta.
        assert barco.get_combustible_actual() < barco.get_combustible_maximo() 
        #El combustible es menor al maximo porque alguna hora el viento no va a ser favorable. Algo de combustible vamos a gastar, realisticamente cuando arrancamos ya gastaríamos.
        assert barco.get_km_recorridos() == 300

    def test_prueba_barco_con_sensor_de_viento_mock_cambia_de_sistemas_correctamente_dependiendo_del_viento(self):
        sensor_viento_mock = Mock()
        selector_factory = SelectorCreador()
        factoria = selector_factory.crear_factoria_de_tipo_de_barco(TiposBarcos.BASICO)
        barco = factoria.crear_barco(1,400,3,600,sensor_viento_mock)
        
        modulo_gps = Mock()
        modulo_gps.calcular_tiempo.return_value = 10
        modulo_gps.calcular_distancia.return_value = 300

        sensor_viento_mock.medir_viento_favorable.return_value = False
        controlador = ControladorDeSistemaDeNavegacion()

        controlador.optimizar_navegacion(barco,sensor_viento_mock.medir_viento_favorable())
        assert isinstance(barco.get_sistema_navegacion(), AMotor)
        barco.navegar(modulo_gps) #Tiene un algoritmos que tiene más posibilidades que el viento sea favorable
        #600 - (10*6) = 600 - 60 = 540
        
        assert barco.get_combustible_actual() == 540
        assert isinstance(barco.get_sistema_navegacion(), AMotor)
        assert barco.get_combustible_gastado() == 60
        
        sensor_viento_mock.medir_viento_favorable.return_value = True
        controlador.optimizar_navegacion(barco,sensor_viento_mock.medir_viento_favorable())
        modulo_gps.calcular_tiempo.return_value = 3
        modulo_gps.calcular_distancia.return_value = 150

        barco.navegar(modulo_gps)
        
        
        assert isinstance(barco.get_sistema_navegacion(), AVela)
        assert barco.get_combustible_actual() == 540
        #540 - 0 = 540
        
        sensor_viento_mock.medir_viento_favorable.return_value = False
        controlador.optimizar_navegacion(barco,sensor_viento_mock.medir_viento_favorable())
        modulo_gps.calcular_tiempo.return_value = 5
        modulo_gps.calcular_distancia.return_value = 25

        barco.navegar(modulo_gps)
        #540 - 30 = 510
        
        assert barco.get_combustible_actual() == 510
        assert isinstance(barco.get_sistema_navegacion(), AMotor)
        assert barco.get_combustible_gastado() == 90
        assert barco.get_km_recorridos() == 475
        
        
    def test_prueba_navegar_tiempo_es_0(self):
        selector_factory = SelectorCreador()
        factoria = selector_factory.crear_factoria_de_tipo_de_barco(TiposBarcos.BASICO)
        barco = factoria.crear_barco(1,400,3,40)

        modulo_gps_real = ModuloGPS()
        with mock.patch.object(modulo_gps_real, 'calcular_tiempo', return_value= -10):
                    with self.assertRaises(tiempo_incorrecto):
                            barco.navegar(modulo_gps_real)
    
    
    def test_prueba_navegar_distancia_0(self):
        selector_factory = SelectorCreador()
        factoria = selector_factory.crear_factoria_de_tipo_de_barco(TiposBarcos.BASICO)
        barco = factoria.crear_barco(1,400,3,40)
        
        modulo_gps_real = ModuloGPS()
        with mock.patch.object(modulo_gps_real, 'calcular_distancia', return_value= -10):
                    with self.assertRaises(distancia_incorrecta):
                            barco.navegar(modulo_gps_real)

        