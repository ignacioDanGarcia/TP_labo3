from unittest import TestCase
from unittest.mock import Mock, patch, MagicMock


from pytest import raises
from BarcosDirectorio.BarcoBasico import BarcoBasico
from BarcosDirectorio.BarcoEspecial import BarcoEspecial
from Excepciones.exceptions import Cantidad_contenedores_maxima_alcanzada_exception, Contenedor_no_aceptado_exception, Peso_excedido_exception
from ContenedoresDirectorio.TiposDeContenedores.TipoContenedor import TipoContenedor
from BarcosDirectorio.TiposDeBarcos import TiposBarcos
from BarcosDirectorio.Factory.SelectorDeCreador import SelectorCreador
from BarcosDirectorio.Factory.CreadorDeBarcosBasicos import CreadorBarcosBasicos
from BarcosDirectorio.Factory.CreadorDeBarcosEspeciales import CreadorBarcosEspeciales
from BarcosDirectorio.ManejadorDeContenedoresDirectorio.ManejadorDeContenedores import ManejadorDeContenedores
from BarcosDirectorio.ManejadorDeContenedoresDirectorio.SelectoraEstrategiaPorBarco import SelectoraEstrategiaPorBarco
class test_barcos(TestCase):
    
    def test_manejadora_contenedores_carga_contenedor_en_barco(self):
        selector_factory = SelectorCreador()
        creador = selector_factory.crear_factoria(TiposBarcos.ESPECIAL)
        selectora_de_estrategias_de_carga = SelectoraEstrategiaPorBarco()
        manejador_de_contenedores = ManejadorDeContenedores(selectora_de_estrategias_de_carga)
        barco = creador.crear_barco(1,100,3,500)
        mock_contenedor = Mock()
        mock_contenedor.get_tipo.return_value = TipoContenedor.BASICO
        mock_contenedor.peso_contenedor.return_value = 10
        mock_contenedor.get_material_especial.return_value = True
        
        assert manejador_de_contenedores.puede_cargar(barco, mock_contenedor) == True
        assert len(barco.get_contenedores()) == 0
        manejador_de_contenedores.cargar(barco,mock_contenedor)
        assert len(barco.get_contenedores()) == 1
        assert barco.obtener_peso_actual() == 10
        assert barco.get_contenedores().pop() == mock_contenedor

        
    def test_si_barco_basico_puede_cargar_carga_sin_material_especial(self):
        selector_factory = SelectorCreador()
        creador = selector_factory.crear_factoria(TiposBarcos.BASICO)
        selectora_de_estrategias_de_carga = SelectoraEstrategiaPorBarco()
        manejador_de_contenedores = ManejadorDeContenedores(selectora_de_estrategias_de_carga)
        barco = creador.crear_barco(1,100,3,500)
        mock_contenedor = Mock()
        mock_contenedor.get_tipo.return_value = TipoContenedor.BASICO
        mock_contenedor.peso_contenedor.return_value = 10
        mock_contenedor.get_material_especial.return_value = False
        
        assert manejador_de_contenedores.puede_cargar(barco, mock_contenedor) == True
    
    def test_si_barco_especial_puede_cargar_carga_sin_material_especial(self):
        selector_factory = SelectorCreador()
        creador = selector_factory.crear_factoria(TiposBarcos.ESPECIAL)
        
        barco = creador.crear_barco(1,100,3,500)
        
        selectora_de_estrategias_de_carga = SelectoraEstrategiaPorBarco()
        manejador_de_contenedores = ManejadorDeContenedores(selectora_de_estrategias_de_carga)
        
        mock_contenedor = Mock()
        mock_contenedor.get_tipo.return_value = TipoContenedor.BASICO
        mock_contenedor.get_material_especial.return_value = False
        mock_contenedor.peso_contenedor.return_value = 10
        assert manejador_de_contenedores.puede_cargar(barco,mock_contenedor)
    
        
    def test_si_barco_especial_puede_cargar_carga_con_material_especial(self):
        selector_factory = SelectorCreador()
        creador = selector_factory.crear_factoria(TiposBarcos.ESPECIAL)
        
        selectora_de_estrategias_de_carga = SelectoraEstrategiaPorBarco()
        manejador_de_contenedores = ManejadorDeContenedores(selectora_de_estrategias_de_carga)
        
        barco = creador.crear_barco(1,100,3,500)        
        mock_contenedor = Mock()
        mock_contenedor.get_tipo.return_value = TipoContenedor.FLATRACK
        mock_contenedor.get_material_especial.return_value = True
        mock_contenedor.peso_contenedor.return_value = 10
        assert manejador_de_contenedores.puede_cargar(barco, mock_contenedor) == True
    
    
    def test_barco_basico_no_puede_cargar_carga_con_material_especial(self):
        selector_factory = SelectorCreador()
        creador = selector_factory.crear_factoria(TiposBarcos.BASICO)
        
        selectora_de_estrategias_de_carga = SelectoraEstrategiaPorBarco()
        manejador_de_contenedores = ManejadorDeContenedores(selectora_de_estrategias_de_carga)
        
        barco = creador.crear_barco(1,100,3,500)
        mock_contenedor = Mock()
        mock_contenedor.get_tipo.return_value = TipoContenedor.FLATRACK
        mock_contenedor.get_material_especial.return_value = True
        mock_contenedor.peso_contenedor.return_value = 50
        assert False == manejador_de_contenedores.puede_cargar(barco, mock_contenedor)
        
    
    def test_metodo_cargar_de_barco_carga_contenedor_sin_material_especial_y_peso_bajo(self):
        selector_factory = SelectorCreador()
        creador = selector_factory.crear_factoria(TiposBarcos.ESPECIAL)
        
        selectora_de_estrategias_de_carga = SelectoraEstrategiaPorBarco()
        manejador_de_contenedores = ManejadorDeContenedores(selectora_de_estrategias_de_carga)
        
        barco = creador.crear_barco(1,100,3,500) 
        mock_contenedor = Mock()
        mock_contenedor.get_tipo.return_value = TipoContenedor.BASICO
        mock_contenedor.peso_contenedor.return_value = 10
        mock_contenedor.get_material_especial.return_value = False
        manejador_de_contenedores.cargar(barco, mock_contenedor)
        
        assert mock_contenedor in barco.contenedores 
    
    def test_metodo_cargar_de_barco_no_carga_por_excepcion_por_peso_excedido(self):
        selector_factory = SelectorCreador()
        creador = selector_factory.crear_factoria(TiposBarcos.ESPECIAL)
        
        selectora_de_estrategias_de_carga = SelectoraEstrategiaPorBarco()
        manejador_de_contenedores = ManejadorDeContenedores(selectora_de_estrategias_de_carga)
        
        barco = creador.crear_barco(1,100,3,500) 
        mock_contenedor = Mock()
        mock_contenedor.get_tipo.return_value = TipoContenedor.FLATRACK
        mock_contenedor.peso_contenedor.return_value = 900
        mock_contenedor.get_material_especial.return_value = False
        
        '''with self.assertRaises(Peso_excedido_exception):
            manejador_de_contenedores.cargar(barco, mock_contenedor)'''
        assert manejador_de_contenedores.cargar(barco,mock_contenedor) == False
    
    
    def test_metodo_tiene_lugar_de_barco_tira_exception_por_capacidad_contenedores_al_tope(self):
        selector_factory = SelectorCreador()
        creador = selector_factory.crear_factoria(TiposBarcos.ESPECIAL)
        
        barco = creador.crear_barco(1,100,3,500) 
        mock_contenedor1=Mock()
        mock_contenedor1.peso_contenedor.return_value =1
        mock_contenedor1.get_material_especial.return_value = False
        mock_contenedor1.get_tipo.return_value = TipoContenedor.FLATRACK
        
        mock_contenedor2 = Mock()
        mock_contenedor2.peso_contenedor.return_value =1
        mock_contenedor2.get_material_especial.return_value = False
        mock_contenedor2.get_tipo.return_value = TipoContenedor.FLATRACK
        
        mock_contenedor3 = Mock()
        mock_contenedor3.peso_contenedor.return_value =1
        mock_contenedor3.get_material_especial.return_value = False
        mock_contenedor3.get_tipo.return_value = TipoContenedor.FLATRACK
        
        
        
        selectora_de_estrategias_de_carga = SelectoraEstrategiaPorBarco()
        manejador_de_contenedores = ManejadorDeContenedores(selectora_de_estrategias_de_carga)
        
        manejador_de_contenedores.cargar(barco,mock_contenedor1)
        manejador_de_contenedores.cargar(barco,mock_contenedor2)
        manejador_de_contenedores.cargar(barco,mock_contenedor3)
        mock_contenedor = Mock()
        mock_contenedor.peso_contenedor.return_value =80
        mock_contenedor.get_material_especial.return_value = False
        mock_contenedor.get_tipo.return_value = TipoContenedor.FLATRACK
        
        '''with self.assertRaises(Cantidad_contenedores_maxima_alcanzada_exception):
            barco.tiene_lugar(mock_contenedor)'''
            
        assert manejador_de_contenedores.puede_cargar(barco,mock_contenedor) == False
    
    def test_metodo_tiene_lugar_de_barco_tira_exception_por_peso_maximo_excedido(self):
        selector_factory = SelectorCreador()
        creador = selector_factory.crear_factoria(TiposBarcos.ESPECIAL)
        
        barco = creador.crear_barco(1,100,4,500) 
        mock_contenedor1=Mock()
        mock_contenedor1.peso_contenedor.return_value =25
        mock_contenedor1.get_material_especial.return_value = False
        mock_contenedor1.get_tipo.return_value = TipoContenedor.FLATRACK
        
        mock_contenedor2 = Mock()
        mock_contenedor2.peso_contenedor.return_value =25
        mock_contenedor2.get_material_especial.return_value = False
        mock_contenedor2.get_tipo.return_value = TipoContenedor.FLATRACK
        
        mock_contenedor3 = Mock()
        mock_contenedor3.peso_contenedor.return_value =25
        mock_contenedor3.get_material_especial.return_value = False
        mock_contenedor3.get_tipo.return_value = TipoContenedor.FLATRACK
        
        selectora_de_estrategias_de_carga = SelectoraEstrategiaPorBarco()
        manejador_de_contenedores = ManejadorDeContenedores(selectora_de_estrategias_de_carga)
        
        
        manejador_de_contenedores.cargar(barco,mock_contenedor1)
        manejador_de_contenedores.cargar(barco,mock_contenedor2)
        manejador_de_contenedores.cargar(barco,mock_contenedor3)
        
        mock_contenedor = Mock()
        mock_contenedor.peso_contenedor.return_value =33
        mock_contenedor.get_material_especial.return_value = False
        mock_contenedor.get_tipo.return_value = TipoContenedor.FLATRACK
        
        '''with self.assertRaises(Peso_excedido_exception):
            manejador_de_contenedores.puede_cargar(barco, mock_contenedor)'''
        
        assert manejador_de_contenedores.puede_cargar(barco, mock_contenedor) == False
    
    
    def test_barco_basico_creado_con_factory_tira_exception_por_peso_maximo_excedido(self):
        selector_factory = SelectorCreador()
        creador = selector_factory.crear_factoria(TiposBarcos.BASICO)
        
        barco = creador.crear_barco(1,100,4,500)
        mock_contenedor1=Mock()
        mock_contenedor1.peso_contenedor.return_value =25
        mock_contenedor1.get_material_especial.return_value = False
        mock_contenedor1.get_tipo.return_value = TipoContenedor.BASICO
        
        mock_contenedor2 = Mock()
        mock_contenedor2.peso_contenedor.return_value =25
        mock_contenedor2.get_material_especial.return_value = False
        mock_contenedor2.get_tipo.return_value = TipoContenedor.BASICO
        
        mock_contenedor3 = Mock()
        mock_contenedor3.peso_contenedor.return_value =25
        mock_contenedor3.get_material_especial.return_value = False
        mock_contenedor3.get_tipo.return_value = TipoContenedor.BASICO
        
        selectora_de_estrategias_de_carga = SelectoraEstrategiaPorBarco()
        manejador_de_contenedores = ManejadorDeContenedores(selectora_de_estrategias_de_carga)
        
        manejador_de_contenedores.cargar(barco,mock_contenedor1)
        manejador_de_contenedores.cargar(barco,mock_contenedor2)
        manejador_de_contenedores.cargar(barco,mock_contenedor3)
        
        mock_contenedor = Mock()
        mock_contenedor.peso_contenedor.return_value = 33
        mock_contenedor.get_material_especial.return_value = False
        mock_contenedor.get_tipo.return_value = TipoContenedor.BASICO
        
        assert manejador_de_contenedores.puede_cargar(barco,mock_contenedor) == False
    
    
    def test_barco_basico_creado_con_factory_tira_exception_por_cantidad_contenedores_al_tope(self):
        selector_factory = SelectorCreador()
        creador = selector_factory.crear_factoria(TiposBarcos.BASICO)
        
        barco = creador.crear_barco(1,100,3,500)
        mock_contenedor1=Mock()
        mock_contenedor1.peso_contenedor.return_value =1
        mock_contenedor1.get_material_especial.return_value = False
        mock_contenedor1.get_tipo.return_value = TipoContenedor.BASICO
        
        mock_contenedor2 = Mock()
        mock_contenedor2.peso_contenedor.return_value =1
        mock_contenedor2.get_material_especial.return_value = False
        mock_contenedor2.get_tipo.return_value = TipoContenedor.BASICO
        
        mock_contenedor3 = Mock()
        mock_contenedor3.peso_contenedor.return_value =1
        mock_contenedor3.get_material_especial.return_value = False
        mock_contenedor3.get_tipo.return_value = TipoContenedor.BASICO
        
        selectora_de_estrategias_de_carga = SelectoraEstrategiaPorBarco()
        manejador_de_contenedores = ManejadorDeContenedores(selectora_de_estrategias_de_carga)
        
        manejador_de_contenedores.cargar(barco,mock_contenedor1)
        manejador_de_contenedores.cargar(barco,mock_contenedor2)
        manejador_de_contenedores.cargar(barco,mock_contenedor3)
        
        mock_contenedor = Mock()
        mock_contenedor.peso_contenedor.return_value =80
        mock_contenedor.get_material_especial.return_value = False
        mock_contenedor.get_tipo.return_value = TipoContenedor.BASICO
        
        assert manejador_de_contenedores.puede_cargar(barco, mock_contenedor)== False
    
    
    def test_barco_especial_creado_con_factory(self):
        # entre comillas hay que poner el nombre de la subclase, no solamente especial
        # la subclase se llama BarcoEspecial
        selector_factory = SelectorCreador()
        creador = selector_factory.crear_factoria(TiposBarcos.ESPECIAL)
        
        barco = creador.crear_barco(1,100,4,500)         
        assert isinstance(barco, BarcoEspecial)
        
     
    def test_barco_basico_creado_con_factory(self):
        # entre comillas hay que poner el nombre de la subclase, no solamente basico
        # la subclase se llama BarcoBasico
        selector_factory = SelectorCreador()
        creador = selector_factory.crear_factoria(TiposBarcos.BASICO)
        
        barco = creador.crear_barco(1,100,4,500) 
        assert isinstance(barco, BarcoBasico)