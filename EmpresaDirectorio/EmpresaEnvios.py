from BarcosDirectorio.Barcos import Barco
from Camion import Camion
from EmpresaDirectorio.EmpresaData import EmpresaData
from Excepciones.exceptions import CombustibleInsuficienteException, tiempo_incorrecto
from ContenedoresDirectorio.TiposDeContenedores.TipoContenedor import TipoContenedor
from ContenedoresDirectorio.SelectoraEstrategiaPorCarga import SelectoraEstrategiaPorCarga
from ContenedoresDirectorio.ManejadorDeCargas import ManejadorDeCargas
"""
CLASE QUE HACE VIAJAR A LOS VEHICULOS
"""

class EmpresaEnvios():
    def __init__(self, empresa_data : EmpresaData) -> None:
        self.administracion_empresaData = empresa_data
    
        """
        recibe los barcos o camiones llenos y los hace "viajar"
        o los pone en modo viajando que seria disponible = False
      
      """
        
    def get_administracion(self):
        return self.administracion_empresaData

    def hacer_viajar_barcos(self, barcos, gps):
        for barco in barcos:
            try:
                barco.puede_navegar(gps) # este metodo lanza excepcion
                barco.navegar(gps)
            except CombustibleInsuficienteException as e:
                print(e.mensaje)

                    

    def descargar_contenedores_barcos(self, barcos):
        #lista_con_todos_los_contenedores = []

        for barco in barcos:
    
            barco.set_disponible(True)
            barco.set_combustible_gastado(0)
            barco.set_km_recorridos(0)
            barco.set_contenedores(None)

       
    def hacer_viajar_camiones(self,camiones):
        for camion in camiones:
            camion.viajar()
    
    def descargar_contenedor_camiones(self, camiones):
        for camion in camiones:
            if camion.get_contenedor().get_tipo() == TipoContenedor.OPENTOP :
                self.administracion_empresaData.remove(camion.get_contenedor())
            else:
                camion.set_contenedor(None)
                camion.set_disponible(True)



            

