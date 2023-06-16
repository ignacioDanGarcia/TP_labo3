from unittest import TestCase
from unittest.mock import Mock, patch, MagicMock


from pytest import raises
from BarcosDirectorio.BarcoBasico import BarcoBasico
from BarcosDirectorio.BarcoEspecial import BarcoEspecial
from BarcosDirectorio.FactoryBarcos import FactoryBarcos
from Excepciones.exceptions import Cantidad_contenedores_maxima_alcanzada_exception, Material_no_compatible_con_barco_Exceptionn, Peso_excedido_exception


class test_barcos(TestCase):
    
    def test_si_barco_no_especial_puede_cargar_carga_sin_material_especial(self):
        barco = BarcoEspecial(100,3,False)
        mock_contenedor = Mock()
        mock_contenedor.get_material_especial.return_value = False
        assert barco.puede_cargar_esta_carga(mock_contenedor) == True
        
    
    def test_si_barco_especial_puede_cargar_carga_sin_material_especial(self):
        barco = BarcoEspecial(100,3,True)
        mock_contenedor = Mock()
        mock_contenedor.get_material_especial.return_value = False
        assert barco.puede_cargar_esta_carga(mock_contenedor) == True
    
        
    def test_si_barco_especial_puede_cargar_carga_con_material_especial(self):
        barco = BarcoEspecial(100,3,True)
        mock_contenedor = Mock()
        mock_contenedor.get_material_especial.return_value = True
        assert barco.puede_cargar_esta_carga(mock_contenedor) == True
    
    
    def test_barco_no_especial_no_puede_cargar_carga_con_material_especial(self):
        barco = BarcoEspecial(100,3,False)
        mock_contenedor = Mock()
        mock_contenedor.get_material_especial.return_value = True
        with self.assertRaises(Material_no_compatible_con_barco_Exceptionn):
            barco.puede_cargar_esta_carga(mock_contenedor)
        
    
    def test_metodo_cargar_de_barco_carga_contenedor_sin_material_especial_y_peso_bajo(self):
        barco = BarcoEspecial(100,3,False)
        mock_contenedor = Mock()
        mock_contenedor.peso_contenedor.return_value = 10
        mock_contenedor.get_material_especial.return_value = False
        barco.cargar(mock_contenedor)
        assert mock_contenedor in barco.contenedores 
        
    
    def test_metodo_cargar_de_barco_no_carga_por_excepcion_por_peso_excedido(self):
        barco = BarcoEspecial(100,3,False)
        mock_contenedor = Mock()
        mock_contenedor.peso_contenedor.return_value = 900
        mock_contenedor.get_material_especial.return_value = False

        with self.assertRaises(Peso_excedido_exception):
            barco.cargar(mock_contenedor)

    
    def test_metodo_tiene_lugar_de_barco_tira_exception_por_capacidad_contenedores_al_tope(self):
        barco = BarcoEspecial(100,3,False)
        mock_contenedor1=Mock()
        mock_contenedor1.peso_contenedor.return_value =1
        mock_contenedor1.get_material_especial.return_value = False
        
        mock_contenedor2 = Mock()
        mock_contenedor2.peso_contenedor.return_value =1
        mock_contenedor2.get_material_especial.return_value = False
        
        mock_contenedor3 = Mock()
        mock_contenedor3.peso_contenedor.return_value =1
        mock_contenedor3.get_material_especial.return_value = False
        
        barco.cargar(mock_contenedor1)
        barco.cargar(mock_contenedor2)
        barco.cargar(mock_contenedor3)
        
        mock_contenedor = Mock()
        mock_contenedor.peso_contenedor.return_value =80
        mock_contenedor.get_material_especial.return_value = False
        
        with self.assertRaises(Cantidad_contenedores_maxima_alcanzada_exception):
            barco.tiene_lugar(mock_contenedor)
        
    
    def test_metodo_tiene_lugar_de_barco_tira_exception_por_peso_maximo_excedido(self):
        barco = BarcoEspecial(100,4,False)
        mock_contenedor1=Mock()
        mock_contenedor1.peso_contenedor.return_value =25
        mock_contenedor1.get_material_especial.return_value = False
        
        mock_contenedor2 = Mock()
        mock_contenedor2.peso_contenedor.return_value =25
        mock_contenedor2.get_material_especial.return_value = False
        
        mock_contenedor3 = Mock()
        mock_contenedor3.peso_contenedor.return_value =25
        mock_contenedor3.get_material_especial.return_value = False
        
        barco.cargar(mock_contenedor1)
        barco.cargar(mock_contenedor2)
        barco.cargar(mock_contenedor3)
        
        mock_contenedor = Mock()
        mock_contenedor.peso_contenedor.return_value =33
        mock_contenedor.get_material_especial.return_value = False
        
        with self.assertRaises(Peso_excedido_exception):
            barco.tiene_lugar(mock_contenedor)
    
        
    """
    def test_mat_no_aceptado_basico(self):
        barco = BarcoBasico(100,3,False)
        mock_contenedor = Mock()
        mock_contenedor.get_material_especial.return_value = True
        mock_contenedor.get_tipo.return_value = 'Basico'
        with self.assertRaises(Material_no_compatible_con_barco_Exceptionn):
            barco.puede_cargar_esta_carga(mock_contenedor)
        #Testea si la carga es especial y el barco no la puede llevar que tire exception. 
    
    
    def test_mat_no_aceptado_basico2(self):
        barco = BarcoBasico(100,3,True)
        mock_contenedor = Mock()
        mock_contenedor.get_material_especial.return_value = False
        mock_contenedor.get_tipo.return_value = 'Basico'
        with self.assertRaises(Material_no_compatible_con_barco_Exceptionn):
            barco.puede_cargar_esta_carga(mock_contenedor)
        #Testea si la carga no especial y el barco la puede llevar que no tire exception. 
    """
    
    def test_barco_basico_creado_con_factory_tira_exception_por_peso_maximo_excedido(self):
        barco = FactoryBarcos.crear_barco("BarcoBasico",100,4,False)
        mock_contenedor1=Mock()
        mock_contenedor1.peso_contenedor.return_value =25
        mock_contenedor1.get_material_especial.return_value = False
        mock_contenedor1.get_tipo.return_value = 'Basico'
        
        mock_contenedor2 = Mock()
        mock_contenedor2.peso_contenedor.return_value =25
        mock_contenedor2.get_material_especial.return_value = False
        mock_contenedor2.get_tipo.return_value = 'Basico'
        
        mock_contenedor3 = Mock()
        mock_contenedor3.peso_contenedor.return_value =25
        mock_contenedor3.get_material_especial.return_value = False
        mock_contenedor3.get_tipo.return_value = 'Basico'
        
        barco.cargar(mock_contenedor1)
        barco.cargar(mock_contenedor2)
        barco.cargar(mock_contenedor3)
        
        mock_contenedor = Mock()
        mock_contenedor.peso_contenedor.return_value =33
        mock_contenedor.get_material_especial.return_value = False
        mock_contenedor.get_tipo.return_value = 'Basico'
        
        with self.assertRaises(Peso_excedido_exception):
            barco.tiene_lugar(mock_contenedor)
    
    
    def test_barco_basico_creado_con_factory_tira_exception_por_cantidad_contenedores_al_tope(self):
        barco = FactoryBarcos.crear_barco("BarcoBasico",100,3,False)
        mock_contenedor1=Mock()
        mock_contenedor1.peso_contenedor.return_value =1
        mock_contenedor1.get_material_especial.return_value = False
        mock_contenedor1.get_tipo.return_value = 'Basico'
        
        mock_contenedor2 = Mock()
        mock_contenedor2.peso_contenedor.return_value =1
        mock_contenedor2.get_material_especial.return_value = False
        mock_contenedor2.get_tipo.return_value = 'Basico'
        
        mock_contenedor3 = Mock()
        mock_contenedor3.peso_contenedor.return_value =1
        mock_contenedor3.get_material_especial.return_value = False
        mock_contenedor3.get_tipo.return_value = 'Basico'
        
        barco.cargar(mock_contenedor1)
        barco.cargar(mock_contenedor2)
        barco.cargar(mock_contenedor3)
        
        mock_contenedor = Mock()
        mock_contenedor.peso_contenedor.return_value =80
        mock_contenedor.get_material_especial.return_value = False
        mock_contenedor.get_tipo.return_value = 'Basico'
        
        with self.assertRaises(Cantidad_contenedores_maxima_alcanzada_exception):
            barco.tiene_lugar(mock_contenedor)
    
    
    def test_barco_especial_creado_con_factory(self):
        # entre comillas hay que poner el nombre de la subclase, no solamente especial
        # la subclase se llama BarcoEspecial
        barco = FactoryBarcos.crear_barco("BarcoEspecial",100,4,False)
        assert isinstance(barco, BarcoEspecial)
        
        
    def test_barco_basico_creado_con_factory(self):
        # entre comillas hay que poner el nombre de la subclase, no solamente basico
        # la subclase se llama BarcoBasico
        barco = FactoryBarcos.crear_barco("BarcoBasico",100,4,False)
        assert isinstance(barco, BarcoBasico)