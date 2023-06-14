from unittest import TestCase
from unittest.mock import Mock, patch, MagicMock
import mock

from pytest import raises
from BarcosDirectorio.FactoryBarcos import FactoryBarcos
from BarcosDirectorio.BarcoEspecial import BarcoEspecial
from Excepciones.exceptions import Cantidad_contenedores_maxima_alcanzada_exception, Material_no_compatible_con_barco_Exceptionn, Peso_excedido_exception


class test_barcos(TestCase):
    def test_mat_aceptado(self):
        barco = BarcoEspecial(100,3,False)
        mock_contenedor = Mock()
        mock_contenedor.get_mat_especial.return_value = False
        assert barco.puede_cargar_esta_carga(mock_contenedor) == True
        #Testea si puede llevar el material de la carga del barco.
    
    def test_mat_aceptado2(self):
        barco = BarcoEspecial(100,3,True)
        mock_contenedor = Mock()
        mock_contenedor.get_mat_especial.return_value = False
        assert barco.puede_cargar_esta_carga(mock_contenedor) == True
        #Testea si puede llevar el material de la carga del barco. Si el barco es especial pero la carga no, no hay problema.
        
    def test_mat_aceptado3(self):
        barco = BarcoEspecial(100,3,True)
        mock_contenedor = Mock()
        mock_contenedor.get_mat_especial.return_value = True
        assert barco.puede_cargar_esta_carga(mock_contenedor) == True
        #Testea si la carga es especial y el barco también se puede llevar la carga. 
    
    def test_mat_no_aceptado(self):
        barco = BarcoEspecial(100,3,False)
        mock_contenedor = Mock()
        mock_contenedor.get_mat_especial.return_value = True
        with self.assertRaises(Material_no_compatible_con_barco_Exceptionn):
            barco.puede_cargar_esta_carga(mock_contenedor)
        #Testea si la carga es especial y el barco no la puede llevar que tire exception. 
        
    def test_carga_basico(self):
        barco = BarcoEspecial(100,3,False)
        mock_contenedor = Mock()
        mock_contenedor.peso_contenedor.return_value = 10
        mock_contenedor.get_mat_especial.return_value = False
        barco.cargar(mock_contenedor)
        assert (mock_contenedor in barco.contenedores)       
        #Testea si se puede cargar un barco cumpliendo condiciones basicas. 
        
    def test_peso_excedido(self):
        barco = BarcoEspecial(100,3,False)
        mock_contenedor = Mock()
        mock_contenedor.peso_contenedor.return_value = 900
        mock_contenedor.get_mat_especial.return_value = False

        with self.assertRaises(Peso_excedido_exception):
            barco.cargar(mock_contenedor)
        #testea si el peso del contenedor es superior al aceptado por el barco.


    
    def test_barco_con_capacidad_contenedores_al_tope(self):
        barco = BarcoEspecial(100,3,False)
        mock_contenedor1=Mock()
        mock_contenedor1.peso_contenedor.return_value =1
        mock_contenedor1.get_mat_especial.return_value = False
        
        mock_contenedor2 = Mock()
        mock_contenedor2.peso_contenedor.return_value =1
        mock_contenedor2.get_mat_especial.return_value = False
        
        mock_contenedor3 = Mock()
        mock_contenedor3.peso_contenedor.return_value =1
        mock_contenedor3.get_mat_especial.return_value = False
        
        barco.cargar(mock_contenedor1)
        barco.cargar(mock_contenedor2)
        barco.cargar(mock_contenedor3)
        
        mock_contenedor = Mock()
        mock_contenedor.peso_contenedor.return_value =80
        mock_contenedor.get_mat_especial.return_value = False
        
        with self.assertRaises(Cantidad_contenedores_maxima_alcanzada_exception):
            barco.tiene_lugar(mock_contenedor)
        #Testea si entra un contenedor por la cantidad de contenedores aceptada del barco. 
        
        
    def test_barco_con_peso_disponible_insuficiente(self):
        barco = BarcoEspecial(100,4,False)
        mock_contenedor1=Mock()
        mock_contenedor1.peso_contenedor.return_value =25
        mock_contenedor1.get_mat_especial.return_value = False
        
        mock_contenedor2 = Mock()
        mock_contenedor2.peso_contenedor.return_value =25
        mock_contenedor2.get_mat_especial.return_value = False
        
        mock_contenedor3 = Mock()
        mock_contenedor3.peso_contenedor.return_value =25
        mock_contenedor3.get_mat_especial.return_value = False
        
        barco.cargar(mock_contenedor1)
        barco.cargar(mock_contenedor2)
        barco.cargar(mock_contenedor3)
        
        mock_contenedor = Mock()
        mock_contenedor.peso_contenedor.return_value =33
        mock_contenedor.get_mat_especial.return_value = False
        
        with self.assertRaises(Peso_excedido_exception):
            barco.tiene_lugar(mock_contenedor)
        #Si tiene lugar disponible el barco pero el que intento agregar es más pesado tira exception.

    def test_barco_dinamico(self):
        barco = FactoryBarcos.crear_barco("Especial")(100,4,False)
        #Crea dinamicamente un barco del tipo que se le pase por parametro, en este caso "Especial"