from abc import ABC


class Contenedor(ABC):

    #Cada contenedor define un precio base que se debe pagar para transportar una determinada carga.
    # a esto debe sumarse el precio que se debe pagar por la carga, este precio se define en carga
    
    def __init__(self, id, precio_transporte_carga):
        self.id = id
        self.precio_transporte_carga = precio_transporte_carga
        self.volumen = 0.0
        self.peso = 0.0
        self.medidas_interior = None
        self.medidas_exterior = None
    
    
    @abc.abstractmethod
    def getVolumen(self):
        pass


    
