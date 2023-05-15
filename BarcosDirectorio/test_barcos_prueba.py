from unittest import TestCase
from unittest.mock import Mock, patch, MagicMock

from pytest import raises
from BarcosDirectorio.Barco_especial import Barco_especial
from BarcosDirectorio.Excepciones.exceptions import Cantidad_contenedores_maxima_alcanzada_exception, Peso_excedido_exception


class test_barcos(TestCase):
    def test_mat_aceptado(self):
        barco = Barco_especial(1,100,3,False)
        mock_contenedor = Mock()
        mock_contenedor.get_mat_especial.return_value = False
        assert barco.puede_cargar_esta_carga(mock_contenedor) == True
        #Testea si puede llevar el material de la carga del barco.
        
        
    def test_peso_excedido(self):
        barco = Barco_especial(1,100,3,False)
        mock_contenedor = Mock()
        mock_contenedor.peso_contenedor.return_value = 900
        mock_contenedor.get_mat_especial.return_value = False

        with self.assertRaises(Peso_excedido_exception):
            barco.cargar(mock_contenedor)
        #testea si el peso del contenedor es superior al aceptado por el barco.


    
    def test_barco_con_capacidad_contenedores_al_tope(self):
        barco = Barco_especial(1,100,3,False)
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
    