from abc import ABC,abstractmethod
from Medidas_contenedores import Medidas

class Contenedor(ABC):

    #Cada contenedor define un precio base que se debe pagar para transportar una determinada carga.
    # a esto debe sumarse el precio que se debe pagar por la carga, este precio se define en carga
    
    def __init__(self, id, precio_transporte_carga):
        self.id = id
        self.precio_transporte_carga = precio_transporte_carga
        self.volumen_max = 0.0
        self.peso_max = 0.0
        self.medidas_interior = None
        self.medidas_exterior = None
    
    
    @abstractmethod
    def getVolumen(self):
        pass


    
