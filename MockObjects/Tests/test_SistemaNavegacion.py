from types import NoneType
from unittest import TestCase
from unittest.mock import Mock, patch, MagicMock
from BarcosDirectorio.BarcoBasico import BarcoBasico
from BarcosDirectorio.SistemasNavegacion.Sensor_viento import SensorViento
from BarcosDirectorio.SistemasNavegacion.AMotor import AMotor
from BarcosDirectorio.SistemasNavegacion.AVela import AVela
from Excepciones.exceptions import CombustibleInsuficienteException
from BarcosDirectorio.SistemasNavegacion.ControladorDeNavegacion import ControladorDeSistemaDeNavegacion
from BarcosDirectorio.TiposDeBarcos import TiposBarcos
from BarcosDirectorio.Factory.SelectorDeCreador import SelectorCreador
from BarcosDirectorio.Factory.CreadorDeBarcosBasicos import CreadorBarcosBasicos
from BarcosDirectorio.Factory.CreadorDeBarcosEspeciales import CreadorBarcosEspeciales
import random
import time
class Tests_sistemasNavegacion(TestCase):
    def test_prueba_instanciar_barco_y_navegar_tiempo_suficiente(self):
        selector = SelectorCreador()
        factoria = selector.crear_factoria(TiposBarcos.BASICO)
        barco = factoria.crear_barco(400,3,40)
        # #El ultimo atributo es la cantidad de litros de combustible del barco
        assert barco.get_combustible_actual() == 40
        assert isinstance(barco.get_sistema_navegacion(), AMotor)
        if barco.puede_navegar(5):
            barco.navegar(5) #Acá paso las horas al barco. Gasta 6L * por hora 40 - 30 == 10
        
        assert barco.get_combustible_actual() == 10
        #assert isinstance(barco.get_sistema_navegacion(), AVela)
    
    def test_prueba_instanciar_barco_y_navegar_mas_tiempo_que_aguanta_su_nafta(self):
        selector = SelectorCreador()
        factoria = selector.crear_factoria(TiposBarcos.ESPECIAL)
        barco = factoria.crear_barco(400,3,10)
        #10 - 18 no alcanza, raiseo exception
        with self.assertRaises(CombustibleInsuficienteException):   
            if barco.puede_navegar(3):
                barco.navegar(3)
    
    def test_prueba_barco_con_sensor_de_viento_puede_ahorrar_nafta(self):
        sensor_viento = SensorViento()
        selector = SelectorCreador()
        factoria = selector.crear_factoria(TiposBarcos.BASICO)
        barco = factoria.crear_barco(400,3,600,sensor_viento)
        
        assert isinstance(barco.get_sistema_navegacion(), AMotor)
        horasViaje = 10
        barco.navegar(horasViaje) #Tiene un algoritmos que tiene más posibilidades que el viento sea favorable
        
        print (barco.get_combustible_actual())
        #El barco tiene 600L de nafta
        assert barco.get_combustible_actual() > (barco.get_combustible_maximo() - (barco.get_gasto_por_hora() *horasViaje)) 
        #El combustible al final del viaje es mayor que si hubiesemos viajado todo el recorrido con nafta.
        assert barco.get_combustible_actual() < barco.get_combustible_maximo() 
        #El combustible es menor al maximo porque alguna hora el viento no va a ser favorable. Algo de combustible vamos a gastar, realisticamente cuando arrancamos ya gastaríamos.


    def test_prueba_barco_con_sensor_de_viento_mock_cambia_de_sistemas_correctamente_dependiendo_del_viento(self):
        sensor_viento_mock = Mock()
        selector = SelectorCreador()
        factoria = selector.crear_factoria(TiposBarcos.BASICO)
        barco = factoria.crear_barco(400,3,600,sensor_viento_mock)
        
        sensor_viento_mock.medir_viento_favorable.return_value = False
        controlador = ControladorDeSistemaDeNavegacion()

        horasViaje = 10
        controlador.optimizar_navegacion(barco,sensor_viento_mock.medir_viento_favorable())
        assert isinstance(barco.get_sistema_navegacion(), AMotor)
        barco.navegar(horasViaje) #Tiene un algoritmos que tiene más posibilidades que el viento sea favorable
        #600 - (10*6) = 600 - 60 = 540
        
        assert barco.get_combustible_actual() == 540
        assert isinstance(barco.get_sistema_navegacion(), AMotor)
        assert barco.get_combustible_gastado() == 60
        
        sensor_viento_mock.medir_viento_favorable.return_value = True
        controlador.optimizar_navegacion(barco,sensor_viento_mock.medir_viento_favorable())
        horasViaje = 3
        barco.navegar(horasViaje)
        
        
        assert isinstance(barco.get_sistema_navegacion(), AVela)
        assert barco.get_combustible_actual() == 540
        #540 - 0 = 540
        
        sensor_viento_mock.medir_viento_favorable.return_value = False
        controlador.optimizar_navegacion(barco,sensor_viento_mock.medir_viento_favorable())
        horasViaje = 5
        barco.navegar(horasViaje)
        #540 - 30 = 510
        
        assert barco.get_combustible_actual() == 510
        assert isinstance(barco.get_sistema_navegacion(), AMotor)
        assert barco.get_combustible_gastado() == 90

