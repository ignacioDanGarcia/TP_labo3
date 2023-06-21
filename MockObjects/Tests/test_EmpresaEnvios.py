from unittest import TestCase
from unittest.mock import Mock, patch, MagicMock
from pytest import raises
from EmpresaDirectorio.EmpresaData import EmpresaData
from EmpresaDirectorio.EmpresaEnvios import EmpresaEnvios
from Camion import Camion
from Cargas.Carga import Carga
from Cargas.Categorias import Categoria
from ContenedoresDirectorio.Builder.BuilderContenedorOpenTop import BuilderContenedorOpenTop
from ContenedoresDirectorio.Director.Contenedor_director import Contenedor_director
from Medidas import Medidas
from EmpresaDirectorio.EmpresaData import EmpresaData


class TestEmpresaEnvios(TestCase):

    def test_hacer_viajar_camiones_verifico_contenedores(self):
       
     
        camion1 = Camion(154)
        camion2 = Camion(237)

        builder = BuilderContenedorOpenTop()
        director = Contenedor_director(builder)
        contenedores = []
        contenedores.append(director.crear_contenedor(1,False))
        medidas = Medidas(1,1,20)
        carga = Carga(medidas,50,Categoria.MAQUINARIA)

        contenedores.set_cargas(carga)

        camion1.set_contenedor(contenedores)
        camion2.set_contenedor(contenedores)
        
        camiones = [camion1,camion2]

        mock_barcos = Mock()
        empresa_data = EmpresaData([mock_barcos], camiones, contenedores)

        empresa_envios = EmpresaEnvios(empresa_data)

        empresa_envios.hacer_viajar_camiones(camiones)

        #cuando viaja el camion deja la carga, por lo que el contenedor debe estar vacion
        #al ser open top el contenedor no vuelve a la empresa, por lo que en empresa no debe estar el contenedor
        assert camion1.get_contenedor().get_cargas() == None
        assert camion1.get_contenedor().get_cargas() == None
        assert empresa_data.get_contenedores().index(camion1.get_contenedor()) == False
        assert empresa_data.get_contenedores().index(camion2.get_contenedor()) == False