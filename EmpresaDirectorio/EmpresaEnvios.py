from BarcosDirectorio.Barcos import Barco
from Camion import Camion
from Interfaces.ViajeraInterfaz import ViajeraInterfaz
"""
CLASE QUE HACE VIAJAR A LOS VEHICULOS
"""

class EmpresaEnvios(ViajeraInterfaz):
    def __init__(self) -> None:
        pass
    
        """
        recibe los barcos o camiones llenos y los hace "viajar"
        o los pone en modo viajando que seria disponible = False
        """