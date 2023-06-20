from unittest import TestCase
from unittest.mock import Mock, patch, MagicMock

'''from pytest import raises
from ContenedoresDirectorio.Builder.Builder_contenedor import Contenedor_builder
from ContenedoresDirectorio.Director.Contenedor_director import Contenedor_director
from ContenedoresDirectorio.Builder.BuilderContenedorBasico import BuilderContenedorBasico
from ContenedoresDirectorio.Builder.BuilderContenedorBasicoHc import BuilderContenedorBasicoHC
from ContenedoresDirectorio.Builder.BuilderContenedorFlatRack import BuilderContenedorFlatRack
from ContenedoresDirectorio.ManejadorDeCargas import ManejadorDeCargas
from Excepciones.exceptions import distancia_incorrecta
from Pedidos import Pedidos'''
from Cargas.Carga import Carga
from Cargas.Categorias import Categoria
from Medidas import Medidas
from ContenedoresDirectorio.TiposDeContenedores.Tipo import TipoContenedor
'''from BarcosDirectorio.BarcoBasico import BarcoBasico
from BarcosDirectorio.BarcoEspecial import BarcoEspecial
from BarcosDirectorio.Factory.CreadorDeBarcosBasicos import CreadorBarcosBasicos
from BarcosDirectorio.Factory.CreadorDeBarcosEspeciales import CreadorBarcosEspeciales'''
from BarcosDirectorio.Factory.SelectorDeCreador import SelectorCreador
from BarcosDirectorio.TiposDeBarcos import TiposBarcos
from ModuloGPS import ModuloGPS
from Modulo_Contable import ModuloContable


class TestModuloContable(TestCase):
    def test_distancia_menor_a_100_con_cargas_de_una_persona_y_gastamos_600_en_nafta(self):
        selector_de_factoria = SelectorCreador()
            
        creador_barcos_basicos = selector_de_factoria.crear_factoria(TiposBarcos.BASICO)
        
        #Seteo un barco:
        barco = creador_barcos_basicos.crear_barco(1,500,3,500)
        modulo_gps_mock = Mock()
        modulo_gps_mock.calcular_distancia.return_value = 99
        barco.set_combustible_gastado(100)
        
        #Carga y contenedor
        medidas = Medidas(3,2,2)
        carga = Carga(medidas,50,Categoria.MAQUINARIA)
        carga.set_id(1)
        
        carga2 = Carga(medidas,50,Categoria.MAQUINARIA)
        cargas = [carga,carga2]
        carga2.set_id(1)
        
        
        mock_contenedor = Mock()
        mock_contenedor.get_tipo.return_value = TipoContenedor.BASICO
        mock_contenedor.get_cargas.return_value = cargas #Esto no llenaría al contenedor, entonces se cobran $1000 cada carga
        mock_contenedor.get_precio_transporte_base.return_value = 500 #Si son iguales los IDS cobramos 500 una sola vez. 
        mock_contenedor.get_medidas_interior.return_value = Medidas(12.0,2.35,2.3)
        mock_contenedor.peso_contenedor.return_value = 100
        
        barco.cargar(mock_contenedor)
        modulo_contable = ModuloContable()
        
        assert modulo_contable.calcular_ganancia_barco(barco,6, modulo_gps_mock) == 1900
        #Estamos gastando $600 de nafta
        # $1000 de cada carga + 500 del precio base = $2500 - 600 = 900
    
    def test_distancia_menor_a_100_gastamos_600_en_nafta_con_cargas_de_mas_de_una_persona(self):
        selector_de_factoria = SelectorCreador()
            
        creador_barcos_basicos = selector_de_factoria.crear_factoria(TiposBarcos.BASICO)
        
        #Seteo un barco:
        barco = creador_barcos_basicos.crear_barco(1,500,3,500)
        modulo_gps_mock = Mock()
        modulo_gps_mock.calcular_distancia.return_value = 99
        barco.set_combustible_gastado(100)
        
        #Carga y contenedor
        medidas = Medidas(3,2,2)
        carga = Carga(medidas,50,Categoria.MAQUINARIA)
        carga.set_id(3)
        
        carga2 = Carga(medidas,50,Categoria.MAQUINARIA)
        carga2.set_id(800)
        
        cargas = [carga,carga2]

        
        mock_contenedor = Mock()
        mock_contenedor.get_tipo.return_value = TipoContenedor.BASICO
        mock_contenedor.get_cargas.return_value = cargas #Acá habría dos cargas de 50 kg cada una, entonces a cada persona debería cobrarsele $1000 por la carga y los $500 de precio base.
        mock_contenedor.get_precio_transporte_base.return_value = 500 
        mock_contenedor.get_medidas_interior.return_value = Medidas(12.0,2.35,2.3)
        mock_contenedor.peso_contenedor.return_value = 100
        
        barco.cargar(mock_contenedor)
        modulo_contable = ModuloContable()
        
        assert modulo_contable.calcular_ganancia_barco(barco,6, modulo_gps_mock) == 2400
        #Estamos gastando $600 de nafta
        # $2000 de las cargas + 500 del precio base a cada uno = $3000 - 600 = 2400
    
    def test_distancia_menor_a_100_gastamos_600_en_nafta_con_cargas_de_mas_de_una_persona_pero_una_tuvo_mas_de_una_carga(self):
        selector_de_factoria = SelectorCreador()
            
        creador_barcos_basicos = selector_de_factoria.crear_factoria(TiposBarcos.BASICO)
        
        #Seteo un barco:
        barco = creador_barcos_basicos.crear_barco(1,500,3,500)
        modulo_gps_mock = Mock()
        modulo_gps_mock.calcular_distancia.return_value = 99
        barco.set_combustible_gastado(100)
        
        #Carga y contenedor
        medidas = Medidas(3,2,2)
        carga = Carga(medidas,50,Categoria.MAQUINARIA)
        carga.set_id(3)
        
        carga2 = Carga(medidas,50,Categoria.MAQUINARIA)
        carga2.set_id(800)

        carga3 = Carga(medidas,50,Categoria.MAQUINARIA)
        cargas = [carga,carga2]
        carga3.set_id(3)
        
        cargas = [carga,carga2,carga3]
        
        
        
        mock_contenedor = Mock()
        mock_contenedor.get_tipo.return_value = TipoContenedor.BASICO
        mock_contenedor.get_cargas.return_value = cargas 
        mock_contenedor.get_precio_transporte_base.return_value = 500 
        mock_contenedor.get_medidas_interior.return_value = Medidas(12.0,2.35,2.3)
        mock_contenedor.peso_contenedor.return_value = 100
        
        barco.cargar(mock_contenedor)
        modulo_contable = ModuloContable()
        
        assert modulo_contable.calcular_ganancia_barco(barco,6, modulo_gps_mock) == 3400
        #Estamos gastando $600 de nafta
        #Acá habría tres cargas de 50 kg cada una, entonces a cada persona debería cobrarsele $1000 por la carga 
        #y los $500 de precio base. Hay dos cargas de la misma persona, entonces a una se le cobran $1000 por carga = 2000 + 500 precio base 2500
        #Y a la otra se le cobran $1000 de la carga y $500 del precio Base. Entonces cobramos unos $4000    
        # 4000 - 600
    
        
        