from BarcosDirectorio.Barcos import Barco
from Camion import Camion
from EmpresaData import EmpresaData
"""
CLASE QUE HACE VIAJAR A LOS VEHICULOS
"""

class EmpresaEnvios():
    def __init__(self, empresa_data : EmpresaData) -> None:
        self.administracion_empresa = empresa_data
    
        """
        recibe los barcos o camiones llenos y los hace "viajar"
        o los pone en modo viajando que seria disponible = False
        """
    def hacer_viajar_barcos(self, barcos):
        for barco in barcos:
            if barco.puede_navegar():
                barco.navegar()
                    
    def hacer_viajar_camiones(self,camiones):
        for camion in camiones:
            camion.viajar()
            camion.descargar()
            self.administracion_empresa.vaciar_contenedor_entregado_con_envio(camion.get_contenedor())
            

